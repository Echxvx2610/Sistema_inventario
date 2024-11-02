
import pymysql
from pymysql.err import OperationalError
#* libreia mysql retornaba error al importar BD alternativa (pymysql)


def establecer_conexion(host_name, user_name, user_password, puerto=3306):
    conexion = None
    try:
        conexion = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            port=puerto,
            charset='utf8'
        )
        print("........Conexión exitosa........")
    except OperationalError as e:
        print(f"Error: '{e}'")
    return conexion

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

        # Tabla entradas_inventario
        tabla_entradas = """
        CREATE TABLE IF NOT EXISTS entradas_inventario (
            entrada_id INT AUTO_INCREMENT PRIMARY KEY,
            cantidad_entrada INT NOT NULL,
            fecha_entrada DATETIME NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_entradas)
        print("Tabla 'entradas_inventario' creada exitosamente.")

        # Tabla salidas_inventario
        tabla_salidas = """
        CREATE TABLE IF NOT EXISTS salidas_inventario (
            salida_id INT AUTO_INCREMENT PRIMARY KEY,
            cantidad_salida INT NOT NULL,
            fecha_salida DATETIME NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_salidas)
        print("Tabla 'salidas_inventario' creada exitosamente.")

        # Tabla historial_inventario
        tabla_historial = """
        CREATE TABLE IF NOT EXISTS historial_inventario (
            cantidad_historial INT NOT NULL,
            fecha_historial DATETIME NOT NULL,
            usuario_id INT,
            tipo_movimiento ENUM('entrada', 'salida') NOT NULL,
            PRIMARY KEY (fecha_historial, usuario_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
        """
        cursor.execute(tabla_historial)
        print("Tabla 'historial_inventario' creada exitosamente.")
    
    except Exception as e:
        print(f"Error al crear las tablas: '{e}'")

def main():
    host_name = "localhost"
    user_name = "root"
    user_password = "admin"

    # Establecer la conexión a la base de datos
    conexion = establecer_conexion(host_name, user_name, user_password)
    if conexion:
        crear_base_datos(conexion)
        crear_tablas(conexion)
        conexion.close()

if __name__ == "__main__":
    main()
