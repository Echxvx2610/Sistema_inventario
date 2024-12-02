# views.py
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from .operaciones_BD import *
import matplotlib.pyplot as plt
import numpy as np
import re  # Importar para usar expresiones regulares
import plotly.graph_objects as go
import plotly.express as px
import webbrowser
import os
import pandas as pd
from playwright.async_api import async_playwright
import asyncio
import datetime


class InicioView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        #label = QLabel("Vista de Inicio")
        #label.setFont(QFont("Arial", 24))
        #label.setStyleSheet("color: white;")
        saludo = QLabel("Bienvenido, Echxvx2610")
        saludo.setFont(QFont("Arial", 16))
        saludo.setStyleSheet("color: white;")
       #layout.addWidget(label, alignment=Qt.AlignCenter)
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
    proveedor_eliminado = Signal()  # Señal para notificar cuando se elimine un proveedor

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear un contenedor horizontal para la barra de herramientas y la barra de búsqueda
        header_layout = QHBoxLayout()

        # Crear la barra de herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")

        # Acción para agregar proveedor
        add_action = QAction(QIcon(r"ui\resources\img\agregar_usuario.png"), "Agregar", self)
        add_action.triggered.connect(self.agregar_proveedor)
        toolbar.setIconSize(QSize(45, 45))
        toolbar.addAction(add_action)

        # Acción para editar proveedor
        edit_action = QAction(QIcon(r"ui\resources\img\editar_usuario.png"), "Editar", self)
        edit_action.triggered.connect(self.editar_proveedor)
        toolbar.addAction(edit_action)

        # Acción para eliminar proveedor
        delete_action = QAction(QIcon(r"ui\resources\img\eliminar_usuario.png"), "Eliminar", self)
        delete_action.triggered.connect(self.eliminar_proveedor)
        toolbar.addAction(delete_action)

        # Agregar la barra de herramientas al contenedor header_layout
        header_layout.addWidget(toolbar)

        # Contenedor para la barra de búsqueda
        search_container = QWidget()
        search_container_layout = QHBoxLayout(search_container)
        search_container_layout.setContentsMargins(0, 0, 0, 0)
        search_container_layout.setSpacing(5)
        search_container.setStyleSheet("background-color: #2f3136; padding: 5px;")
        
        # Barra de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar Proveedor")
        self.search_input.setFixedWidth(200)
        self.search_input.setStyleSheet("background-color: #2f3136; color: white ; border-bottom: 1px solid #72767d; padding: 5px;")
        search_container_layout.addWidget(self.search_input)

        # Agregar botón de búsqueda
        button_search = QPushButton("Buscar")
        button_search.setIcon(QIcon(r"ui/resources/img/search.png"))
        button_search.setFixedSize(150, 50)
        button_search.setIconSize(QSize(150, 50))
        button_search.setToolTip("Buscar un proveedor")
        button_search.setStyleSheet("color: white;")
        button_search.clicked.connect(self.buscar_proveedor)
        search_container_layout.addWidget(button_search)

        # Agregar botón de "Mostrar Todo"
        button_show_all = QPushButton("Mostrar Todo")
        button_show_all.setIcon(QIcon(r"ui/resources/img/datos.png"))
        button_show_all.setFixedSize(150, 50)
        button_show_all.setIconSize(QSize(150, 50))
        button_show_all.setToolTip("Mostrar todos los proveedores")
        button_show_all.setStyleSheet("color: white;")
        button_show_all.clicked.connect(self.reload_data)  # Conectar al método correspondiente
        search_container_layout.addWidget(button_show_all)

        # Agregar la barra de búsqueda al contenedor header_layout
        header_layout.addWidget(search_container)

        # Agregar header_layout al layout principal
        layout.addLayout(header_layout)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Dirección", "Teléfono"])
        self.table_widget.verticalHeader().hide()  # Ocultar encabezado vertical
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Hacer que las columnas se estiren

        # Ajustar el tamaño de las filas
        self.table_widget.setRowHeight(0, 30)  # Tamaño mínimo de la fila
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 30)  # Ajustar todas las filas

        # Cambiar el tamaño de la fuente
        font = QFont()
        font.setPointSize(12)
        self.table_widget.setFont(font)

        layout.addWidget(self.table_widget)

        # Cargar los datos de la base de datos
        load_data_proveedor(self)

    def agregar_proveedor(self):
        # Crear un diálogo para agregar un nuevo proveedor
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Proveedor")

        layout = QVBoxLayout(dialog)

        # Campos para agregar proveedor
        nombre_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(nombre_input)

        apellido_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Apellido:"))
        layout.addWidget(apellido_input)

        direccion_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Dirección:"))
        layout.addWidget(direccion_input)

        telefono_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Teléfono:"))
        layout.addWidget(telefono_input)

        # Botón para confirmar la adición
        save_button = QPushButton("Agregar", dialog)
        save_button.clicked.connect(lambda: self.guardar_agregado(
            dialog,
            nombre_input.text(),
            apellido_input.text(),
            direccion_input.text(),
            telefono_input.text()
        ))
        layout.addWidget(save_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def guardar_agregado(self, dialog, nombre, apellido, direccion, telefono):
        # Validación de campos
        if not nombre or not apellido or not direccion or not telefono:
            QMessageBox.warning(self, "Campos incompletos", "Todos los campos son obligatorios.")
            return
        
        # Validar que el teléfono sea numérico y tenga una longitud adecuada
        if not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 15:
            QMessageBox.warning(self, "Teléfono inválido", "El teléfono debe ser un número de entre 7 y 15 dígitos.")
            return
        
        # Validar que nombre y apellido no contengan números
        if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            QMessageBox.warning(self, "Nombre inválido", "El nombre no debe contener números ni caracteres especiales.")
            return
        
        if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", apellido):
            QMessageBox.warning(self, "Apellido inválido", "El apellido no debe contener números ni caracteres especiales.")
            return

        try:
            add_proveedor(nombre, apellido, direccion, telefono)
            load_data_proveedor(self)  # Recargar la tabla después de agregar
            dialog.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo agregar el proveedor: {str(e)}")
            print("Error al agregar el proveedor:", str(e))

    def editar_proveedor(self):
        # Obtener el proveedor seleccionado
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            proveedor_id = self.table_widget.item(current_row, 0).text()
            nombre_actual = self.table_widget.item(current_row, 1).text()
            apellido_actual = self.table_widget.item(current_row, 2).text()
            direccion_actual = self.table_widget.item(current_row, 3).text()
            telefono_actual = self.table_widget.item(current_row, 4).text()

            # Crear un diálogo para editar el proveedor
            dialog = QDialog(self)
            dialog.setWindowTitle("Editar Proveedor")

            layout = QVBoxLayout(dialog)

            # Campos para editar proveedor
            nombre_input = QLineEdit(dialog)
            nombre_input.setText(nombre_actual)
            layout.addWidget(QLabel("Nombre:"))
            layout.addWidget(nombre_input)

            apellido_input = QLineEdit(dialog)
            apellido_input.setText(apellido_actual)
            layout.addWidget(QLabel("Apellido:"))
            layout.addWidget(apellido_input)

            direccion_input = QLineEdit(dialog)
            direccion_input.setText(direccion_actual)
            layout.addWidget(QLabel("Dirección:"))
            layout.addWidget(direccion_input)

            telefono_input = QLineEdit(dialog)
            telefono_input.setText(telefono_actual)
            layout.addWidget(QLabel("Teléfono:"))
            layout.addWidget(telefono_input)

            # Botón para confirmar la edición
            save_button = QPushButton("Guardar cambios", dialog)
            save_button.clicked.connect(lambda: self.guardar_edicion(
                dialog,
                proveedor_id,
                nombre_input.text(),
                apellido_input.text(),
                direccion_input.text(),
                telefono_input.text()
            ))
            layout.addWidget(save_button)

            dialog.setLayout(layout)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Proveedor no seleccionado", "Por favor, seleccione un proveedor para editar.")
            
    def guardar_edicion(self, dialog, proveedor_id, nombre, apellido, direccion, telefono):
        # Validación de campos
        if not nombre or not apellido or not direccion or not telefono:
            QMessageBox.warning(self, "Campos incompletos", "Todos los campos son obligatorios.")
            return
        
        # Validar que el teléfono sea numérico y tenga una longitud adecuada
        if not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 15:
            QMessageBox.warning(self, "Teléfono inválido", "El teléfono debe ser un número de entre 7 y 15 dígitos.")
            return
        
        # Validar que nombre y apellido no contengan números
        if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            QMessageBox.warning(self, "Nombre inválido", "El nombre no debe contener números ni caracteres especiales.")
            return
        
        if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", apellido):
            QMessageBox.warning(self, "Apellido inválido", "El apellido no debe contener números ni caracteres especiales.")
            return

        try:
            edit_proveedor(proveedor_id, nombre, apellido, direccion, telefono)
            load_data_proveedor(self)  # Recargar la tabla después de editar
            dialog.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo editar el proveedor: {str(e)}")
            print("Error al editar el proveedor:", str(e))

    def eliminar_proveedor(self):
        selected_index = self.table_widget.currentRow()
        if selected_index == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor para eliminar")
            return

        proveedor_id = self.table_widget.item(selected_index, 0).text()

        respuesta = QMessageBox.question(
            self,
            "Eliminar Proveedor",
            "¿Estás seguro de eliminar el proveedor? \nEliminar un proveedor eliminará todos los productos asociados a él.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            try:
                delete_proveedor(proveedor_id)
                # Emitir la señal después de eliminar el proveedor
                self.proveedor_eliminado.emit()
                # Llamar a load_data_proveedor directamente desde operaciones_BD
                load_data_proveedor(self)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el proveedor: {str(e)}")
                print("Error al eliminar el proveedor:", str(e))

    def buscar_proveedor(self):
        # Obtener el texto ingresado en la barra de búsqueda
        termino_busqueda = self.search_input.text().strip()

        # Validar que no esté vacío
        if not termino_busqueda:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa un término para buscar.")
            logging.warning("Por favor, ingresa un término para buscar.")
            return

        # Consultar la base de datos
        try:
            resultados = buscar_proveedor(termino_busqueda)  # Llamada a la función buscar_proveedor
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar en la base de datos: {e}")
            logging.error(f"Error al buscar en la base de datos: {e}")
            return

        # Verificar si hay resultados
        if not resultados:
            QMessageBox.information(self, "Sin resultados", "No se encontraron proveedores que coincidan con el término ingresado.")
            logging.warning("No se encontraron proveedores que coincidan con el término ingresado.")
            load_data_proveedor(self)  # Asumiendo que tienes una función para cargar los proveedores
            return

        # Poblar la tabla con los resultados
        self.table_widget.setRowCount(0)  # Limpiar la tabla antes de llenarla
        for row_idx, row_data in enumerate(resultados):
            self.table_widget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_idx, col_idx, item)


    def reload_data(self):
        #limpiar search input
        self.search_input.clear()
        load_data_proveedor(self)

class ProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # Crear un contenedor horizontal para la barra de herramientas y la barra de búsqueda
        header_layout = QHBoxLayout()

        # Crear la barra de herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #2f3136; padding: 5px; color: white;")

        # Acción para agregar producto
        add_action = QAction(QIcon(r"ui\resources\img\agregar_producto.png"), "Agregar", self)
        add_action.triggered.connect(self.agregar_producto)
        toolbar.setIconSize(QSize(45, 45))
        toolbar.addAction(add_action)

        # Acción para editar producto
        edit_action = QAction(QIcon(r"ui\resources\img\editar_producto.png"), "Editar", self)
        edit_action.triggered.connect(self.editar_producto)
        toolbar.addAction(edit_action)

        # Acción para eliminar producto
        delete_action = QAction(QIcon(r"ui\resources\img\eliminar_producto.png"), "Eliminar", self)
        delete_action.triggered.connect(self.eliminar_producto)
        toolbar.addAction(delete_action)

        # Agregar la barra de herramientas al contenedor header_layout
        header_layout.addWidget(toolbar)

        # Contenedor para la barra de búsqueda
        search_container = QWidget()
        search_container_layout = QHBoxLayout(search_container)
        search_container_layout.setContentsMargins(0, 0, 0, 0)
        search_container_layout.setSpacing(5)
        search_container.setStyleSheet("background-color: #2f3136; padding: 5px;")
        
        # Agregar barra de búsqueda al contenedor ( Declarar como atributo de clase )
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar productos")
        self.search_input.setFixedWidth(200)
        self.search_input.setStyleSheet("background-color: #2f3136; color: white ; border-bottom: 1px solid #72767d; padding: 5px;")
        search_container_layout.addWidget(self.search_input)

        # Agregar botón de búsqueda
        button_search = QPushButton("Buscar")
        button_search.setIcon(QIcon(r"ui/resources/img/search.png"))
        button_search.setFixedSize(150, 50)
        button_search.setIconSize(QSize(150, 50))
        button_search.setToolTip("Buscar productos")
        button_search.setStyleSheet("color: white;")
        button_search.clicked.connect(self.buscar_producto)
        search_container_layout.addWidget(button_search)

        # Agregar botón de "Mostrar Todo"
        button_show_all = QPushButton("Mostrar Todo")
        button_show_all.setIcon(QIcon(r"ui/resources/img/datos.png"))
        button_show_all.setFixedSize(150, 50)
        button_show_all.setIconSize(QSize(150, 50))
        button_show_all.setToolTip("Mostrar todos los productos")
        button_show_all.setStyleSheet("color: white;")
        button_show_all.clicked.connect(self.reload_data)  # Conectar al método correspondiente
        search_container_layout.addWidget(button_show_all)

        # Agregar la barra de búsqueda al contenedor header_layout
        header_layout.addWidget(search_container)

        # Agregar header_layout al layout principal
        layout.addLayout(header_layout)

        # Crear la tabla para mostrar los datos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)  # Número de columnas que deseas mostrar
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Precio", "Cantidad en Stock"])
        # Eliminar índice de las filas
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
        # Crear un diálogo para agregar el producto
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Producto")

        layout = QVBoxLayout(dialog)

        # Campos para ingresar datos
        nombre_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(nombre_input)

        # ComboBox para seleccionar la categoría
        categoria_combo = QComboBox(dialog)
        categorias = ["Bebidas", "Snack", "Limpieza", "Autos", "Electronicos", "Abarrotes", "Carnes", "Frutas & Verduras"]
        
        # Añadir las opciones al QComboBox
        categoria_combo.addItems(categorias)
        
        # Campo para agregar una nueva categoría si no está en la lista
        nueva_categoria_input = QLineEdit(dialog)
        nueva_categoria_input.setPlaceholderText("Agregar nueva categoría (opcional)")
        
        # Botón para confirmar la adición de nueva categoría
        agregar_categoria_button = QPushButton("Agregar Categoría", dialog)
        def agregar_categoria():
            nueva_categoria = nueva_categoria_input.text().strip()
            if nueva_categoria and nueva_categoria not in categorias:
                categorias.append(nueva_categoria)
                categoria_combo.addItem(nueva_categoria)
                nueva_categoria_input.clear()
                QMessageBox.information(dialog, "Categoría Agregada", f"Categoría '{nueva_categoria}' agregada exitosamente.")
        
        agregar_categoria_button.clicked.connect(agregar_categoria)
        
        layout.addWidget(QLabel("Categoría:"))
        layout.addWidget(categoria_combo)
        layout.addWidget(nueva_categoria_input)
        layout.addWidget(agregar_categoria_button)

        # Precio input
        precio_input = QDoubleSpinBox(dialog)
        precio_input.setRange(0.01, 999999.99)
        precio_input.setValue(100.0)
        layout.addWidget(QLabel("Precio:"))
        layout.addWidget(precio_input)

        # Stock mínimo input
        stock_minimo_input = QSpinBox(dialog)
        stock_minimo_input.setRange(0, 999999)
        stock_minimo_input.setValue(10)
        layout.addWidget(QLabel("Stock Mínimo:"))
        layout.addWidget(stock_minimo_input)

        # Cantidad en stock input
        cantidad_input = QSpinBox(dialog)
        cantidad_input.setRange(0, 999999)
        cantidad_input.setValue(0)
        layout.addWidget(QLabel("Cantidad en Stock:"))
        layout.addWidget(cantidad_input)

        # ComboBox para seleccionar proveedor
        proveedor_combo = QComboBox(dialog)
        proveedores = load_data_proveedor_combobox()  # Debería devolver una lista de tuplas (proveedor_id, nombre)
        
        if proveedores:
            for proveedor_id, nombre in proveedores:
                proveedor_combo.addItem(nombre, proveedor_id)

        layout.addWidget(QLabel("Seleccionar Proveedor:"))
        layout.addWidget(proveedor_combo)

        # Botón para confirmar la adición
        save_button = QPushButton("Agregar", dialog)
        save_button.clicked.connect(lambda: self.guardar_nuevo_producto(
            dialog,
            nombre_input.text(),                # nombre_producto
            categoria_combo.currentText(),      # categoría seleccionada
            precio_input.value(),               # precio
            stock_minimo_input.value(),         # stock_minimo
            cantidad_input.value(),             # cantidad_en_stock
            proveedor_combo.currentData()       # proveedor_id
        ))
        layout.addWidget(save_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def guardar_nuevo_producto(self, dialog, nombre, categoria, precio, stock_minimo, cantidad, proveedor_id):
        # Validaciones de los datos
        if not nombre.strip() or not categoria.strip():
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completa los campos Nombre y Categoría.")
            return

        if precio <= 0:
            QMessageBox.warning(self, "Precio inválido", "El precio debe ser mayor que 0.")
            return

        if stock_minimo <= 0:
            QMessageBox.warning(self, "Stock Mínimo inválido", "El stock mínimo debe ser mayor que 0.")
            return

        if cantidad < 0:
            QMessageBox.warning(self, "Cantidad inválida", "La cantidad no puede ser negativa.")
            return

        if proveedor_id is None:
            QMessageBox.warning(self, "Proveedor requerido", "Por favor, selecciona un proveedor.")
            return

        # Si todo es válido, guardar el producto
        add_producto(nombre, categoria, precio, stock_minimo, cantidad, proveedor_id)
        load_data_productos(self)  # Recargar datos de productos
        dialog.accept()

    def editar_producto(self):
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            # Obtener el ID del producto actual
            producto_id = self.table_widget.item(current_row, 0).text()
            nombre_actual = self.table_widget.item(current_row, 1).text()
            precio_actual = self.table_widget.item(current_row, 3).text()
            print(precio_actual)
            # Obtener stock mínimo actual desde la tabla
            stock_minimo_actual = self.table_widget.item(current_row, 4).text() 
            stock_actual = self.table_widget.item(current_row, 5).text()
            
            # Crear un diálogo para editar el producto
            dialog = QDialog(self)
            dialog.setWindowTitle("Editar Producto")

            layout = QVBoxLayout(dialog)

            # Campos para editar
            nombre_input = QLineEdit(dialog)
            nombre_input.setText(nombre_actual)
            layout.addWidget(QLabel("Nombre:"))
            layout.addWidget(nombre_input)

            # Crear el input para el precio (usando QLineEdit)
            precio_input = QLineEdit(dialog)
            precio_input.setText(precio_actual)  # Establecer el valor inicial
            precio_input.setValidator(QDoubleValidator(0.0, 10000.0, 2))  # Validar como número con dos decimales
            layout.addWidget(QLabel("Precio:"))
            layout.addWidget(precio_input)

            # Crear el input para el stock mínimo (usando QLineEdit)
            stock_minimo_input = QLineEdit(dialog)
            stock_minimo_input.setText(stock_minimo_actual)  # Establecer el valor inicial
            stock_minimo_input.setValidator(QIntValidator(0, 10000))  # Validar como número entero
            layout.addWidget(QLabel("Stock Mínimo:"))
            layout.addWidget(stock_minimo_input)

            # Crear el input para la cantidad en stock (usando QLineEdit)
            stock_input = QLineEdit(dialog)
            stock_input.setText(stock_actual)  # Establecer el valor inicial
            stock_input.setValidator(QIntValidator(0, 10000))  # Validar como número entero
            layout.addWidget(QLabel("Cantidad en Stock:"))
            layout.addWidget(stock_input)

            # ComboBox para seleccionar un nuevo proveedor
            proveedor_combo = QComboBox(dialog)
            proveedores = load_data_proveedor_combobox()  # Ahora debería devolver una lista de tuplas (provedor_id, nombre)

            if proveedores:
                for proveedor_id, nombre in proveedores:
                    proveedor_combo.addItem(nombre, proveedor_id)  # Agregar el nombre y el ID como dato

            layout.addWidget(QLabel("Seleccionar Proveedor:"))
            layout.addWidget(proveedor_combo)

            # Botón para confirmar la edición
            save_button = QPushButton("Guardar", dialog)
            save_button.clicked.connect(lambda: self.guardar_edicion(
                dialog,
                producto_id,
                nombre_input.text(),                   # nombre_producto
                precio_input.text(),                   # precio (como texto)
                stock_minimo_input.text(),             # stock_minimo (como texto)
                stock_input.text(),                    # cantidad_en_stock (como texto)
                proveedor_combo.currentData()           # proveedor_id
            ))
            layout.addWidget(save_button)

            dialog.setLayout(layout)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Producto no seleccionado", "Por favor, selecciona un producto para editar.")
    def guardar_edicion(self, dialog, producto_id, nombre, precio, stock_minimo, cantidad, proveedor_id):
        # Validaciones de los datos
        if not nombre.strip():
            QMessageBox.warning(self, "Nombre inválido", "El nombre no puede estar vacío.")
            return

        try:
            precio = float(precio)  # Intentar convertir el precio de texto a flotante
        except ValueError:
            QMessageBox.warning(self, "Precio inválido", "El precio debe ser un número válido.")
            return

        if precio <= 0:
            QMessageBox.warning(self, "Precio inválido", "El precio debe ser mayor que 0.")
            return

        try:
            stock_minimo = int(stock_minimo)  # Intentar convertir el stock mínimo a entero
        except ValueError:
            QMessageBox.warning(self, "Stock Mínimo inválido", "El stock mínimo debe ser un número válido.")
            return

        if stock_minimo <= 0:
            QMessageBox.warning(self, "Stock Mínimo inválido", "El stock mínimo debe ser mayor que 0.")
            return

        try:
            cantidad = int(cantidad)  # Intentar convertir la cantidad a entero
        except ValueError:
            QMessageBox.warning(self, "Cantidad inválida", "La cantidad debe ser un número válido.")
            return

        if cantidad < 0:
            QMessageBox.warning(self, "Cantidad inválida", "La cantidad no puede ser negativa.")
            return

        if proveedor_id is None:
            QMessageBox.warning(self, "Proveedor requerido", "Por favor, selecciona un proveedor.")
            return

        # Si todo es válido, guardar los cambios del producto
        edit_producto(producto_id, nombre, precio, cantidad, stock_minimo, proveedor_id)
        load_data_productos(self)  # Recargar datos de productos
        dialog.accept()

    def eliminar_producto(self):
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            producto_id = self.table_widget.item(current_row, 0).text()
            question = QMessageBox.question(
                self,
                "Eliminar Producto",
                "¿Esta seguro de eliminar el producto?",
                QMessageBox.Yes | QMessageBox.No
            )
            if question == QMessageBox.No:
                return
            delete_producto(producto_id)
            load_data_productos(self)  # Recargar datos
        else:
            QMessageBox.warning(self, "Producto no seleccionado", "Por favor, selecciona un producto para eliminar.")

    def reload_data(self):
        """Recarga los datos de la tabla de productos."""
        # limpiar search input
        self.search_input.setText("")
        load_data_productos(self)

    def buscar_producto(self):
        # Obtener el texto ingresado en la barra de búsqueda
        termino_busqueda = self.search_input.text().strip()

        # Validar que no esté vacío
        if not termino_busqueda:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa un término para buscar.")
            logging.warning("Por favor, ingresa un término para buscar.")
            return

        # Consultar la base de datos
        try:
            resultados = buscar_producto(termino_busqueda)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar en la base de datos: {e}")
            logging.error(f"Error al buscar en la base de datos: {e}")
            return

        # Verificar si hay resultados
        if not resultados:
            QMessageBox.information(self, "Sin resultados", "No se encontraron productos que coincidan con el término ingresado.")
            logging.warning("No se encontraron productos que coincidan con el término ingresado.")
            load_data_productos(self)
            return

        # Poblar la tabla con los resultados
        self.table_widget.setRowCount(0)  # Limpiar la tabla antes de llenarla
        for row_idx, row_data in enumerate(resultados):
            self.table_widget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_idx, col_idx, item)

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

    def showEvent(self, event):
        """
        Este método se llama cada vez que la vista es mostrada.
        Aquí se actualizan los datos de la tabla.
        """
        self.cargar_datos()
        super().showEvent(event)  # Llamada al método showEvent original

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
        # Cargar los datos de historial y productos
        historial = load_historial()  # Función que carga los datos de `historial_inventario`
        productos = load_productos()  # Función que carga los datos de la tabla `productos`

        # Crear un diccionario para mapear producto_id a información del producto
        info_productos = {producto[0]: {"nombre": producto[1], "precio": float(producto[3])} for producto in productos}

        # Separar datos del historial
        ids_productos = [row[1] for row in historial]
        cantidad_movimiento = [row[2] for row in historial]
        tipo_movimiento = [row[5] for row in historial]

        # Calcular las métricas necesarias
        ganancias = []
        salidas = {}
        entradas = {}

        for producto_id, cantidad, movimiento in zip(ids_productos, cantidad_movimiento, tipo_movimiento):
            if movimiento == 'salida' and producto_id in info_productos:
                precio = info_productos[producto_id]["precio"]
                ganancias.append(precio * cantidad)
                salidas[producto_id] = salidas.get(producto_id, 0) + cantidad
            elif movimiento == 'entrada' and producto_id in info_productos:
                entradas[producto_id] = entradas.get(producto_id, 0) + cantidad

        # Validar si hay datos para salidas
        if not salidas:
            message = "No hay datos de movimientos tipo 'salida' en el historial para generar gráficos."
            QMessageBox.warning(self, "Advertencia", message)
            return [], {}, {}, "", "", ""

        # Ordenar productos por salidas
        productos_mas_vendidos = sorted(salidas.items(), key=lambda x: x[1], reverse=True)[:5]

        # Identificar productos menos vendidos (mayores entradas y menos salidas)
        productos_menos_vendidos = []
        for producto_id in entradas:
            cantidad_entrada = entradas[producto_id]
            cantidad_salida = salidas.get(producto_id, 0)
            if cantidad_entrada > cantidad_salida:
                productos_menos_vendidos.append((producto_id, cantidad_entrada - cantidad_salida))

        productos_menos_vendidos = sorted(productos_menos_vendidos, key=lambda x: x[1], reverse=True)[:5]

        # Gráfico 1: Ganancias por producto (barras)
        fig1 = go.Figure(data=[go.Bar(
            x=[info_productos[producto_id]["nombre"] for producto_id in salidas.keys()],
            y=ganancias,
            marker=dict(color='green')
        )])
        fig1.update_layout(
            title='Ganancias por Producto',
            xaxis_title='Producto',
            yaxis_title='Ganancias ($)',
            template='plotly_white'
        )

        # Gráfico 2: Productos más vendidos (pastel)
        fig2 = px.pie(
            names=[info_productos[producto_id]["nombre"] for producto_id, _ in productos_mas_vendidos],
            values=[cantidad for _, cantidad in productos_mas_vendidos],
            title='Productos Más Vendidos'
        )

        # Gráfico 3: Productos menos vendidos (barras)
        fig3 = go.Figure(data=[go.Bar(
            x=[info_productos[producto_id]["nombre"] for producto_id, _ in productos_menos_vendidos],
            y=[cantidad for _, cantidad in productos_menos_vendidos],
            marker=dict(color='red')
        )])
        fig3.update_layout(
            title='Productos Menos Vendidos (Con Más Entradas y Menos Salidas)',
            xaxis_title='Producto',
            yaxis_title='Diferencia de Entradas y Salidas',
            template='plotly_white'
        )

        # Convertir los gráficos a HTML
        fig1_html = fig1.to_html(full_html=False, include_plotlyjs='cdn')
        fig2_html = fig2.to_html(full_html=False, include_plotlyjs=False)
        fig3_html = fig3.to_html(full_html=False, include_plotlyjs=False)

        # Crear la carpeta y guardar los gráficos en un archivo HTML
        html_file = r'ui/resources/reportes/html/grafico_inventario.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)

        # Agregar encabezado al HTML
        with open(html_file, 'w') as f:
            f.write('<html>\n<head>\n<title>Reporte de Inventario</title>\n</head>\n<body>\n')
            f.write('<h1 style="text-align: center;">Reporte de Inventario de Productos</h1>\n')  # Título principal del reporte
            f.write('<p>A continuación se presentan los gráficos de inventario:</p>\n')  # Descripción o subtítulo
            
            # Insertar los gráficos generados
            f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
            f.write(fig2.to_html(full_html=False, include_plotlyjs=False))
            f.write(fig3.to_html(full_html=False, include_plotlyjs=False))
    
            f.write('</body>\n</html>')

        # Abrir el archivo HTML en el navegador
        webbrowser.open(f'file://{os.path.abspath(html_file)}')

        return ganancias, salidas, entradas, fig1_html, fig2_html, fig3_html

    def exportar_csv(self):
        try:
            # Obtener los datos que deseas exportar, por ejemplo, productos
            productos = load_productos()  # Cargar productos de la base de datos
            # Crear un DataFrame de pandas con los datos
            df = pd.DataFrame(productos, columns=["producto_id", "nombre_producto", "categoria", "precio", "stock_minimo", "cantidad_en_stock", "proveedor_id"])

            # Ruta del archivo CSV
            csv_file = 'ui/resources/reportes/csv/inventario_productos.csv'

            # Exportar el DataFrame a un archivo CSV
            df.to_csv(csv_file, index=False)

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Éxito", f"CSV exportado exitosamente a {csv_file}")
            print(f"CSV exportado exitosamente a {csv_file}")
        except Exception as e:
            # Manejar posibles errores
            QMessageBox.critical(self, "Error", f"Error al exportar el CSV: {e}")
            print(f"Error al exportar el CSV: {e}")

    def generar_grafico_pdf(self):
        # Cargar los datos de historial y productos
        historial = load_historial()  # Función que carga los datos de `historial_inventario`
        productos = load_productos()  # Función que carga los datos de la tabla `productos`

        # Crear un diccionario para mapear producto_id a información del producto
        info_productos = {producto[0]: {"nombre": producto[1], "precio": float(producto[3])} for producto in productos}

        # Separar datos del historial
        ids_productos = [row[1] for row in historial]
        cantidad_movimiento = [row[2] for row in historial]
        tipo_movimiento = [row[5] for row in historial]

        # Calcular las métricas necesarias
        ganancias = []
        salidas = {}
        entradas = {}

        for producto_id, cantidad, movimiento in zip(ids_productos, cantidad_movimiento, tipo_movimiento):
            if movimiento == 'salida' and producto_id in info_productos:
                precio = info_productos[producto_id]["precio"]
                ganancias.append(precio * cantidad)
                salidas[producto_id] = salidas.get(producto_id, 0) + cantidad
            elif movimiento == 'entrada' and producto_id in info_productos:
                entradas[producto_id] = entradas.get(producto_id, 0) + cantidad

        # Validar si hay datos para salidas
        if not salidas:
            message = "No hay datos de movimientos tipo 'salida' en el historial para generar gráficos."
            QMessageBox.warning(self, "Advertencia", message)
            return [], {}, {}, "", "", ""

        # Ordenar productos por salidas
        productos_mas_vendidos = sorted(salidas.items(), key=lambda x: x[1], reverse=True)[:5]

        # Identificar productos menos vendidos (mayores entradas y menos salidas)
        productos_menos_vendidos = []
        for producto_id in entradas:
            cantidad_entrada = entradas[producto_id]
            cantidad_salida = salidas.get(producto_id, 0)
            if cantidad_entrada > cantidad_salida:
                productos_menos_vendidos.append((producto_id, cantidad_entrada - cantidad_salida))

        productos_menos_vendidos = sorted(productos_menos_vendidos, key=lambda x: x[1], reverse=True)[:5]

        # Gráfico 1: Ganancias por producto (barras)
        fig1 = go.Figure(data=[go.Bar(
            x=[info_productos[producto_id]["nombre"] for producto_id in salidas.keys()],
            y=ganancias,
            marker=dict(color='green')
        )])
        fig1.update_layout(
            title='Ganancias por Producto',
            xaxis_title='Producto',
            yaxis_title='Ganancias ($)',
            template='plotly_white'
        )

        # Gráfico 2: Productos más vendidos (pastel)
        fig2 = px.pie(
            names=[info_productos[producto_id]["nombre"] for producto_id, _ in productos_mas_vendidos],
            values=[cantidad for _, cantidad in productos_mas_vendidos],
            title='Productos Más Vendidos'
        )

        # Gráfico 3: Productos menos vendidos (barras)
        fig3 = go.Figure(data=[go.Bar(
            x=[info_productos[producto_id]["nombre"] for producto_id, _ in productos_menos_vendidos],
            y=[cantidad for _, cantidad in productos_menos_vendidos],
            marker=dict(color='red')
        )])
        fig3.update_layout(
            title='Productos Menos Vendidos (Con Más Entradas y Menos Salidas)',
            xaxis_title='Producto',
            yaxis_title='Diferencia de Entradas y Salidas',
            template='plotly_white'
        )

        # Convertir los gráficos a HTML
        fig1_html = fig1.to_html(full_html=False, include_plotlyjs='cdn')
        fig2_html = fig2.to_html(full_html=False, include_plotlyjs=False)
        fig3_html = fig3.to_html(full_html=False, include_plotlyjs=False)

        return ganancias, salidas, entradas, fig1_html, fig2_html, fig3_html


    def exportar_pdf(self):
        # Ruta del archivo HTML original
        html_file = r'ui/resources/reportes/html/grafico_inventario.html'
        
        # Ruta del archivo PDF de salida
        pdf_file = os.path.join('ui/resources/reportes/pdf', 'grafico_inventario.pdf')

        # Crear la barra de progreso
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)  # Rango de 0 a 100
        self.progress_bar.setValue(0)  # Valor inicial en 0
        self.progress_bar.setTextVisible(True)  # Mostrar texto del progreso
        self.layout().addWidget(self.progress_bar)  # Agregar la barra de progreso al layout

        # Obtener la información clave
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        software_version = "sistema_inv v1.1"
        user_email = "correousuario@gmail.com"

        # Llamar a la función generar_grafico() para obtener los datos del inventario y los gráficos
        ganancia, salidas, entradas, fig1_html, fig2_html, fig3_html = self.generar_grafico_pdf()

        # Calcular los totales
        total_valor_inventario = sum(ganancia)  # Sumar las ganancias
        gasto_inventario = sum([salidas[producto_id] for producto_id in salidas])  # Gasto total de salidas
        venta_inventario = total_valor_inventario  # Las ganancias ya representan la venta total

        # Crear el contenido del HTML con la información clave
        html_content = f"""
        <html>
        <head>
            <title>Reporte de Inventario</title>
        </head>
        <body>
            <h1>Reporte de Inventario</h1>
            
            <p><strong>Fecha y hora:</strong> {current_datetime}</p>
            <p><strong>Software:</strong> {software_version}</p>
            <p><strong>Correo Usuario:</strong> {user_email}</p>
            <p><strong>Valor Total Inventario:</strong> ${total_valor_inventario}</p>
            <p><strong>Gasto de Inventario:</strong> ${gasto_inventario}</p>
            <p><strong>Venta de Inventario:</strong> ${venta_inventario}</p>

            <br>
            <h2>Gráficos</h2>
            {fig1_html}
            {fig2_html}
            {fig3_html}
        </body>
        </html>
        """

        # Guardar el HTML modificado con la información clave
        with open(html_file, 'w') as f:
            f.write(html_content)

        # Crear el hilo para la exportación del PDF
        self.export_thread = ExportPdfThread(html_file, pdf_file)

        # Conectar las señales
        self.export_thread.finished.connect(self.on_export_finished)
        self.export_thread.error.connect(self.on_export_error)
        self.export_thread.progress.connect(self.update_progress_bar)

        # Iniciar el hilo
        self.export_thread.start()

    def update_progress_bar(self, value):
        # Actualizar la barra de progreso con el valor recibido
        self.progress_bar.setValue(value)

    def on_export_finished(self):
        QMessageBox.information(self, "Éxito", "PDF exportado exitosamente.")
        #print("PDF exportado exitosamente.")
        
        # Asegurarnos de que la barra esté al 100% antes de ocultarla o restablecerla
        #self.progress_bar.setValue(100)
        
        # Aquí podemos optar por eliminar la barra de progreso o restablecerla
        self.reset_progress_bar()

    def on_export_error(self, error_message):
        QMessageBox.critical(self, "Error", error_message)
        print(f"Error al exportar el PDF: {error_message}")
        
        # Restablecer la barra de progreso en caso de error
        self.progress_bar.setValue(0)

    def reset_progress_bar(self):
        """Restablece o elimina la barra de progreso después de la tarea."""
        # Opción 1: Restablecer el valor de la barra de progreso
        #self.progress_bar.setValue(0)
        
        # Opción 2: Eliminar la barra de progreso de la interfaz (si ya no la necesitas)
        self.layout().removeWidget(self.progress_bar)
        self.progress_bar.deleteLater()  # Esto eliminará el widget de forma segura


