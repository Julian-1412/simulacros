import datetime
inventario = [ 
    {"nombre": "El amanecer", "autor": "Aurelio B", "categoria": "Novela", "precio": 20000, "stock": 10, "vendidos": 0},
    {"nombre": "La verdad", "autor": "Martha G", "categoria": "Ciencia", "precio": 25000, "stock": 40, "vendidos": 0},
    {"nombre": "El ilusionista", "autor": "Luis P","categoria": "Politica", "precio": 47000, "stock": 20, "vendidos": 0},
    {"nombre": "Somos reales", "autor": "Roxana M", "categoria": "Religion", "precio": 68000, "stock": 15, "vendidos": 0},
    {"nombre": "Arte y guerra","autor": "German V", "categoria": "Historia",  "precio": 22000, "stock": 25, "vendidos": 0}
]#inventory with 5 items initially created

historial_ventas = []
#list where sales data will be entered

def input_int(numero_esperado):
    """This function creates a loop that verifies that the user enters an integer until they succeed."""
    while True:
        try:
            valor = int(input(numero_esperado))
            return valor
        except ValueError:
            print("Dato no permitido. Ingresa un número entero.")


def input_float(numero_esperado):
    """This function creates a loop that verifies that the user enters a floating point number until they succeed."""
    while True:
        try:
            valor = float(input(numero_esperado))
            return valor
        except ValueError:
            print("Dato no permitido. Ingresa un número válido.")

def buscar_producto(nombre):
    """This function is expected to validate whether a product with that name already exists in the inventory, regardless of whether the user enters the name in uppercase or lowercase letters. All names are converted to lowercase letters."""
    return next((name for name in inventario if name["nombre"].lower() == nombre.lower()), None)


