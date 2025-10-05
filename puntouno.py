# funcion para combinar dos listas de tareas ordenadas por prioridad y tiempo
def merge(left, right):
    result = []
    i = j = 0

    # comparar tareas de ambas listas segun prioridad y tiempo
    while i < len(left) and j < len(right):
        if left[i]['prioridad'] > right[j]['prioridad']:
            result.append(left[i])
            i += 1
        elif left[i]['prioridad'] < right[j]['prioridad']:
            result.append(right[j])
            j += 1
        else:
            # si tienen la misma prioridad se ordenan por tiempo menor primero
            if left[i]['tiempo'] < right[j]['tiempo']:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # agregar las tareas restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# funcion principal merge sort con impresion de pasos
def mergeSort(arr, level=0):
    print(f"{'  ' * level}division nivel {level} cantidad de tareas {len(arr)}")

    # caso base si la lista tiene una o ninguna tarea ya esta ordenada
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # ordenar cada mitad
    left = mergeSort(left, level + 1)
    right = mergeSort(right, level + 1)

    # combinar las mitades
    merged = merge(left, right)
    print(f"{'  ' * level}combinacion nivel {level} tareas combinadas {len(merged)}")

    return merged


# lista de tareas de ejemplo
tareas = [
    {'nombre': 'analizar requerimientos', 'prioridad': 8, 'tiempo': 10},
    {'nombre': 'disenar interfaz', 'prioridad': 6, 'tiempo': 6},
    {'nombre': 'revisar codigo', 'prioridad': 7, 'tiempo': 4},
    {'nombre': 'documentar proyecto', 'prioridad': 5, 'tiempo': 3},
    {'nombre': 'probar modulo', 'prioridad': 7, 'tiempo': 8},
    {'nombre': 'entregar informe', 'prioridad': 9, 'tiempo': 2},
    {'nombre': 'actualizar base de datos', 'prioridad': 5, 'tiempo': 1}
]

# mostrar lista original
print("lista original de tareas")
for t in tareas:
    print(t)

# aplicar merge sort
tareasOrdenadas = mergeSort(tareas)

# mostrar lista final ordenada
print("\nlista final de tareas ordenadas por prioridad y tiempo")
for t in tareasOrdenadas:
    print(t)
