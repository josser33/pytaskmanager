import datetime
from modules.validaciones import validar_no_vacio, validar_opcion_prioridad, buscar_por_id, validar_fecha

def registrar_tarea(tareas):
    """
    Solicita datos al usuario y añade una nueva tarea a la lista.
    """
    print("\n--- REGISTRAR NUEVA TAREA ---")
    
    nuevo_id = 1 if not tareas else tareas[-1]['id'] + 1
    
    titulo = validar_no_vacio("Título de la tarea: ")
    descripcion = validar_no_vacio("Descripción: ")
    prioridad = validar_opcion_prioridad()
    fecha_limite = validar_fecha("Fecha límite (DD/MM/AAAA): ")
    
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Pendiente",
        "fecha_creacion": str(datetime.date.today()),
        "fecha_limite": fecha_limite
    }
    
    tareas.append(nueva_tarea)
    print(f"\n[!] Tarea '{titulo}' registrada con éxito (ID: {nuevo_id}).")

def listar_tareas(tareas):
    """
    Muestra todas las tareas registradas en un formato legible.
    """
    print("\n--- LISTADO DE TAREAS ---")
    
    if not tareas:
        print("No hay tareas registradas actualmente.")
        return

    
    print(f"{'ID':<4} | {'Título':<15} | {'Prioridad':<10} | {'Estado':<12}")
    print("-" * 50)
    
    for t in tareas:
        print(f"{t['id']:<4} | {t['titulo']:<15} | {t['prioridad']:<10} | {t['estado']:<12}")

def buscar_tarea(tareas):
    print("\n--- BUSCAR TAREA ---")
    if not tareas:
        print("No hay tareas para buscar.")
        return

    tarea, _ = buscar_por_id(tareas)
    if tarea:
        print("\nInformación encontrada:")
        for clave, valor in tarea.items():
            print(f"{clave.capitalize()}: {valor}")

def eliminar_tarea(tareas):
    print("\n--- ELIMINAR TAREA ---")
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    tarea, id_encontrado = buscar_por_id(tareas, "Ingrese el ID de la tarea a eliminar: ")
    if tarea:
        confirmar = input(f"¿Seguro que desea eliminar la tarea '{tarea['titulo']}'? (s/n): ").lower()
        if confirmar == 's':
            for i in range(len(tareas)):
                if tareas[i]['id'] == id_encontrado:
                    tareas.pop(i)
                    print("[!] Tarea eliminada exitosamente.")
                    break
        else:
            print("Operación cancelada.")

def editar_tarea(tareas):
    """
    Permite modificar los datos de una tarea existente.
    """
    print("\n--- EDITAR TAREA ---")
    if not tareas:
        print("No hay tareas para editar.")
        return

    tarea, _ = buscar_por_id(tareas, "Ingrese el ID de la tarea que desea editar: ")
    
    if tarea:
        print(f"\nEditando la tarea: {tarea['titulo']}")
        print("Deje en blanco si no desea modificar el campo.")
        
        nuevo_titulo = input(f"Nuevo título [{tarea['titulo']}]: ").strip()
        if nuevo_titulo:
            tarea['titulo'] = nuevo_titulo
            
        nueva_desc = input(f"Nueva descripción [{tarea['descripcion']}]: ").strip()
        if nueva_desc:
            tarea['descripcion'] = nueva_desc
            
        print(f"Prioridad actual: {tarea['prioridad']}")
        cambiar_prio = input("¿Desea cambiar la prioridad? (s/n): ").lower()
        if cambiar_prio == 's':
            tarea['prioridad'] = validar_opcion_prioridad()
            
        print(f"Estado actual: {tarea['estado']}")
        cambiar_estado = input("¿Marcar como Completada? (s/n): ").lower()
        if cambiar_estado == 's':
            tarea['estado'] = "Completada"
            
        print("\n[!] Tarea actualizada con éxito.")