from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QMessageBox
import logging
import pymysql
from pymysql.err import OperationalError
#* libreia mysql retornaba error al importar BD alternativa (pymysql)

# Configurar el registro
logging.basicConfig(filename="app.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def mostrar_error(mensaje):
    """Mostrar un cuadro de mensaje en caso de error."""
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText("Ha ocurrido un error.")
    msg_box.setInformativeText(mensaje)
    msg_box.exec_()

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
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            sql = "INSERT INTO proveedores (nombre_provedor, apellido_provedor, direccion, telefono) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apellido, direccion, telefono))
        connection.commit()
        connection.close()
    except Exception as e:
        error_message = f"Error al agregar proveedor: {str(e)}"
        logging.error(error_message)
        mostrar_error(error_message)

def edit_proveedor(proveedor_id, nombre, apellido, direccion, telefono):
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            sql = "UPDATE proveedores SET nombre_provedor=%s, apellido_provedor=%s, direccion=%s, telefono=%s WHERE provedor_id=%s"
            cursor.execute(sql, (nombre, apellido, direccion, telefono, proveedor_id))
        connection.commit()
        connection.close()
    except Exception as e:
        error_message = f"Error al editar proveedor con ID {proveedor_id}: {str(e)}"
        logging.error(error_message)
        mostrar_error(error_message)

def delete_proveedor(proveedor_id):
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            sql = "DELETE FROM proveedores WHERE provedor_id=%s"
            cursor.execute(sql, (proveedor_id,))
        connection.commit()
        connection.close()
    except Exception as e:
        error_message = f"Error al eliminar proveedor con ID {proveedor_id}: {str(e)}"
        logging.error(error_message)
        mostrar_error(error_message)

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

def add_producto(nombre_producto, categoria, precio, stock_minimo, cantidad_en_stock, provedor_id=None):
    """Agregar un producto a la base de datos."""
    try:
        connection = conectar_bd()
        cursor = connection.cursor()

        query = """
        INSERT INTO productos (nombre_producto, categoria, precio, stock_minimo, cantidad_en_stock, provedor_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (nombre_producto, categoria, precio, stock_minimo, cantidad_en_stock, provedor_id)

        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        logging.error(f"Error al agregar producto: {e}")
        mostrar_error("No se pudo agregar el producto. Verifique los datos e intente nuevamente.")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def edit_producto(producto_id, nombre_producto, precio, cantidad_en_stock, stock_minimo, provedor_id):
    """Editar un producto en la base de datos."""
    try:
        connection = conectar_bd()
        cursor = connection.cursor()

        query = """
        UPDATE productos
        SET nombre_producto = %s, precio = %s, stock_minimo = %s, cantidad_en_stock = %s, provedor_id = %s
        WHERE producto_id = %s
        """
        values = (nombre_producto, precio, stock_minimo, cantidad_en_stock, provedor_id, producto_id)

        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        logging.error(f"Error al actualizar producto: {e}")
        mostrar_error("No se pudo actualizar el producto. Por favor, intente nuevamente.")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def delete_producto(producto_id):
    """Eliminar un producto de la base de datos, incluso si tiene un proveedor asignado."""
    try:
        connection = conectar_bd()
        cursor = connection.cursor()

        # Consulta para desactivar temporalmente las verificaciones de clave foránea
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        # Consulta para eliminar el producto
        query = "DELETE FROM productos WHERE producto_id = %s"
        cursor.execute(query, (producto_id,))

        # Reactivar las verificaciones de clave foránea
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        connection.commit()
        print(f"Producto con ID {producto_id} eliminado exitosamente.")
    except Exception as e:
        logging.error(f"Error al eliminar producto: {e}")
        mostrar_error("No se pudo eliminar el producto. Intente nuevamente.")
    finally:
        if cursor:
            cursor.close()
        if connection:
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

def load_productos():
    """
    Recupera los datos de la tabla 'productos' y los devuelve como una lista de tuplas.
    """
    try:
        # Conectar a la base de datos
        connection = conectar_bd()  # Asegúrate de que esta función esté disponible en tu proyecto
        cursor = connection.cursor()

        # Consulta a la base de datos
        query = """
        SELECT producto_id, nombre_producto, categoria, precio, stock_minimo, cantidad_en_stock, provedor_id
        FROM productos
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows  # Devuelve los datos como una lista de tuplas
    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()


# Operaciones Usuarios
def registrar_usuario(nombre_usuario, correo, contraseña, nivel_acceso=1):
    """
    Registrar un nuevo usuario en la base de datos.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = """
                INSERT INTO usuarios (nombre_usuario, correo, contraseña, nivel_acceso)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre_usuario, correo, contraseña, nivel_acceso))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        logging.error(f"Error al registrar usuario: {e}")
        mostrar_error("No se pudo registrar el usuario. Verifica la información.")
        return False

def validar_usuario(nombre_usuario, contraseña):
    """
    Validar el usuario y contraseña en la base de datos.
    """
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = """
                SELECT nivel_acceso FROM usuarios 
                WHERE nombre_usuario = %s AND contraseña = %s
            """
            cursor.execute(query, (nombre_usuario, contraseña))
            resultado = cursor.fetchone()
        connection.close()
        return resultado  # Retorna el nivel de acceso si las credenciales son válidas, None si no lo son
    except Exception as e:
        logging.error(f"Error al validar usuario: {e}")
        mostrar_error("Hubo un problema al validar las credenciales.")
        return None

# quitar comentarios y ejecutar para crear BD y tablas
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
