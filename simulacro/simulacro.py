import datetime

inventario = [
    {"nombre": "Laptop A", "marca": "Dell", "categoria": "Computadoras", "precio": 850, "stock": 10, "garantia": 12, "vendidos": 0},
    {"nombre": "Mouse X", "marca": "Logitech", "categoria": "Accesorios", "precio": 25, "stock": 40, "garantia": 6, "vendidos": 0},
    {"nombre": "Teclado Z", "marca": "Razer", "categoria": "Accesorios", "precio": 120, "stock": 20, "garantia": 12, "vendidos": 0},
    {"nombre": "Monitor 24", "marca": "Samsung", "categoria": "Pantallas", "precio": 200, "stock": 15, "garantia": 24, "vendidos": 0},
    {"nombre": "Smartphone S", "marca": "Xiaomi", "categoria": "Celulares", "precio": 350, "stock": 25, "garantia": 12, "vendidos": 0}
]

historial_ventas = []


def input_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def input_float(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

def buscar_producto(nombre):
    return next((p for p in inventario if p["nombre"].lower() == nombre.lower()), None)


def registrar_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip()
    if buscar_producto(nombre):
        print("El producto ya existe.")
        return

    marca = input("Marca: ").strip()
    categoria = input("Categoría: ").strip()
    precio = input_float("Precio unitario: ")
    if precio <= 0:
        print("El precio debe ser positivo.")
        return

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo.")
        return

    garantia = input_int("Garantía (en meses): ")

    producto = {
        "nombre": nombre,
        "marca": marca,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "garantia": garantia,
        "vendidos": 0
    }

    inventario.append(producto)
    print("✔ Producto registrado exitosamente!")


def ver_inventario():
    print("\n--- LISTADO DE INVENTARIO ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    for p in inventario:
        print(f"{p['nombre']} | Marca: {p['marca']} | Categoría: {p['categoria']} | "
              f"Precio: ${p['precio']} | Stock: {p['stock']} | Garantía: {p['garantia']} meses")


def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    nombre = input("Ingresa el nombre del producto: ")
    producto = buscar_producto(nombre)

    if not producto:
        print("Producto no encontrado.")
        return

    print("Deja el campo en blanco para mantener el valor actual.")

    nuevo_precio = input("Nuevo precio: ")
    if nuevo_precio.strip():
        producto["precio"] = float(nuevo_precio)

    nuevo_stock = input("Nuevo stock: ")
    if nuevo_stock.strip():
        producto["stock"] = int(nuevo_stock)

    nueva_garantia = input("Nueva garantía (en meses): ")
    if nueva_garantia.strip():
        producto["garantia"] = int(nueva_garantia)

    print("✔ Producto actualizado!")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(nombre)

    if not producto:
        print("Producto no encontrado.")
        return

    inventario.remove(producto)
    print("✔ Producto eliminado.")


def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")
    cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (Regular / VIP): ")

    nombre_producto = input("Producto vendido: ")
    producto = buscar_producto(nombre_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    cantidad = input_int("Cantidad vendida: ")

    if cantidad > producto["stock"]:
        print(f"No hay suficiente stock. Disponible: {producto['stock']}")
        return

    descuento = input_float("Descuento aplicado (%): ")

    producto["stock"] -= cantidad
    producto["vendidos"] += cantidad

    precio_total = cantidad * producto["precio"]
    precio_final = precio_total - (precio_total * descuento / 100)

    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "fecha": datetime.date.today().isoformat(),
        "descuento": descuento,
        "bruto": precio_total,
        "neto": precio_final
    }

    historial_ventas.append(venta)
    print("✔ Venta registrada exitosamente!")


def ver_historial_ventas():
    print("\n--- HISTORIAL DE VENTAS ---")
    if not historial_ventas:
        print("No se han registrado ventas.")
        return

    for v in historial_ventas:
        print(f"{v['fecha']} | {v['cliente']} | {v['producto']} | Cantidad: {v['cantidad']} | "
              f"Bruto: ${v['bruto']:.2f} | Neto: ${v['neto']:.2f}")



def reporte_top_productos():
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")
    productos_ordenados = sorted(inventario, key=lambda p: p["vendidos"], reverse=True)
    for p in productos_ordenados[:3]:
        print(f"{p['nombre']} - Vendidos: {p['vendidos']}")


def reporte_ventas_por_marca():
    print("\n--- VENTAS POR MARCA ---")

    totales_marca = {}
    for venta in historial_ventas:
        producto = buscar_producto(venta["producto"])
        marca = producto["marca"]
        totales_marca[marca] = totales_marca.get(marca, 0) + venta["neto"]

    for marca, total in totales_marca.items():
        print(f"{marca}: ${total:.2f}")


def reporte_ingresos():
    print("\n--- REPORTE DE INGRESOS ---")
    bruto = sum(v["bruto"] for v in historial_ventas)
    neto = sum(v["neto"] for v in historial_ventas)
    print(f"Ingreso bruto: ${bruto:.2f}")
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
            print("¡Hasta luego!")
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
        print("2. Ventas por Marca")
        print("3. Reporte de Ingresos")
        print("4. Rendimiento del Inventario")
        print("5. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            reporte_top_productos()
        elif opcion == "2":
            reporte_ventas_por_marca()
        elif opcion == "3":
            reporte_ingresos()
        elif opcion == "4":
            reporte_rendimiento_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


menu_principal()