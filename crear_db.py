import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('inventario.db')
cursor = conexion.cursor()

# Ejecutar las consultas para crear tablas
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL,
    cantidad_en_stock INTEGER NOT NULL,
    stock_minimo INTEGER NOT NULL,
    id_proveedor INTEGER,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id)
);

CREATE TABLE IF NOT EXISTS Proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT,
    telefono TEXT,
    direccion TEXT
);

CREATE TABLE IF NOT EXISTS Movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cantidad INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    motivo TEXT,
    FOREIGN KEY (id_producto) REFERENCES Producto(id)
);

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contraseña TEXT NOT NULL
);                                         
""")

print("Tablas creadas exitosamente.")

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()
