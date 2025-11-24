#titulo,autor,categoria,precio,cantidad en stock 
#ventas de productos asociando: cliente, producto vendido, cantidad, fecha y descuento(si aplica)
#validar stock disponible y actualizarlo automaticamente
import datetime
inventary = [ ###########################
    {"nombre": "El amanecer", "autor": "Aurelio B", "categoria": "Novela", "precio": 20000, "stock": 10, "vendidos": 0},
    {"nombre": "La verdad", "autor": "Martha G", "categoria": "Ciencia", "precio": 25000, "stock": 40, "vendidos": 0},
    {"nombre": "El ilusionista", "autor": "Luis P","categoria": "Politica", "precio": 47000, "stock": 20, "vendidos": 0},
    {"nombre": "Somos reales", "autor": "Roxana M", "categoria": "Religion", "precio": 68000, "stock": 15, "vendidos": 0},
    {"nombre": "Arte y guerra","autor": "German V", "categoria": "Historia",  "precio": 22000, "stock": 25, "vendidos": 0}
]#inventario con 5 datos creados incialmente

sales_history = []
#lista donde ingresaran los datos de las ventas

def input_int(expected_num):
    """Con esta funcion se crea un ciclo que verifique que el usuario ingrese un numero entrero hasta que lo logre"""
    while True:
        try:
            value = int(input(expected_num))
            return value
        except ValueError:
            print("Dato no permitido. Ingresa un número entero.")


def input_float(expected_num):
    """Con esta funcion se crea un ciclo que verifique que el usuario ingrese un numero flotante hasta que lo logre"""
    while True:
        try:
            value = float(input(expected_num))
            return value
        except ValueError:
            print("Dato no permitido. Ingresa un número válido.")

def search_product(name):
    """Con esta funcion se espera que se pueda validar si dentro del inventario ya existe un producto con ese nombre, sin importar si el usuario ingresa el nombre con mayusculas o minusculas, todos los nombres son igualados a minuscula"""
    return next((name for name in inventary if name["nombre"].lower() == nombre.lower()), None)


def register_product():
    """Con esta funcion se pretende que se ingrese un nuevo producto al inventario pero que no se repita en caso de existir"""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    name = input("Nombre del producto: ").strip() #elimina espacios al inicio o final del string
    if search_product(name):        #funcion para determinar si el nombre ingresado ya existe en el inventario
        print("El producto ya existe, si desea actualizar ir a la opcion actualizar producto.")
        return
    #si el nombre del libro ya existe, avisa para pasar a actualizarlo

    author = input("Autor: ").strip()
    category = input("Categoría: ").strip()
    price = input_float("Precio unitario: ")
    if price <= 0:
        print("El precio debe ser positivo.")
        return
    #verifica que los datos ingresados sean correctos para poder continuar, debe ingresar un valor por encima de 0

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo, porque estas agregando un producto.")
        return
    #verifica que el valor ingresado sea un entero mayor a 0 para poder continuar

    product = {
        "nombre": nombre,
        "autor" : autor,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "vendidos": 0
    }
    #los datos ingresados previamente son guardados en este diccionario

    inventary.append(product)
    print(" Producto registrado!")
    #agrega el diccionario creado a el inventario general 

def see_inventary():
    """permite visualizar que se encuentra en el inventario"""
    print("\n--- INVENTARIO ACTUAL---")
    if not inventary:
        print("El inventario está vacío.")
        return
    #si no existen datos en el inventario, retorna. 
    for book in inventario:
        print(f"Nombre: {book['nombre']} | Autor: {book['autor']} | Categoría: {book['categoria']} | "
              f"Precio: ${book['precio']} | Stock: {book['stock']} ")
    #ciclo creado para iterar sobre cada valor del inventario e imprimir el inventario completo


def update_product():
    """funcion creada para modificar valores en el inventario sobre libros existentes"""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    name = input("Ingresa el nombre del producto: ")
    product = search_producto(name) #valida que el libro si se encuentre en el inventario

    if not product:
        print("Producto no encontrado.")
        return  #retorna si no se encuentra el libro en el inventario

    print("Deja el campo en blanco si deseas mantener el mismo precio en el libro.")

    new_price = input("Nuevo precio: ")
    if new_price.strip():
        product["precio"] = input_float("Ingresa un numero o confirme el valor: ")
       #permite validar que el nuevo precio sea correcto

    new_stock = input("Nuevo stock: ")
    if new_stock.strip():
        product["stock"] = input_int("Ingresa un numero entero o confirme el valor: ")
        #permite validar que el stock sea un numero
    print(" Producto actualizado!")


def delete_product():
    """Funcion que permite validar si el producto existe para eliminarlo """
    print("\n--- ELIMINAR PRODUCTO ---")
    name = input("Nombre del producto: ")
    product = search_product(name)#permite validar si el producto se encuentra en el inventario

    if not product:
        print("Producto no encontrado.")
        return #si el producto no existe, avisa y luego retorna al paso anterior

    inventary.remove(product) # metodo para eliminar el producto del inventario 
    print(" Producto eliminado satisfactoriamente!.")


