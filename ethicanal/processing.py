import sys
import os
import json
import sqlite3
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Añadir el directorio del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import MODEL_NAME, CODE_OF_CONDUCT, PROMPT_TEMPLATE, FLAGS

# Inicializar el modelo y el parser
llm = Ollama(model=MODEL_NAME)
output_parser = StrOutputParser()

# Definir el prompt
prompt = ChatPromptTemplate.from_messages(PROMPT_TEMPLATE)

# Crear la cadena de procesamiento
chain = prompt | llm | output_parser

# Definir el nombre y la ubicación del archivo de la base de datos
database_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'ethbot.db')

def process_comment(comment_to_analyze):
    """
    Procesa un comentario dado usando el modelo LLM y devuelve el análisis en formato JSON.
    """
    response = chain.invoke({"input": CODE_OF_CONDUCT + comment_to_analyze})
    return response

def analyze_comment_json(comment_json):
    """
    Extrae el comentario de un JSON, lo analiza y devuelve el resultado.
    """
    # Extraer el comentario del JSON
    comment_to_analyze = comment_json["comment_body"]
    
    # Procesar el comentario
    result = process_comment(comment_to_analyze)
    
    # Convertir el resultado JSON en un diccionario
    result_dict = json.loads(result)
    
    # Generar la lista numerada de banderas (flags) según la configuración en config.py
    flags = result_dict.get("flags", [])
    numbered_flags = {FLAGS[flag]: flag for flag in flags if flag in FLAGS}
    
    # Agregar las banderas numeradas al resultado
    result_dict["numbered_flags"] = numbered_flags
    
    # Agregar el resultado del modelo al JSON original
    comment_json["analysis"] = result_dict
    
    return comment_json

def create_table_if_not_exists(repo_name):
    """
    Crea una tabla con el nombre del repositorio si no existe.
    """
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {repo_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comment_id TEXT NOT NULL,
                user TEXT NOT NULL,
                user_id TEXT NOT NULL,
                comment_body TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                classification TEXT NOT NULL,
                reasons TEXT NOT NULL,
                numbered_flags TEXT NOT NULL,
                issue_number TEXT,
                issue_title TEXT,
                issue_body TEXT,
                issue_url TEXT,
                comment_url TEXT,
                repository_name TEXT,
                repository_full_name TEXT,
                repository_html_url TEXT
            )
        ''')
        conn.commit()

def save_comment_to_db(comment_json):
    """
    Guarda el comentario analizado en la base de datos en una tabla con el nombre del repositorio.
    """
    analysis = comment_json["analysis"]
    
    # Convertir las listas de flags a cadenas JSON
    numbered_flags_json = json.dumps(analysis["numbered_flags"])
    
    # Nombre de la tabla basado en el nombre del repositorio
    repo_name = comment_json["repository_name"].replace("/", "_")
    
    # Crear la tabla si no existe
    create_table_if_not_exists(repo_name)
    
    # Insertar el comentario en la tabla correspondiente
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {repo_name} (
                comment_id, user, user_id, comment_body, created_at, updated_at, 
                classification, reasons, numbered_flags,
                issue_number, issue_title, issue_body, issue_url, 
                comment_url, repository_name, repository_full_name, repository_html_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            comment_json["comment_id"],
            comment_json["user"],
            comment_json["user_id"],
            comment_json["comment_body"],
            comment_json["created_at"],
            comment_json["updated_at"],
            analysis["classification"],
            analysis["reasons"],
            numbered_flags_json,
            comment_json["issue_number"],
            comment_json["issue_title"],
            comment_json["issue_body"],
            comment_json["issue_url"],
            comment_json["comment_url"],
            comment_json["repository_name"],
            comment_json["repository_full_name"],
            comment_json["repository_html_url"]
        ))
        conn.commit()

if __name__ == "__main__":
    # JSON de ejemplo
    example_json = {
        "comment_id": "2136686641",
        "user": "CobosDS",
        "user_id": "126188600",
        "user_avatar_url": "https://avatars.githubusercontent.com/u/126188600?v=4",
        "user_html_url": "https://github.com/CobosDS",
        "user_type": "User",
        "issue_number": "4",
        "issue_title": "Hate speech test",
        "issue_body": "💣 Describe the issue or problem you detected\r\n\r\n(Write your answer here.)\r\n\r\n📋 Provide the solution you'd like\r\n\r\n(Describe your proposed solution here.)\r\n\r\n🤔 If any, describe alternatives you've considered\r\n\r\n(Write your answer here.)\r\n",
        "comment_body": "That issue is useless",
        "created_at": "2024-05-29T07:05:50Z",
        "updated_at": "2024-05-29T07:05:50Z",
        "issue_url": "https://github.com/CobosDS/botests/issues/4",
        "comment_url": "https://github.com/CobosDS/botests/issues/4#issuecomment-2136686641",
        "repository_name": "CobosDS/botests",
        "repository_full_name": "",
        "repository_html_url": ""
    }

    # Ejecutar el análisis
    result = analyze_comment_json(example_json)
    
     # Imprimir el resultado
    print(json.dumps(result, indent=2))

    # Guardar el resultado en la base de datos
    save_comment_to_db(result)
    
   
