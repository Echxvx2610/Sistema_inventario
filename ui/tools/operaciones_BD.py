from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pymysql
from pymysql.err import OperationalError
#* libreia mysql retornaba error al importar BD alternativa (pymysql)

def conectar_bd():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        database='sistema_inventario'
    )
    return connection
def crear_base_datos(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_inventario;")
        print("Base de datos creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la base de datos: '{e}'")

def crear_tablas(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("USE sistema_inventario;")
        
        # Tabla proveedores
        tabla_proveedores = """
        CREATE TABLE IF NOT EXISTS proveedores (
            provedor_id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_provedor VARCHAR(100) NOT NULL,
            apellido_provedor VARCHAR(100) NOT NULL,
            direccion VARCHAR(255),
            telefono VARCHAR(15)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_proveedores)
        print("Tabla 'proveedores' creada exitosamente.")

        # Tabla productos
        tabla_productos = """
        CREATE TABLE IF NOT EXISTS productos (
            producto_id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_producto VARCHAR(100) NOT NULL,
            categoria VARCHAR(100),
            precio DECIMAL(10, 2) NOT NULL,
            stock_minimo INT NOT NULL,
            cantidad_en_stock INT NOT NULL,
            provedor_id INT,
            FOREIGN KEY (provedor_id) REFERENCES proveedores(provedor_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_productos)
        print("Tabla 'productos' creada exitosamente.")

        # Tabla usuarios
        tabla_usuarios = """
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario_id INT AUTO_INCREMENT PRIMARY KEY,
            nivel_acceso INT NOT NULL,
            contraseña VARCHAR(255) NOT NULL,
            nombre_usuario VARCHAR(100) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_usuarios)
        print("Tabla 'usuarios' creada exitosamente.")

        # Eliminar las tablas 'entradas_inventario' y 'salidas_inventario'
        cursor.execute("DROP TABLE IF EXISTS entradas_inventario;")
        cursor.execute("DROP TABLE IF EXISTS salidas_inventario;")
        
        # Tabla historial_inventario (simplificada para entradas y salidas)
        tabla_historial = """
        CREATE TABLE IF NOT EXISTS historial_inventario (
            historial_id INT AUTO_INCREMENT PRIMARY KEY,
            producto_id INT NOT NULL,
            cantidad_movimiento INT NOT NULL,
            fecha_movimiento DATETIME NOT NULL,
            usuario_id INT,
            tipo_movimiento ENUM('entrada', 'salida') NOT NULL,
            FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_historial)
        print("Tabla 'historial_inventario' creada exitosamente.")
    
    except Exception as e:
        print(f"Error al crear las tablas: '{e}'")

# Operaciones CRUD de proveedores
def load_data_proveedor(self):
        # Lógica para cargar los datos de la base de datos usando operaciones_BD
        rows = []
        try:
            connection = conectar_bd()
            with connection.cursor() as cursor:
                # Consulta a la base de datos
                cursor.execute("SELECT provedor_id, nombre_provedor, apellido_provedor, direccion, telefono FROM proveedores")
                rows = cursor.fetchall()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar los datos: {str(e)}")
        finally:
            connection.close()

        # Configura la tabla con el número de filas
        self.table_widget.setRowCount(len(rows))
        
        # Insertar datos en la tabla
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Evita que los datos sean editables
                self.table_widget.setItem(row_idx, col_idx, item)

def add_proveedor(nombre, apellido, direccion, telefono):
    connection = conectar_bd()
    with connection.cursor() as cursor:
        sql = "INSERT INTO proveedores (nombre_provedor, apellido_provedor, direccion, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellido, direccion, telefono))
    connection.commit()
    connection.close()

def edit_proveedor(proveedor_id, nombre, apellido, direccion, telefono):
    connection = conectar_bd()
    with connection.cursor() as cursor:
        sql = "UPDATE proveedores SET nombre_provedor=%s, apellido_provedor=%s, direccion=%s, telefono=%s WHERE provedor_id=%s"
        cursor.execute(sql, (nombre, apellido, direccion, telefono, proveedor_id))
    connection.commit()
    connection.close()

def delete_proveedor(proveedor_id):
    connection = conectar_bd()
    with connection.cursor() as cursor:
        sql = "DELETE FROM proveedores WHERE provedor_id=%s"
        cursor.execute(sql, (proveedor_id,))
    connection.commit()
    connection.close()

# Operaciones CRUD de productos
def load_data_productos(self):
    # Conectar a la base de datos con pymysql
    connection = conectar_bd()
    cursor = connection.cursor()
    
    # Consulta a la base de datos
    cursor.execute("SELECT producto_id, nombre_producto, categoria, precio, stock_minimo, cantidad_en_stock, provedor_id FROM productos")
    rows = cursor.fetchall()
    
    # Configurar la tabla con el número de filas
    self.table_widget.setRowCount(len(rows))
    
    # Insertar datos en la tabla
    for row_idx, row_data in enumerate(rows):
        for col_idx, col_data in enumerate(row_data):
            item = QTableWidgetItem(str(col_data))
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Evita que los datos sean editables
            self.table_widget.setItem(row_idx, col_idx, item)
    
    # Configurar las cabeceras de la tabla
    self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Precio", "Stock Mínimo", "Cantidad en Stock", "Proveedor ID"])
    
    # Cerrar la conexión
    cursor.close()
    connection.close()

def load_data_proveedor_combobox():
    # Conectar a la base de datos y obtener la lista de proveedores
    proveedores = []
    connection = conectar_bd()
    cursor = connection.cursor()
    cursor.execute("SELECT provedor_id, nombre_provedor FROM proveedores")  # Ajusta según tu esquema
    proveedores = cursor.fetchall()  # Devuelve una lista de tuplas (provedor_id, nombre)
    connection.close()
    return proveedores

def add_producto(nombre, descripcion, precio, stock):
    connection = conectar_bd()
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        sql = "INSERT INTO productos (nombre_producto, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, descripcion, precio, stock))
    connection.commit()
    connection.close()

def edit_producto(producto_id, nombre_producto, precio, cantidad_en_stock, stock_minimo, provedor_id):
    connection = conectar_bd()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            UPDATE productos
            SET nombre_producto = %s, precio = %s, stock_minimo = %s, cantidad_en_stock = %s, provedor_id = %s
            WHERE producto_id = %s
        """, (nombre_producto, precio, stock_minimo, cantidad_en_stock, provedor_id, producto_id))
        connection.commit()
    except Exception as e:
        print(f"Error al actualizar el producto: {e}")
    finally:
        cursor.close()

def delete_producto(producto_id):
    connection = conectar_bd()
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        sql = "DELETE FROM productos WHERE producto_id=%s"
        cursor.execute(sql, (producto_id,))
    connection.commit()
    connection.close()

# Operaciones CRUD para Analisis de inventario
def load_historial():
    """
    Recupera los datos de la tabla historial_inventario y los devuelve como una lista de tuplas.
    """
    try:
        connection = conectar_bd()
        cursor = connection.cursor()

        # Consulta para recuperar los datos
        query = "SELECT * FROM historial_inventario"
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows  # Devuelve los datos como una lista de tuplas
    finally:
        cursor.close()
        connection.close()


# #Función principal para la creación de la base de datos y las tablas del sistema
# def main():
#     # Establecer la conexión a la base de datos
#     conexion = conectar_bd()
#     if conexion:
#         crear_base_datos(conexion)
#         crear_tablas(conexion)
#         conexion.close()

# if __name__ == "__main__":
#     main()
