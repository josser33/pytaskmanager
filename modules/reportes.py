def mostrar_resumen(tareas):
    """
    Muestra estadísticas básicas sobre las tareas.
    """
    print("\n--- RESUMEN DE GESTIÓN ---")
    total = len(tareas)
    completadas = 0
    
    for t in tareas:
        if t['estado'] == "Completada":
            completadas += 1
            
    pendientes = total - completadas
    
    print(f"Total de tareas: {total}")
    print(f"Tareas completadas: {completadas}")
    print(f"Tareas pendientes: {pendientes}")
    
    if total > 0:
        porcentaje = (completadas / total) * 100
        print(f"Progreso actual: {porcentaje:.2f}%")