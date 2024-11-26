# views.py
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from .operaciones_BD import *
import matplotlib.pyplot as plt
import numpy as np

class InicioView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Vista de Inicio")
        label.setFont(QFont("Arial", 24))
        label.setStyleSheet("color: white;")
        saludo = QLabel("Bienvenido, Echxvx2610")
        saludo.setFont(QFont("Arial", 16))
        saludo.setStyleSheet("color: white;")
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(saludo, alignment=Qt.AlignCenter)

        # Crear un layout en cuadrícula para las tablas (2x2)
        grid_layout = QGridLayout()

        # Añadir tablas a la cuadrícula (2x2)
        grid_layout.addWidget(self.create_inventory_movements_table(), 0, 0)  # Fila 0, Columna 0
        grid_layout.addWidget(self.create_products_with_low_stock_table(), 0, 1)  # Fila 0, Columna 1
        grid_layout.addWidget(self.create_most_sold_products_table(), 1, 0)   # Fila 1, Columna 0
        grid_layout.addWidget(self.create_least_sold_products_table(), 1, 1)   # Fila 1, Columna 1
        
        # Añadir la cuadrícula de tablas al layout principal
        layout.addLayout(grid_layout)

    def create_inventory_movements_table(self):
        """Crear tabla de Últimos Movimientos de Inventario"""
        table = QTableWidget()
        table.setRowCount(5)  # Número de filas de ejemplo
        table.setColumnCount(3)  # Tres columnas: Fecha, Producto, Movimiento
        
        # Establecer los encabezados de las columnas
        table.setHorizontalHeaderLabels(['Fecha', 'Producto', 'Movimiento'])

        # Insertar datos de ejemplo
        data = [
            ['2024-11-10', 'Producto A', 'Entrada'],
            ['2024-11-09', 'Producto B', 'Salida'],
            ['2024-11-08', 'Producto C', 'Entrada'],
            ['2024-11-07', 'Producto D', 'Salida'],
            ['2024-11-06', 'Producto E', 'Entrada']
        ]
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(item))

        # Configuración de la tabla
        table.setStyleSheet("QTableWidget { background-color: #2f3136; color: white; border: 1px solid #72767d; }"
                            "QHeaderView::section { background-color: #36393f; }")
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)  # Ajuste automático de tamaño
        
        # Ajustar las columnas para que se estiren
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que todas las columnas se estiren
        
        # Usar un QScrollArea para permitir el desplazamiento si la tabla es muy grande
        scroll_area = QScrollArea()
        scroll_area.setWidget(table)
        scroll_area.setWidgetResizable(True)  # Permite que la tabla se redimensione con el área de desplazamiento
        return scroll_area

    def create_products_with_low_stock_table(self):
        """Crear tabla de Productos con Stock Mínimo"""
        table = QTableWidget()
        table.setRowCount(5)  # Número de filas de ejemplo
        table.setColumnCount(3)  # Tres columnas: Producto, Stock Actual, Stock Mínimo
        
        # Establecer los encabezados de las columnas
        table.setHorizontalHeaderLabels(['Producto', 'Stock Actual', 'Stock Mínimo'])

        # Insertar datos de ejemplo
        data = [
            ['Producto A', '10', '5'],
            ['Producto B', '3', '5'],
            ['Producto C', '8', '6'],
            ['Producto D', '4', '3'],
            ['Producto E', '2', '5']
        ]
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(item))

        # Configuración de la tabla
        table.setStyleSheet("QTableWidget { background-color: #2f3136; color: white; border: 1px solid #72767d; }"
                            "QHeaderView::section { background-color: #36393f; }")
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        
        # Ajustar las columnas para que se estiren
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que todas las columnas se estiren

        # Usar un QScrollArea para permitir el desplazamiento si la tabla es muy grande
        scroll_area = QScrollArea()
        scroll_area.setWidget(table)
        scroll_area.setWidgetResizable(True)  # Permite que la tabla se redimensione con el área de desplazamiento
        return scroll_area

    def create_most_sold_products_table(self):
        """Crear tabla de Productos Más Vendidos"""
        table = QTableWidget()
        table.setRowCount(5)  # Número de filas de ejemplo
        table.setColumnCount(3)  # Tres columnas: Producto, Unidades Vendidas, Ingresos
        
        # Establecer los encabezados de las columnas
        table.setHorizontalHeaderLabels(['Producto', 'Unidades Vendidas', 'Ingresos'])

        # Insertar datos de ejemplo
        data = [
            ['Producto A', '500', '$5000'],
            ['Producto B', '400', '$4000'],
            ['Producto C', '300', '$3000'],
            ['Producto D', '200', '$2000'],
            ['Producto E', '100', '$1000']
        ]
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(item))

        # Configuración de la tabla
        table.setStyleSheet("QTableWidget { background-color: #2f3136; color: white; border: 1px solid #72767d; }"
                            "QHeaderView::section { background-color: #36393f; }")
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        
        # Ajustar las columnas para que se estiren
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que todas las columnas se estiren

        # Usar un QScrollArea para permitir el desplazamiento si la tabla es muy grande
        scroll_area = QScrollArea()
        scroll_area.setWidget(table)
        scroll_area.setWidgetResizable(True)  # Permite que la tabla se redimensione con el área de desplazamiento
        return scroll_area

    def create_least_sold_products_table(self):
        """Crear tabla de Productos Menos Vendidos"""
        table = QTableWidget()
        table.setRowCount(5)  # Número de filas de ejemplo
        table.setColumnCount(3)  # Tres columnas: Producto, Unidades Vendidas, Ingresos
        
        # Establecer los encabezados de las columnas
        table.setHorizontalHeaderLabels(['Producto', 'Unidades Vendidas', 'Ingresos'])

        # Insertar datos de ejemplo
        data = [
            ['Producto E', '50', '$500'],
            ['Producto D', '60', '$600'],
            ['Producto C', '70', '$700'],
            ['Producto B', '80', '$800'],
            ['Producto A', '90', '$900']
        ]
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(item))

        # Configuración de la tabla
        table.setStyleSheet("QTableWidget { background-color: #2f3136; color: white; border: 1px solid #72767d; }"
                            "QHeaderView::section { background-color: #36393f; }")
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        
        # Ajustar las columnas para que se estiren
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que todas las columnas se estiren

        # Usar un QScrollArea para permitir el desplazamiento si la tabla es muy grande
        scroll_area = QScrollArea()
        scroll_area.setWidget(table)
        scroll_area.setWidgetResizable(True)  # Permite que la tabla se redimensione con el área de desplazamiento
        return scroll_area

