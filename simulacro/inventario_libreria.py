#titulo,autor,categoria,precio,cantidad en stock 
#ventas de productos asociando: cliente, producto vendido, cantidad, fecha y descuento(si aplica)
#validar stock disponible y actualizarlo automaticamente
import datetime
inventario = [ 
    {"nombre": "El amanecer", "autor": "Aurelio B", "categoria": "Novela", "precio": 20000, "stock": 10, "vendidos": 0},
    {"nombre": "La verdad", "autor": "Martha G", "categoria": "Ciencia", "precio": 25000, "stock": 40, "vendidos": 0},
    {"nombre": "El ilusionista", "autor": "Luis P","categoria": "Politica", "precio": 47000, "stock": 20, "vendidos": 0},
    {"nombre": "Somos reales", "autor": "Roxana M", "categoria": "Religion", "precio": 68000, "stock": 15, "vendidos": 0},
    {"nombre": "Arte y guerra","autor": "German V", "categoria": "Historia",  "precio": 22000, "stock": 25, "vendidos": 0}
]#inventario con 5 datos creados incialmente

historial_ventas = []
#lista donde ingresaran los datos de las ventas

def input_int(numero_esperado):
    """Con esta funcion se crea un ciclo que verifique que el usuario ingrese un numero entrero hasta que lo logre"""
    while True:
        try:
            valor = int(input(numero_esperado))
            return valor
        except ValueError:
            print("Dato no permitido. Ingresa un número entero.")


def input_float(numero_esperado):
    """Con esta funcion se crea un ciclo que verifique que el usuario ingrese un numero flotante hasta que lo logre"""
    while True:
        try:
            valor = float(input(numero_esperado))
            return valor
        except ValueError:
            print("Dato no permitido. Ingresa un número válido.")

def buscar_producto(nombre):
    """Con esta funcion se espera que se pueda validar si dentro del inventario ya existe un producto con ese nombre, sin importar si el usuario ingresa el nombre con mayusculas o minusculas, todos los nombres son igualados a minuscula"""
    return next((name for name in inventario if name["nombre"].lower() == nombre.lower()), None)


def registrar_producto():
    """Con esta funcion se pretende que se ingrese un nuevo producto al inventario pero que no se repita en caso de existir"""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip() #elimina espacios al inicio o final del string
    if buscar_producto(nombre):        #funcion para determinar si el nombre ingresado ya existe en el inventario
        print("El producto ya existe, si desea actualizar ir a la opcion actualizar producto.")
        return
    #si el nombre del libro ya existe, avisa para pasar a actualizarlo

    autor = input("Autor: ").strip()
    categoria = input("Categoría: ").strip()
    precio = input_float("Precio unitario: ")
    if precio <= 0:
        print("El precio debe ser positivo.")
        return
    #verifica que los datos ingresados sean correctos para poder continuar, debe ingresar un valor por encima de 0

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo, porque estas agregando un producto.")
        return
    #verifica que el valor ingresado sea un entero mayor a 0 para poder continuar

    producto = {
        "nombre": nombre,
        "autor" : autor,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "vendidos": 0
    }
    #los datos ingresados previamente son guardados en este diccionario

    inventario.append(producto)
    print(" Producto registrado!")
    #agrega el diccionario creado a el inventario general 

def ver_inventario():
    """permite visualizar que se encuentra en el inventario"""
    print("\n--- INVENTARIO ACTUAL---")
    if not inventario:
        print("El inventario está vacío.")
        return
    #si no existen datos en el inventario, retorna. 
    for book in inventario:
        print(f"Nombre: {book['nombre']} | Autor: {book['autor']} | Categoría: {book['categoria']} | "
              f"Precio: ${book['precio']} | Stock: {book['stock']} ")
    #ciclo creado para iterar sobre cada valor del inventario e imprimir el inventario completo


def actualizar_producto():
    """funcion creada para modificar valores en el inventario sobre libros existentes"""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    nombre = input("Ingresa el nombre del producto: ")
    producto = buscar_producto(nombre) #valida que el libro si se encuentre en el inventario

    if not producto:
        print("Producto no encontrado.")
        return  #retorna si no se encuentra el libro en el inventario

    print("Deja el campo en blanco si deseas mantener el mismo precio en el libro.")

    nuevo_precio = input("Nuevo precio: ")
    if nuevo_precio.strip():
        producto["precio"] = input_float("Ingresa un numero o confirme el valor: ")
       #permite validar que el nuevo precio sea correcto

    nuevo_stock = input("Nuevo stock: ")
    if nuevo_stock.strip():
        producto["stock"] = input_int("Ingresa un numero entero o confirme el valor: ")
        #permite validar que el stock sea un numero
    print(" Producto actualizado!")


