CREATE TABLE Producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL,
    cantidad_en_stock INTEGER NOT NULL,
    stock_minimo INTEGER NOT NULL,
    id_proveedor INTEGER,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id)
);

CREATE TABLE Proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT,
    telefono TEXT,
    direccion TEXT
);

CREATE TABLE Movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cantidad INTEGER NOT NULL,
    tipo TEXT NOT NULL, -- 'ingreso' o 'salida'
    motivo TEXT,
    FOREIGN KEY (id_producto) REFERENCES Producto(id)
);
