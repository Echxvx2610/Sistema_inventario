# views.py
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from .operaciones_BD import *

class InicioView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Inicio")
        label.setFont(QFont("Arial", 24))
        label.setStyleSheet("color: white;")
        saludo = QLabel("Bienvenido, Echxvx2610")
        saludo.setFont(QFont("Arial", 16))
        saludo.setStyleSheet("color: white;")
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(saludo, alignment=Qt.AlignCenter)


class ProveedorView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear la barra de herramientas ( agregar iconos para agregar, editar, eliminar )
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")
        
        # Botón para agregar proveedor
        add_button = QPushButton("Agregar")
        add_button.setStyleSheet("color: white; background-color: #4caf50; border: none; padding: 8px;")
        add_button.clicked.connect(self.agregar_proveedor)
        toolbar.addWidget(add_button)
        
        # Botón para editar proveedor
        edit_button = QPushButton("Editar")
        edit_button.setStyleSheet("color: white; background-color: #ffa726; border: none; padding: 8px;")
        edit_button.clicked.connect(self.editar_proveedor)
        toolbar.addWidget(edit_button)
        
        # Botón para eliminar proveedor
        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet("color: white; background-color: #f44336; border: none; padding: 8px;")
        delete_button.clicked.connect(self.eliminar_proveedor)
        toolbar.addWidget(delete_button)

        layout.addWidget(toolbar)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Dirección", "Teléfono"])

        # Ajustar el tamaño de las columnas automáticamente
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que las columnas se estiren

        # Ajustar el tamaño de las filas
        self.table_widget.setRowHeight(0, 30)  # Tamaño mínimo de la fila
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 30)  # Ajustar todas las filas

        # Cambiar el tamaño de la fuente
        font = QFont()
        font.setPointSize(12)  # Cambiar el tamaño de la fuente
        self.table_widget.setFont(font)

        layout.addWidget(self.table_widget)

        # Cargar los datos de la base de datos
        load_data_proveedor(self)
        
        
    def agregar_proveedor(self):
        # cambiar inputdialog por un dialogo completo como editar
        dialog = QInputDialog(self) 
        nombre, ok1 = dialog.getText(self, "Agregar Proveedor", "Nombre:")
        apellido, ok2 = dialog.getText(self, "Agregar Proveedor", "Apellido:")
        direccion, ok3 = dialog.getText(self, "Agregar Proveedor", "Dirección:")
        telefono, ok4 = dialog.getText(self, "Agregar Proveedor", "Teléfono:")

        if ok1 and ok2 and ok3 and ok4:
            try:
                add_proveedor(nombre, apellido, direccion, telefono)
                load_data_proveedor(self)  # Recargar la tabla después de agregar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar el proveedor: {str(e)}")
                print("Error al agregar el proveedor:", str(e))
                
    def editar_proveedor(self):
        #cambiar inputdialog por un dialogo completo como editar_producto
        selected_index = self.table_widget.currentRow()
        if selected_index == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor para editar")
            return
        
        proveedor_id = self.table_widget.item(selected_index, 0).text()
        nombre = self.table_widget.item(selected_index, 1).text()
        apellido = self.table_widget.item(selected_index, 2).text()
        direccion = self.table_widget.item(selected_index, 3).text()
        telefono = self.table_widget.item(selected_index, 4).text()

        dialog = QInputDialog(self)
        new_nombre, ok1 = dialog.getText(self, "Editar Proveedor", "Nombre:", text=nombre)
        new_apellido, ok2 = dialog.getText(self, "Editar Proveedor", "Apellido:", text=apellido)
        new_direccion, ok3 = dialog.getText(self, "Editar Proveedor", "Dirección:", text=direccion)
        new_telefono, ok4 = dialog.getText(self, "Editar Proveedor", "Teléfono:", text=telefono)

        if ok1 and ok2 and ok3 and ok4:
            try:
                edit_proveedor(proveedor_id, new_nombre, new_apellido, new_direccion, new_telefono)
                load_data_proveedor(self)  # Recargar la tabla después de editar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo editar el proveedor: {str(e)}")
                print("Error al editar el proveedor:", str(e))

    def eliminar_proveedor(self):
        selected_index = self.table_widget.currentRow()
        if selected_index == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor para eliminar")
            return
        
        proveedor_id = self.table_widget.item(selected_index, 0).text()
        try:
            delete_proveedor(proveedor_id)
            load_data_proveedor(self)  # Recargar la tabla después de eliminar
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el proveedor: {str(e)}")
            print("Error al eliminar el proveedor:", str(e))

class ProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear la barra de herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")
        
        # Botón para agregar producto
        add_button = QPushButton("Agregar")
        add_button.setStyleSheet("color: white; background-color: #4caf50; border: none; padding: 8px;")
        add_button.clicked.connect(self.agregar_producto)
        toolbar.addWidget(add_button)
        
        # Botón para editar producto
        edit_button = QPushButton("Editar")
        edit_button.setStyleSheet("color: white; background-color: #ffa726; border: none; padding: 8px;")
        edit_button.clicked.connect(self.editar_producto)
        toolbar.addWidget(edit_button)
        
        # Botón para eliminar producto
        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet("color: white; background-color: #f44336; border: none; padding: 8px;")
        delete_button.clicked.connect(self.eliminar_producto)
        toolbar.addWidget(delete_button)

        layout.addWidget(toolbar)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Precio", "Cantidad en Stock"])
        # Ajustar el tamaño de las columnas automáticamente
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que las columnas se estiren

        # Ajustar el tamaño de las filas
        self.table_widget.setRowHeight(0, 30)  # Tamaño mínimo de la fila
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 30)  # Ajustar todas las filas

        # Cambiar el tamaño de la fuente
        font = QFont()
        font.setPointSize(12)  # Cambiar el tamaño de la fuente
        self.table_widget.setFont(font)

        layout.addWidget(self.table_widget)

        # Cargar los datos de la base de datos
        load_data_productos(self)

    def agregar_producto(self):
        #cambiar inputdialog por un dialogo completo como editar_producto
        nombre = "Nuevo Producto"
        categoria = "Nueva Categoría"  # Añadir un campo para la categoría
        precio = 100.0
        stock_minimo = 10
        cantidad_en_stock = 0  
        add_producto(nombre, categoria, precio, stock_minimo, cantidad_en_stock)
        load_data_productos(self)  # Recargar datos

    def editar_producto(self):
        # Agregar edicion de categoria!
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            # Obtener el ID del producto actual
            producto_id = self.table_widget.item(current_row, 0).text()
            nombre_actual = self.table_widget.item(current_row, 1).text()
            precio_actual = self.table_widget.item(current_row, 3).text()
            stock_actual = self.table_widget.item(current_row, 4).text()
            
            # Obtener stock mínimo actual desde la tabla
            stock_minimo_actual = self.table_widget.item(current_row, 5).text()  # Asumiendo que stock_minimo está en la columna 2

            # Crear un diálogo para editar el producto
            dialog = QDialog(self)
            dialog.setWindowTitle("Editar Producto")

            layout = QVBoxLayout(dialog)

            # Campos para editar
            nombre_input = QLineEdit(dialog)
            nombre_input.setText(nombre_actual)
            layout.addWidget(QLabel("Nombre:"))
            layout.addWidget(nombre_input)

            precio_input = QDoubleSpinBox(dialog)
            precio_input.setValue(float(precio_actual))
            layout.addWidget(QLabel("Precio:"))
            layout.addWidget(precio_input)

            stock_input = QSpinBox(dialog)
            stock_input.setValue(int(stock_actual))
            layout.addWidget(QLabel("Cantidad en Stock:"))
            layout.addWidget(stock_input)

            # Agregar input para stock mínimo
            stock_minimo_input = QSpinBox(dialog)  # Nuevo campo para stock mínimo
            stock_minimo_input.setValue(int(stock_minimo_actual))  # Configurar valor inicial
            layout.addWidget(QLabel("Stock Mínimo:"))  # Etiqueta para stock mínimo
            layout.addWidget(stock_minimo_input)  # Añadir al layout

            # ComboBox para seleccionar un nuevo proveedor
            proveedor_combo = QComboBox(dialog)
            proveedores = load_data_proveedor_combobox()  # Ahora debería devolver una lista de tuplas (provedor_id, nombre)

            # Asegúramos el retorno de la lista de proovedores
            if proveedores:
                # Agregar nombres al ComboBox
                for provedor_id, nombre in proveedores:
                    proveedor_combo.addItem(nombre, provedor_id)  # Agregar el nombre y el ID como dato

            layout.addWidget(QLabel("Seleccionar Proveedor:"))
            layout.addWidget(proveedor_combo)

            # Botón para confirmar la edición
            save_button = QPushButton("Guardar", dialog)
            save_button.clicked.connect(lambda: self.guardar_edicion(
                dialog,
                producto_id,
                nombre_input.text(),                   # nombre_producto
                precio_input.value(),                  # precio
                stock_input.value(),                   # cantidad_en_stock
                stock_minimo_input.value(),            # stock_minimo
                proveedor_combo.currentData()           # proveedor_id
            ))
            layout.addWidget(save_button)

            dialog.setLayout(layout)
            dialog.exec_()

    def guardar_edicion(self, dialog, producto_id, nombre_producto, precio, stock_minimo, cantidad_en_stock, provedor_id):
        edit_producto(producto_id, nombre_producto, precio, cantidad_en_stock, stock_minimo, provedor_id)  # Actualizar con el nuevo proveedor
        load_data_productos(self)  # Recargar datos de productos
        dialog.accept()

    def eliminar_producto(self):
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            producto_id = self.table_widget.item(current_row, 0).text()
            delete_producto(producto_id)
            load_data_productos(self)  # Recargar datos


class AnalisisView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Análisis")
        label.setFont(QFont("Arial", 24))
        label.setStyleSheet("color: white;")
        layout.addWidget(label, alignment=Qt.AlignCenter)
