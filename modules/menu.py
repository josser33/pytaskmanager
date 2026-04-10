from modules.operaciones import registrar_tarea, listar_tareas, buscar_tarea, eliminar_tarea, editar_tarea
from modules.reportes import mostrar_resumen

def mostrar_menu():
    """
    Imprime las opciones del menú principal en la consola.
    """
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE TAREAS")
    print("="*40)
    print("1. Registrar nueva tarea")
    print("2. Listar todas las tareas")
    print("3. Buscar tarea")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Ver resumen de estadísticas")
    print("7. Salir y guardar")
    print("="*40)

def iniciar_aplicacion(tareas):
    """
    Maneja el ciclo principal de la aplicación y la navegación del menú.
    """
    continuar = True
    
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")
        if opcion == '1':
            registrar_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            buscar_tarea(tareas)
        elif opcion == '4':
            editar_tarea(tareas)
        elif opcion == '5':
            eliminar_tarea(tareas)
        elif opcion == '6':
            mostrar_resumen(tareas)
        elif opcion == '7':
            print("\nCerrando el sistema...")
            continuar = False
        else:
            print("\n[!] Error: Opción no válida. Por favor, ingrese un número del 1 al 7.")