def eliminar_producto():
    """Funcion que permite validar si el producto existe para eliminarlo """
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(nombre)#permite validar si el producto se encuentra en el inventario

    if not producto:
        print("Producto no encontrado.")
        return #si el producto no existe, avisa y luego retorna al paso anterior

    inventario.remove(producto) # metodo para eliminar el producto del inventario 
    print(" Producto eliminado satisfactoriamente!.")


def registrar_venta():
    """Funcion creada para ingresar la venta realizada"""
    print("\n--- REGISTRAR VENTA ---")
    cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (Regular / Especial): ")

    nombre_producto = input("Producto vendido: ")
    producto = buscar_producto(nombre_producto)#permite validar si el producto se encuentra en el inventario

    if not producto:
        print("Producto no encontrado.")
        return #si no se encuentra el producto retorna al paso anterior

    cantidad = input_int("Cantidad vendida: ")  #permite validar que el dato sea un numero entero

    if cantidad > producto["stock"]:
        print(f"No hay suficiente stock. Disponible: {producto['stock']}")
        return #permite mostrar si la venta supera el stock disponible y retorna al paso anterior

    descuento = input_float("Descuento aplicado (%): ") #valida que el dato ingresado sea un numero flotante

    producto["stock"] -= cantidad #permite restar al stock la cantidad vendida
    producto["vendidos"] += cantidad #añade la cantidad del prodcuto vendido a el inventario en la clave "vendidos"

    precio_total = cantidad * producto["precio"] #calcula el valor total de la venta
    precio_final = precio_total - (precio_total * descuento / 100) # resta el porcentaje de descuento para mostrar el valor final

    venta = {
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

    historial_ventas.append(venta) #añade el diccionario a la lista de historial de ventas
    print("Venta registrada exitosamente!")


def ver_historial_ventas():
    """Funcion que permite mostrar la historico de las ventas hasta el momento """
    print("\n--- HISTORIAL DE VENTAS ---")
    if not historial_ventas:
        print("No se han registrado ventas.")
        return #retorna en caso de que la lista de historial de ventas se encuentre vacia

    for venta in historial_ventas:
        print(f"{venta['fecha']} | {venta['cliente']} | {venta['producto']} | Cantidad: {venta['cantidad']} | "
              f"Bruto: ${venta['bruto']:.2f} | Neto: ${venta['neto']:.2f} | Descuento: {venta['descuento']}% " ) #".2f permite que el valor tenga maximo 2 decimales"
    #ciclo que va a iterar en la lista de historial de ventas para imprimir cada una de los valores de la lista


def reporte_top_productos():
    """Permite clasificar los 3 productos mas vendidos"""
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")
    productos_ordenados = sorted(inventario, key=lambda p: p["vendidos"], reverse=True)
    for p in productos_ordenados[:3]:
        print(f"{p['nombre']} - Vendidos: {p['vendidos']}")
    #sorted permite ordenar la lista, por defecto lo hace de menor a mayor, pero utilizando reverse=True, permite organizarla de mayor a menor

def reporte_ventas_por_autor():
    """Permite clasificar las ventas por autor"""
    print("\n--- VENTAS POR Autor ---")

    totales_autor = {} #variable que acogera los datos y resultados 
    for venta in historial_ventas: 
        producto = buscar_producto(venta["producto"])
        autor = producto["autor"]
        totales_autor[autor] = totales_autor.get(autor, 0) + venta["neto"] + venta['cantidad']

    for autor, total in totales_autor.items():
        print(f"{autor}: ${total:.2f}")


def reporte_ingresos():
    """Permite visualizar los acumulados en ventas"""
    print("\n--- REPORTE DE INGRESOS ---")
    if historial_ventas==[]:  # permite validar si la lista de historico de ventas se encuentra vacia
        print("Aun no se registran ventas")
    bruto = sum(venta["bruto"] for venta in historial_ventas)#suma el valor encontrado en cada iteracion en clave"bruto" en lista historial de ventas
    neto = sum(venta["neto"] for venta in historial_ventas)#suma el valor encontrado en cada iteracion en clave"neto" en lista historial de ventas
    print(f"Ingreso bruto: ${bruto:.2f}") #permite imprimir valor con maximo 2 decimales
    print(f"Ingreso neto: ${neto:.2f}")
    


def reporte_rendimiento_inventario():
    print("\n--- RENDIMIENTO DEL INVENTARIO ---")
    for p in inventario:
        porcentaje_vendido = (p["vendidos"] / (p["vendidos"] + p["stock"])
                              if p["vendidos"] + p["stock"] > 0 else 0)
        print(f"{p['nombre']}: {porcentaje_vendido*100:.1f}% vendido")



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