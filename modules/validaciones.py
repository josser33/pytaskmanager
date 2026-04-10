from datetime import datetime

def validar_no_vacio(texto_solicitud):
    """
    Pide un dato al usuario y no permite que sea una cadena vacía.
    """
    while True:
        valor = input(texto_solicitud).strip()
        if valor:
            return valor
        print("[!] Error: Este campo no puede quedar vacío.")

def validar_opcion_prioridad():
    """
    Asegura que la prioridad sea una de las tres permitidas.
    """
    opciones = ["Alta", "Media", "Baja"]
    while True:
        valor = input("Prioridad (Alta/Media/Baja): ").capitalize()
        if valor in opciones:
            return valor
        print("[!] Error: Por favor, escribe 'Alta', 'Media' o 'Baja'.")

def buscar_por_id(tareas, mensaje="Ingrese el ID de la tarea: "):
    """
    Valida que el ID ingresado sea un número y que exista en la lista.
    """
    while True:
        try:
            id_buscado = int(input(mensaje))
            for tarea in tareas:
                if tarea['id'] == id_buscado:
                    return tarea, id_buscado
            print(f"[!] No se encontró ninguna tarea con el ID {id_buscado}.")
            return None, None
        except ValueError:
            print("[!] Error: Debe ingresar un número entero para el ID.")

def validar_fecha(texto_solicitud):
    """
    Asegura que el usuario ingrese una fecha válida en formato DD/MM/AAAA.
    """
    while True:
        fecha_str = input(texto_solicitud).strip()
        try:
            fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
            
            return fecha_str
        except ValueError:
            print("[!] Error: Fecha inválida o formato incorrecto. Use DD/MM/AAAA (Ej: 01/03/2026).")