def register_sale():
    """Funcion creada para ingresar la venta realizada"""
    print("\n--- REGISTRAR VENTA ---")
    client = input("Nombre del cliente: ")
    type_client = input("Tipo de cliente (Regular / Especial): ")

    product_name = input("Producto vendido: ")
    product = search_product_(product_name)#permite validar si el producto se encuentra en el inventario

    if not product:
        print("Producto no encontrado.")
        return #si no se encuentra el producto retorna al paso anterior

    quantity = input_int("Cantidad vendida: ")  #permite validar que el dato sea un numero entero

    if quantity > product["stock"]:
        print(f"No hay suficiente stock. Disponible: {product['stock']}")
        return #permite mostrar si la venta supera el stock disponible y retorna al paso anterior

    discount = input_float("Descuento aplicado (%): ") #valida que el dato ingresado sea un numero flotante

    product["stock"] -= quantity #permite restar al stock la cantidad vendida
    product["vendidos"] += quantity #añade la cantidad del prodcuto vendido a el inventario en la clave "vendidos"

    total_price = quantity * product["precio"] #calcula el valor total de la venta
    final_price = total_price - (total_price * discount / 100) # resta el porcentaje de descuento para mostrar el valor final

    sales = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "fecha": datetime.date.today().isoformat(), #importado de la biblioteca para mostrar la fecha de la venta
        "descuento": descuento,
        "bruto": precio_total,
        "neto": precio_final
    }
    #diccionario que recibe los datos de la venta

    sales_history.append(sales) #añade el diccionario a la lista de historial de ventas
    print("Venta registrada exitosamente!")


def see_sales_history():
    """Funcion que permite mostrar la historico de las ventas hasta el momento """
    print("\n--- HISTORIAL DE VENTAS ---")
    if not sales_history:
        print("No se han registrado ventas.")
        return #retorna en caso de que la lista de historial de ventas se encuentre vacia

    for sale in sales_history:
        print(f"{sale['fecha']} | {sale['cliente']} | {sale['producto']} | Cantidad: {sale['cantidad']} | "
              f"Bruto: ${sale['bruto']:.2f} | Neto: ${sale['neto']:.2f} | Descuento: {sale['descuento']}% " ) #".2f permite que el valor tenga maximo 2 decimales"
    #ciclo que va a iterar en la lista de historial de ventas para imprimir cada una de los valores de la lista


def top_products():
    """Permite clasificar los 3 productos mas vendidos"""
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")
    organize_products = sorted(inventary, key=lambda top: top["vendidos"], reverse=True)
    for top in organize_products[:3]:
        print(f"{top['nombre']} - Vendidos: {top['vendidos']}")
    #sorted permite ordenar la lista, por defecto lo hace de menor a mayor, pero utilizando reverse=True, permite organizarla de mayor a menor

def sales_by_author():
    """Permite clasificar las ventas por autor"""
    print("\n--- VENTAS POR Autor ---")

    full_author = {} #variable que acogera los datos y resultados 
    for venta in sales_history: 
        product = search_product(sales["producto"])
        author = producto["author"]
        full_author[author] = full_author.get(author, 0) + sales["neto"] + sales['cantidad']

    for author, total in full_author.items():
        print(f"{author}: ${total:.2f}")


def sales_report():
    """Permite visualizar los acumulados en ventas"""
    print("\n--- REPORTE DE INGRESOS ---")
    if sales_history==[]:  # permite validar si la lista de historico de ventas se encuentra vacia
        print("Aun no se registran ventas")
    bruto = sum(sales["bruto"] for sales in sales_history)#suma el valor encontrado en cada iteracion en clave"bruto" en lista historial de ventas
    neto = sum(sales["neto"] for sales in sales_history)#suma el valor encontrado en cada iteracion en clave"neto" en lista historial de ventas
    print(f"Ingreso bruto: ${bruto:.2f}") #permite imprimir valor con maximo 2 decimales
    print(f"Ingreso neto: ${neto:.2f}")
    


def inventary_performance():
    print("\n--- RENDIMIENTO DEL INVENTARIO ---")
    for p in inventario:
        percentage_sold= (p["vendidos"] / (p["vendidos"] + p["stock"])
                              if p["vendidos"] + p["stock"] > 0 else 0)
        print(f"{p['nombre']}: {percentage_sold*100:.1f}% vendido")



def main_menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Gestionar Inventario")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Reportes")
        print("5. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            menu_inventary()
        elif option== "2":
            register_sale()
        elif option == "3":
            see_sales_history()
        elif option == "4":
            reports_menu()
        elif option == "5":
            print("¡Fue un gusto servirte!")
            break
        else:
            print("Opción no válida.")


def menu_inventary():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Registrar Producto")
        print("2. Ver Inventario")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver")
        option = input("Elige una opción: ")

        if option == "1":
            register_product()
        elif option == "2":
            see_inventary()
        elif option == "3":
            update_product()
        elif option == "4":
            delete_product()
        elif option == "5":
            break
        else:
            print("Opción no válida.")


def reports_menu():
    while True:
        print("\n--- MENÚ DE REPORTES ---")
        print("1. Top 3 Productos Más Vendidos")
        print("2. Ventas por Autor")
        print("3. Reporte de Ingresos")
        print("4. Volver")

        option = input("Elige una opción: ")

        if option == "1":
            top_products()
        elif option== "2":
            sales_by_author()
        elif option == "3":
            sales_report()
        elif option == "4":
            break
        else:
            print("Opción no válida.")


main_menu()