class ProveedorView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear la barra de herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")

        # Acción para agregar proveedor
        add_action = QAction(QIcon(r"ui\resources\img\agregar_usuario.png"), "Agregar", self)
        add_action.triggered.connect(self.agregar_proveedor)
        toolbar.setIconSize(QSize(45,45))
        toolbar.addAction(add_action)

        # Acción para editar proveedor
        edit_action = QAction(QIcon(r"ui\resources\img\editar_usuario.png"), "Editar", self)
        edit_action.triggered.connect(self.editar_proveedor)
        toolbar.addAction(edit_action)

        # Acción para eliminar proveedor
        delete_action = QAction(QIcon(r"ui\resources\img\eliminar_usuario.png"), "Eliminar", self)
        delete_action.triggered.connect(self.eliminar_proveedor)
        toolbar.addAction(delete_action)

        # Agregar la barra de herramientas al diseño
        layout.addWidget(toolbar)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Dirección", "Teléfono"])
        # Eliminar index de la tabla
        self.table_widget.verticalHeader().hide()
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

        # Acción para agregar proveedor
        add_action = QAction(QIcon(r"ui\resources\img\agregar_producto.png"), "Agregar", self)
        add_action.triggered.connect(self.agregar_producto)
        toolbar.setIconSize(QSize(45,45))
        toolbar.addAction(add_action)

        # Acción para editar proveedor
        edit_action = QAction(QIcon(r"ui\resources\img\editar_producto.png"), "Editar", self)
        edit_action.triggered.connect(self.editar_producto)
        toolbar.addAction(edit_action)

        # Acción para eliminar proveedor
        delete_action = QAction(QIcon(r"ui\resources\img\eliminar_producto.png"), "Eliminar", self)
        delete_action.triggered.connect(self.eliminar_producto)
        toolbar.addAction(delete_action)

        # Agregar la barra de herramientas al diseño
        layout.addWidget(toolbar)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Precio", "Cantidad en Stock"])
        # Eliminar index de las filas
        self.table_widget.verticalHeader().hide()
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

# Vista para el historial
class AnalisisView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configurar el diseño principal
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear la barra de herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")

        # Acción para generar gráfico
        generate_chart_action = QAction(QIcon(r"ui\resources\img\generar_grafico.png"), "Generar Gráfico", self)
        generate_chart_action.triggered.connect(self.generar_grafico)
        toolbar.setIconSize(QSize(45, 45))
        toolbar.addAction(generate_chart_action)

        # Acción para exportar CSV
        export_csv_action = QAction(QIcon(r"ui\resources\img\exportar_csv.png"), "Exportar CSV", self)
        export_csv_action.triggered.connect(self.exportar_csv)
        toolbar.addAction(export_csv_action)

        # Acción para exportar PDF
        export_pdf_action = QAction(QIcon(r"ui\resources\img\exportar_pdf.png"), "Exportar PDF", self)
        export_pdf_action.triggered.connect(self.exportar_pdf)
        toolbar.addAction(export_pdf_action)

        # Agregar la barra de herramientas al diseño
        layout.addWidget(toolbar)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)  # Número de columnas de la tabla historial_inventario
        self.table_widget.setHorizontalHeaderLabels([
            "ID", "Producto ID", "Cantidad Movimiento", "Fecha Movimiento", "Usuario ID", "Tipo Movimiento"
        ])
        # Ocultar index de la tabla
        self.table_widget.verticalHeader().hide()

        # Ajustar el tamaño de las columnas automáticamente
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que las columnas se estiren

        # Ajustar el tamaño de las filas
        self.table_widget.setRowHeight(0, 30)
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 30)

        # Cambiar el tamaño de la fuente
        font = QFont()
        font.setPointSize(12)
        self.table_widget.setFont(font)

        # Agregar la tabla al diseño
        layout.addWidget(self.table_widget)

        # Cargar los datos desde la base de datos
        self.cargar_datos()

    def cargar_datos(self):
        """
        Carga los datos de la tabla historial_inventario en el QTableWidget.
        """
        rows = load_historial()  # Llama a la función para obtener los datos desde la BD
        self.table_widget.setRowCount(len(rows))  # Configura el número de filas

        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(data)))

    # Métodos para manejar las acciones de la barra de herramientas
    def generar_grafico(self):
        print("Agregar movimiento: Implementar esta función.")

    def exportar_csv(self):
        print("Editar movimiento: Implementar esta función.")

    def exportar_pdf(self):
        print("Eliminar movimiento: Implementar esta función.")