# Crear un hilo para ejecutar la tarea asincrónica
class ExportPdfThread(QThread):
    finished = Signal()  # Señal que se emite cuando el hilo termina
    error = Signal(str)  # Señal que se emite si hay un error
    progress = Signal(int)  # Señal para actualizar la barra de progreso

    def __init__(self, html_file, pdf_file):
        super().__init__()
        self.html_file = html_file
        self.pdf_file = pdf_file

    def run(self):
        asyncio.run(self.exportar_pdf())  # Ejecutar la función asincrónica en el hilo

    async def exportar_pdf(self):
        try:
            # Crear la carpeta de destino si no existe
            pdf_dir = os.path.dirname(self.pdf_file)
            os.makedirs(pdf_dir, exist_ok=True)

            # Iniciar Playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()

                # Cargar el archivo HTML
                await page.goto(f'file:///{self.html_file}', wait_until='load')

                # Simular progreso de la generación del PDF (actualizamos la barra de progreso)
                for i in range(1, 101):
                    self.progress.emit(i)  # Emitir el progreso de 1 a 100
                    await asyncio.sleep(0.05)  # Simulamos un pequeño retraso para la actualización de progreso

                # Generar el PDF
                await page.pdf(path=self.pdf_file, format='A4')
                await browser.close()

            # Emitir señal de finalización
            self.finished.emit()

        except Exception as e:
            # Emitir señal de error
            self.error.emit(f"Error al exportar el PDF: {e}")