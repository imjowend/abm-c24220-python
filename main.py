# https://github.com/imjowend/abm-c24220-python

def mostrar_menu():
    print("\n Menú de Inventario\n")
    print("1. Agregá un producto")
    print("2. Mostrá el inventario")
    print("3. Actualizá un producto del inventario")
    print("4. Eliminá un producto del inventario")
    print("5. Salir")
    return input("\nSelecciona una opción: ")

def agregar_producto(inventario):
    # Valido que el nombre no tenga mas de 50 caracteres
    while True:
        nombre = input("Ingresá el nombre del producto (máximo 50 caracteres): ")
        if len(nombre) > 50:
            print("El nombre del producto no debe exceder los 50 caracteres. Intentalo nuevamente.")
        else:
            break

    # Valido que el input de Cantidad que me ingresen sea un digito y no un caracter o signo
    while True:
        cantidad = input("Ingresá la cantidad: ")
        if not cantidad.isdigit():
            print("La cantidad debe ser un número entero positivo. Intentalo nuevamente.")
        else:
            cantidad = int(cantidad)
            break

    inventario.append({'nombre': nombre, 'cantidad': cantidad})
    print(f"\n¡Producto '{nombre}' agregado con éxito!")

def actualizar_producto(inventario):
    # Primero valido si existe
    # Lo haremos mediante nombre
    nombre = input("Ingresá el nombre del producto a actualizar (máximo 50 caracteres): ")

    # Valido que el input de Cantidad que me ingresen sea un digito y no un caracter o signo
    while True:
        cantidad = input("Ingresá la nueva cantidad: ")
        if not cantidad.isdigit():
            print("La cantidad debe ser un número entero positivo. Intentalo nuevamente.")
        else:
            cantidad = int(cantidad)
            break

    for item in inventario:
        if nombre == item['nombre']:
            item['cantidad'] = cantidad

    print(f"\n¡Producto '{nombre}' actualizado con éxito!")

def eliminar_producto(inventario):
    # Lo haremos mediante nombre
    nombre = input("Ingresá el nombre del producto a eliminar (máximo 50 caracteres): ")
    for item in inventario:
        if item['nombre'] == nombre:
            inventario.remove(item)
    print(f"\n¡Producto '{nombre}' eliminado con éxito!")

def mostrar_inventario(inventario):
    if inventario:
        print("\n Inventario de Productos")
        for producto in inventario:
            print(f"\nProducto: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nEl inventario está vacío.")

def main():
    inventario = []
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            actualizar_producto(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intentá de nuevo.")

if __name__ == "__main__":
    main()
