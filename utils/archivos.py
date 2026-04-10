import json
import os

RUTA_ARCHIVO = 'data/tareas.json'

def cargar_datos():
    """
    Lee el archivo JSON y retorna la lista de tareas.
    Si el archivo no existe o está vacío, retorna una lista vacía.
    """
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists(RUTA_ARCHIVO):
        guardar_datos([])
        return []

    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except json.JSONDecodeError:
        return []

def guardar_datos(datos):
    """
    Toma una lista de diccionarios (tareas) y la guarda en el archivo JSON.
    """
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)