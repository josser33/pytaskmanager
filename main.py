from utils.archivos import cargar_datos, guardar_datos
from modules.menu import iniciar_aplicacion

def main():
    print("Iniciando Sistema de Gestión de Tareas...")
    
    lista_tareas = cargar_datos()
    
    iniciar_aplicacion(lista_tareas)
    
    guardar_datos(lista_tareas)
    print("Datos guardados exitosamente. ¡Hasta luego!")

if __name__ == "__main__":
    main()