import tkinter as tk
from tkinter import messagebox
from gestionar_productos import agregar_producto, agregar_proveedor, registrar_movimiento
from gestionar_productos import obtener_productos, obtener_movimientos, obtener_productos_con_stock_bajo
from gestionar_productos import agregar_usuario, autenticar_usuario



def autenticar_usuario(username, password):
    return username == "admin" and password == "123"

def ventana_login():
    def iniciar_sesion():
        nombre = entry_nombre.get()
        contraseña = entry_contraseña.get()

        if autenticar_usuario(nombre, contraseña):
            print("Inicio de sesión exitoso.")
            ventana.destroy()  # Cierra la ventana de login
            # Aquí puedes abrir la ventana principal de tu sistema
        else:
            label_mensaje.config(text="Nombre de usuario o contraseña incorrectos.")

    ventana = tk.Tk()
    ventana.title("Iniciar Sesión")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Nombre de Usuario").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Contraseña").pack()
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack()

    tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion).pack()
    label_mensaje = tk.Label(ventana, text="")
    label_mensaje.pack()

    ventana.mainloop()

# Para probar la ventana de inicio de sesión
ventana_login()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Inventario")
ventana.geometry("400x400")

# Función para abrir la ventana de agregar producto
def ventana_agregar_producto():
    ventana_producto = tk.Toplevel()
    ventana_producto.title("Agregar Producto")
    ventana_producto.geometry("300x300")

    tk.Label(ventana_producto, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana_producto)
    entry_nombre.pack()

    tk.Label(ventana_producto, text="Descripción").pack()
    entry_descripcion = tk.Entry(ventana_producto)
    entry_descripcion.pack()

    tk.Label(ventana_producto, text="Precio").pack()
    entry_precio = tk.Entry(ventana_producto)
    entry_precio.pack()

    tk.Label(ventana_producto, text="Cantidad en Stock").pack()
    entry_cantidad = tk.Entry(ventana_producto)
    entry_cantidad.pack()

    tk.Label(ventana_producto, text="Stock Mínimo").pack()
    entry_stock_minimo = tk.Entry(ventana_producto)
    entry_stock_minimo.pack()

    def guardar_producto():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        stock_minimo = int(entry_stock_minimo.get())
        
        # Llamar a la función para agregar el producto
        agregar_producto(nombre, descripcion, precio, cantidad, stock_minimo)
        messagebox.showinfo("Producto Agregado", "El producto ha sido agregado exitosamente.")
        ventana_producto.destroy()

    tk.Button(ventana_producto, text="Guardar", command=guardar_producto).pack()

# Función para abrir la ventana de agregar proveedor
def ventana_agregar_proveedor():
    ventana_proveedor = tk.Toplevel()
    ventana_proveedor.title("Agregar Proveedor")
    ventana_proveedor.geometry("300x250")

    tk.Label(ventana_proveedor, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana_proveedor)
    entry_nombre.pack()

    tk.Label(ventana_proveedor, text="Contacto").pack()
    entry_contacto = tk.Entry(ventana_proveedor)
    entry_contacto.pack()

    tk.Label(ventana_proveedor, text="Teléfono").pack()
    entry_telefono = tk.Entry(ventana_proveedor)
    entry_telefono.pack()

    tk.Label(ventana_proveedor, text="Dirección").pack()
    entry_direccion = tk.Entry(ventana_proveedor)
    entry_direccion.pack()

    def guardar_proveedor():
        nombre = entry_nombre.get()
        contacto = entry_contacto.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()

        agregar_proveedor(nombre, contacto, telefono, direccion)
        messagebox.showinfo("Proveedor Agregado", "El proveedor ha sido agregado exitosamente.")
        ventana_proveedor.destroy()

    tk.Button(ventana_proveedor, text="Guardar", command=guardar_proveedor).pack()

# Función para abrir la ventana de registrar movimiento
def ventana_registrar_movimiento():
    ventana_movimiento = tk.Toplevel()
    ventana_movimiento.title("Registrar Movimiento")
    ventana_movimiento.geometry("300x300")

    tk.Label(ventana_movimiento, text="ID del Producto").pack()
    entry_id_producto = tk.Entry(ventana_movimiento)
    entry_id_producto.pack()

    tk.Label(ventana_movimiento, text="Cantidad").pack()
    entry_cantidad = tk.Entry(ventana_movimiento)
    entry_cantidad.pack()

    tk.Label(ventana_movimiento, text="Tipo (ingreso/salida)").pack()
    entry_tipo = tk.Entry(ventana_movimiento)
    entry_tipo.pack()

    tk.Label(ventana_movimiento, text="Motivo").pack()
    entry_motivo = tk.Entry(ventana_movimiento)
    entry_motivo.pack()

    def guardar_movimiento():
        id_producto = int(entry_id_producto.get())
        cantidad = int(entry_cantidad.get())
        tipo = entry_tipo.get().lower()
        motivo = entry_motivo.get()

        registrar_movimiento(id_producto, cantidad, tipo, motivo)
        messagebox.showinfo("Movimiento Registrado", "El movimiento ha sido registrado exitosamente.")
        ventana_movimiento.destroy()

    tk.Button(ventana_movimiento, text="Guardar", command=guardar_movimiento).pack()

# Función para abrir la ventana de reportes
def ventana_reportes():
    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Reportes de Inventario")
    ventana_reporte.geometry("500x400")

    # Reporte de Inventario Actual
    tk.Label(ventana_reporte, text="Inventario Actual").pack()
    productos = obtener_productos()
    print("Productos:", productos)  # Mensaje de depuración
    for producto in productos:
        tk.Label(ventana_reporte, text=f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[4]}").pack()

    # Reporte de Movimientos
    tk.Label(ventana_reporte, text="").pack()  # Espacio en blanco
    tk.Label(ventana_reporte, text="Historial de Movimientos").pack()
    movimientos = obtener_movimientos()
    print("Movimientos:", movimientos)  # Mensaje de depuración
    for movimiento in movimientos:
        tk.Label(ventana_reporte, text=f"ID Producto: {movimiento[1]}, Cantidad: {movimiento[2]}, Tipo: {movimiento[3]}, Fecha: {movimiento[4]}").pack()

    # Reporte de Productos con Bajo Stock
    tk.Label(ventana_reporte, text="").pack()  # Espacio en blanco
    tk.Label(ventana_reporte, text="Productos con Bajo Stock").pack()
    productos_bajo_stock = obtener_productos_con_stock_bajo()
    print("Productos con bajo stock:", productos_bajo_stock)  # Mensaje de depuración
    for producto in productos_bajo_stock:
        tk.Label(ventana_reporte, text=f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[4]}, Stock Mínimo: {producto[5]}").pack()

# Añadir botones en la ventana principal para acceder a cada funcionalidad
tk.Button(ventana, text="Agregar Producto", command=ventana_agregar_producto).pack(pady=10)
tk.Button(ventana, text="Agregar Proveedor", command=ventana_agregar_proveedor).pack(pady=10)
tk.Button(ventana, text="Registrar Movimiento", command=ventana_registrar_movimiento).pack(pady=10)
tk.Button(ventana, text="Ver Reportes", command=ventana_reportes).pack(pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