def registrar_producto():
    """This function is intended to add a new product to the inventory but not to repeat it if it already exists."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip() #removes spaces at the beginning or end of the string
    if buscar_producto(nombre):        #function to determine whether the name entered already exists in the inventory
        print("El producto ya existe, si desea actualizar ir a la opcion actualizar producto.")
        return
    #If the book name already exists, notify us so we can update it.

    autor = input("Autor: ").strip()
    categoria = input("Categoría: ").strip()
    precio = input_float("Precio unitario: ")
    if precio <= 0:
        print("El precio debe ser positivo.")
        return
    #Verify that the data entered is correct in order to continue. You must enter a value greater than 0.

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo, porque estas agregando un producto.")
        return
    #Verify that the value entered is an integer greater than 0 in order to continue.

    producto = {
        "nombre": nombre,
        "autor" : autor,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "vendidos": 0
    }
    #Previously entered data is stored in this dictionary.

    inventario.append(producto)
    print(" Producto registrado!")
    #add the created dictionary to the general inventory 

def ver_inventario():
    """allows you to see what is in the inventory"""
    print("\n--- INVENTARIO ACTUAL---")
    if not inventario:
        print("El inventario está vacío.")
        return
    #if there is no data in the inventory, return. 
    for book in inventario:
        print(f"Nombre: {book['nombre']} | Autor: {book['autor']} | Categoría: {book['categoria']} | "
              f"Precio: ${book['precio']} | Stock: {book['stock']} ")
    #cycle created to iterate over each value in the inventory and print the complete inventory

def actualizar_producto():
    """function created to modify values in the inventory of existing books"""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    nombre = input("Ingresa el nombre del producto: ")
    producto = buscar_producto(nombre) #validate that the book is in the inventory

    if not producto:
        print("Producto no encontrado.")
        return  #returns if the book is not found in the inventory

    print("Deja el campo en blanco si deseas mantener el mismo precio en el libro.")

    nuevo_precio = input("Nuevo precio: ")
    if nuevo_precio.strip():
        producto["precio"] = input_float("Ingresa un numero o confirme el valor: ")
       #allows you to validate that the new price is correct

    nuevo_stock = input("Nuevo stock: ")
    if nuevo_stock.strip():
        producto["stock"] = input_int("Ingresa un numero entero o confirme el valor: ")
        #allows you to validate that the stock is a number
    print(" Producto actualizado!")


def eliminar_producto():
    """Function that allows you to validate if the product exists in order to delete it. """
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(nombre)#allows you to validate if the product is in stock

    if not producto:
        print("Producto no encontrado.")
        return #if the product does not exist, notify and then return to the previous step

    inventario.remove(producto) # method for removing the product from inventory 
    print(" Producto eliminado satisfactoriamente!.")


def registrar_venta():
    """Function created to enter the sale made"""
    print("\n--- REGISTRAR VENTA ---")
    cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (Regular / Especial): ")

    nombre_producto = input("Producto vendido: ")
    producto = buscar_producto(nombre_producto)#allows you to validate whether the product is in stock

    if not producto:
        print("Producto no encontrado.")
        return #If the product is not found, return to the previous

    cantidad = input_int("Cantidad vendida: ")  #allows you to validate that the data is an integer

    if cantidad > producto["stock"]:
        print(f"No hay suficiente stock. Disponible: {producto['stock']}")
        return #allows you to show if the sale exceeds available stock and returns to the previous step

    descuento = input_float("Descuento aplicado (%): ") #validate that the entered data is a floating point number

    producto["stock"] -= cantidad #allows you to rest the quantity sold from stock
    producto["vendidos"] += cantidad #Add the quantity of the product sold to the inventory under the key “sold.”

    precio_total = cantidad * producto["precio"] #Calculate the total value of the sale.
    precio_final = precio_total - (precio_total * descuento / 100) # discount percentage is subtracted to show the final value

    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "fecha": datetime.date.today().isoformat(), #imported from the library to display the date of sale
        "descuento": descuento,
        "bruto": precio_total,
        "neto": precio_final
    }
    #dictionary that receives sales data

    historial_ventas.append(venta) #add the dictionary to the sales history list
    print("Venta registrada exitosamente!")


def ver_historial_ventas():
    """Function that allows you to view sales history to date. """
    print("\n--- HISTORIAL DE VENTAS ---")
    if not historial_ventas:
        print("No se han registrado ventas.")
        return #returns if the sales history list is empty

    for venta in historial_ventas:
        print(f"{venta['fecha']} | {venta['cliente']} | {venta['producto']} | Cantidad: {venta['cantidad']} | "
              f"Bruto: ${venta['bruto']:.2f} | Neto: ${venta['neto']:.2f} | Descuento: {venta['descuento']}% " ) #“.2f allows the value to have a maximum of 2 decimal places”
     #cycle that will iterate through the sales history list to print each of the values in the list


def reporte_top_productos():
    """Allows you to rank the top 3 best-selling products"""
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")
    productos_ordenados = sorted(inventario, key=lambda p: p["vendidos"], reverse=True)
    for p in productos_ordenados[:3]:
        print(f"{p['nombre']} - Vendidos: {p['vendidos']}")
    #sorted allows you to order the list. By default, it orders from smallest to largest, but using reverse=True allows you to order from largest to smallest.

def reporte_ventas_por_autor():
    """Allows you to classify sales by author"""
    print("\n--- VENTAS POR Autor ---")

    totales_autor = {} #variable that will hold the data and results 
    for venta in historial_ventas: 
        producto = buscar_producto(venta["producto"])
        autor = producto["autor"]
        totales_autor[autor] = totales_autor.get(autor, 0) + venta["neto"] + venta['cantidad']

    for autor, total in totales_autor.items():
        print(f"{autor}: ${total:.2f}")


def reporte_ingresos():
    """Allows you to view accumulated sales figures."""
    print("\n--- REPORTE DE INGRESOS ---")
    if historial_ventas==[]:  # allows you to validate if the sales history list is empty
        print("Aun no se registran ventas")
    bruto = sum(venta["bruto"] for venta in historial_ventas)#Add the value found in each iteration in “bruto” key to the sales history list.
    neto = sum(venta["neto"] for venta in historial_ventas)#add the value found in each iteration to the “neto” key in the sales history list
    print(f"Ingreso bruto: ${bruto:.2f}") #allows printing values with a maximum of 2 decimal places
    print(f"Ingreso neto: ${neto:.2f}")
    


def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Gestionar Inventario")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Reportes")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            ver_historial_ventas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            print("¡Fue un gusto servirte!")
            break
        else:
            print("Opción no válida.")


def menu_inventario():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Registrar Producto")
        print("2. Ver Inventario")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def menu_reportes():
    while True:
        print("\n--- MENÚ DE REPORTES ---")
        print("1. Top 3 Productos Más Vendidos")
        print("2. Ventas por Autor")
        print("3. Reporte de Ingresos")
        print("4. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            reporte_top_productos()
        elif opcion == "2":
            reporte_ventas_por_autor()
        elif opcion == "3":
            reporte_ingresos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


menu_principal()