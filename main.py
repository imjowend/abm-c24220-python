# https://github.com/imjowend/abm-c24220-python
import sqlite3
from colorama import init, Fore, Style

# Esto lo uso para iniciar los colores
init(autoreset=True)

# Función principal para el menú
def mostrar_menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print(Fore.CYAN + "\n=== Menú Principal ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")

        opcion = input("Seleccioná una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print(Fore.MAGENTA + "Hasta luego. Feliz año nuevo")
            break
        else:
            print(Fore.RED + "Opción no válida. Intentá de nuevo.")

# Conexión y creación de la base de datos SQLite
def inicializar_base_datos():
    """Crea la base de datos y la tabla de productos si no existen."""
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para registrar un producto
def agregar_producto():
    """Permite agregar un nuevo producto al inventario."""

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
    descripcion = input("Ingresá una descripción del producto: ")
    precio = float(input("Ingresá el precio del producto: "))
    categoria = input("Ingresá la categoría del producto: ")

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto registrado con éxito.")


def mostrar_productos():
    """Muestra todos los productos registrados en el inventario."""
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print(Fore.YELLOW + "\nInventario de Productos:")
        print(Style.BRIGHT + f"{'ID':<5}{'Nombre':<20}{'Descripción':<30}{'Cantidad':<10}{'Precio':<10}{'Categoría':<15}")
        for producto in productos:
            print(f"{producto[0]:<5}{producto[1]:<20}{producto[2]:<30}{producto[3]:<10}{producto[4]:<10.2f}{producto[5]:<15}")
    else:
        print(Fore.RED + "No hay productos en el inventario.")


def actualizar_producto():
    """Permite actualizar la cantidad de un producto específico."""
    id_producto = int(input("Ingresá el ID del producto a actualizar: "))
    nueva_cantidad = int(input("Ingresá la nueva cantidad disponible: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE productos SET cantidad = ? WHERE id = ?
    ''', (nueva_cantidad, id_producto))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Cantidad actualizada con éxito.")


def eliminar_producto():
    """Permite eliminar un producto del inventario."""
    id_producto = int(input("Ingresá el ID del producto a eliminar: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        DELETE FROM productos WHERE id = ?
    ''', (id_producto,))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto eliminado con éxito.")


def buscar_producto():
    """Permite buscar un producto por su ID."""
    id_producto = int(input("Ingrese el ID del producto a buscar: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT * FROM productos WHERE id = ?
    ''', (id_producto,))
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        print(Fore.YELLOW + "\nProducto encontrado:")
        print(Style.BRIGHT + f"{'ID':<5}{'Nombre':<20}{'Descripción':<30}{'Cantidad':<10}{'Precio':<10}{'Categoría':<15}")
        print(f"{producto[0]:<5}{producto[1]:<20}{producto[2]:<30}{producto[3]:<10}{producto[4]:<10.2f}{producto[5]:<15}")
    else:
        print(Fore.RED + "No se encontró un producto con ese ID.")

# Función para generar un reporte de bajo stock
def reporte_bajo_stock():
    """Genera un reporte de productos con bajo stock."""
    limite = int(input("Ingrese el límite para considerar bajo stock: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT * FROM productos WHERE cantidad <= ?
    ''', (limite,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print(Fore.YELLOW + "\nReporte de los productos con bajo stock:")
        print(Style.BRIGHT + f"{'ID':<5}{'Nombre':<20}{'Descripción':<30}{'Cantidad':<10}{'Precio':<10}{'Categoría':<15}")
        for producto in productos:
            print(f"{producto[0]:<5}{producto[1]:<20}{producto[2]:<30}{producto[3]:<10}{producto[4]:<10.2f}{producto[5]:<15}")
    else:
        print(Fore.RED + "No hay productos con bajo stock.")


if __name__ == "__main__":
    inicializar_base_datos()
    mostrar_menu()
