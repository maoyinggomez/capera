import csv

# funcion para combinar dos listas de productos ordenadas por calificacion y precio
def merge(left, right):
    result = []
    i = j = 0

    # comparar productos de ambas listas y agregar el que tenga mejor calificacion
    while i < len(left) and j < len(right):
        if left[i]['calificacion'] > right[j]['calificacion']:
            result.append(left[i])
            i += 1
        elif left[i]['calificacion'] < right[j]['calificacion']:
            result.append(right[j])
            j += 1
        else:
            # si la calificacion es igual tomar el que tenga menor precio
            if left[i]['precio'] < right[j]['precio']:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # agregar los productos restantes
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# funcion principal de merge sort con impresion de pasos
def mergeSort(arr, level=0):
    print(f"{'  ' * level}division nivel {level} cantidad de productos {len(arr)}")

    # caso base lista con un producto ya esta ordenada
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
    print(f"{'  ' * level}combinacion nivel {level} productos combinados {len(merged)}")

    return merged


# leer el archivo csv de productos
productos = []
with open('productos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        producto = {
            'id': row['id'],
            'nombre': row['nombre'],
            'precio': float(row['precio']),
            'calificacion': int(row['calificacion']),
            'stock': int(row['stock'])
        }
        productos.append(producto)

print("lista original de productos")
print(f"total de productos: {len(productos)}")

# aplicar merge sort para ordenar los productos
productosOrdenados = mergeSort(productos)

# mostrar los mejores productos
print("\nmejores productos con mayor calificacion y menor precio")
for p in productosOrdenados[:10]:
    print(f"{p['nombre']}  calificacion: {p['calificacion']}  precio: {p['precio']}")
