# views.py

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
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

        # Cambia el fondo a blanco
        self.setStyleSheet("background-color: white;")

        # Create a tab widget
        tab_widget = QTabWidget()
        tab_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Asegura que ocupe todo el espacio
        tab_widget.tabBar().setExpanding(True)  # Esto ayuda a que las pestañas se extiendan
        tab_widget.setTabShape(QTabWidget.Rounded)  # Cambia la forma de las pestañas a redonda
        tab_widget.setStyleSheet("QTabWidget::pane { border: none; }")  # Eliminar el borde de la pestaña
        
        # Tab 1: Información General
        tab1 = QWidget()
        tab1_layout = QFormLayout()
        tab1_layout.addRow("Nombre del Proveedor:", QLineEdit())
        tab1_layout.addRow("Email:", QLineEdit())
        tab1_layout.addRow("Teléfono:", QLineEdit())
        tab1_layout.addRow("Calle:", QLineEdit())
        tab1_layout.addRow("Ciudad:", QLineEdit())
        tab1_layout.addRow("Estado:", QLineEdit())
        tab1_layout.addRow("Código Postal:", QLineEdit())
        tab1.setLayout(tab1_layout)

        # Tab 2: Dirección
        tab2 = QWidget()
        tab2_layout = QFormLayout()
        tab2_layout.addRow("Notas:", QLineEdit())
        tab2.setLayout(tab2_layout)

        # Tab 3: Notas
        tab3 = QWidget()
        tab3_layout = QFormLayout()
        tab3_layout.addRow("Notas:", QLineEdit())
        tab3.setLayout(tab3_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(tab1, "Registrar Proveedor")
        tab_widget.addTab(tab2, "Actualizar Información")
        tab_widget.addTab(tab3, "Eliminar Proveedor")

        # Add the tab widget to the main layout
        layout.addWidget(tab_widget)


class ProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Productos")
        label.setFont(QFont("Arial", 24))
        label.setStyleSheet("color: white;")
        layout.addWidget(label, alignment=Qt.AlignCenter)


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
