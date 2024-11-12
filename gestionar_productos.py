import sqlite3

def agregar_producto(nombre, descripcion, precio, cantidad, stock_minimo, id_proveedor=None):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    consulta = """
    INSERT INTO Producto (nombre, descripcion, precio, cantidad_en_stock, stock_minimo, id_proveedor)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(consulta, (nombre, descripcion, precio, cantidad, stock_minimo, id_proveedor))

    conexion.commit()
    conexion.close()
    print("Producto agregado exitosamente.")



def agregar_proveedor(nombre, contacto, telefono, direccion):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    consulta = """
    INSERT INTO Proveedor (nombre, contacto, telefono, direccion)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(consulta, (nombre, contacto, telefono, direccion))

    conexion.commit()
    conexion.close()
    print("Proveedor agregado exitosamente.")



def registrar_movimiento(id_producto, cantidad, tipo, motivo):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    consulta = """
    INSERT INTO Movimiento (id_producto, cantidad, tipo, motivo)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(consulta, (id_producto, cantidad, tipo, motivo))

    # Actualizar la cantidad en stock del producto
    if tipo == "ingreso":
        cursor.execute("UPDATE Producto SET cantidad_en_stock = cantidad_en_stock + ? WHERE id = ?", (cantidad, id_producto))
    elif tipo == "salida":
        cursor.execute("UPDATE Producto SET cantidad_en_stock = cantidad_en_stock - ? WHERE id = ?", (cantidad, id_producto))

    conexion.commit()
    conexion.close()
    print("Movimiento registrado exitosamente.")



def obtener_productos():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Producto")  # Cambiar a 'Producto'
    productos = cursor.fetchall()
    conn.close()
    return productos

def obtener_movimientos():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Movimiento")  # Cambiar a 'Movimiento'
    movimientos = cursor.fetchall()
    conn.close()
    return movimientos

def obtener_productos_con_stock_bajo():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Producto WHERE cantidad_en_stock < stock_minimo")  # Cambiar a 'Producto' y 'cantidad_en_stock'
    productos_bajo_stock = cursor.fetchall()
    conn.close()
    return productos_bajo_stock


#Usuario  para ingresas
def agregar_usuario(nombre, contraseña):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    consulta = """
    INSERT INTO Usuarios (nombre, contraseña)
    VALUES (?, ?)
    """
    cursor.execute(consulta, (nombre, contraseña))
    conexion.commit()
    conexion.close()
    print("Usuario agregado exitosamente.")

def autenticar_usuario(nombre, contraseña):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    consulta = """
    SELECT * FROM Usuarios WHERE nombre = ? AND contraseña = ?
    """
    cursor.execute(consulta, (nombre, contraseña))
    usuario = cursor.fetchone()
    conexion.close()

    return usuario is not None  # Devuelve True si el usuario existe
