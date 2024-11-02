# @author: Cristian Echevarria
# @colab: Oscar Teran
# utf-8
# python 3.12
# sistema_inv.py v1.0

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.tools.views import InicioView, ProveedorView, ProductosView, AnalisisView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_stylesheet(r"ui\resources\styles.qss")  # Carga los estilos desde el archivo
        self.setWindowTitle("Sistema de Inventario")
        self.setMinimumSize(1000, 600)

        # Creamos un widget principal y su layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Creamos el encabezado
        header = QWidget()
        header.setStyleSheet("background-color: #1e2124;")
        header.setFixedHeight(50)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)

        # Menu burger boton para alternar el sidebar
        self.menu_button = QPushButton()
        self.menu_button.setIcon(QIcon(r"ui/resources/img/menu.png"))
        self.menu_button.setFixedSize(50, 50)
        self.menu_button.setIconSize(QSize(50, 50))
        self.menu_button.setStyleSheet("border: none;")
        self.menu_button.clicked.connect(self.toggle_sidebar)
        header_layout.addWidget(self.menu_button, alignment=Qt.AlignLeft)

        # Contenedor para la barra de búsqueda
        search_container = QWidget()
        search_container_layout = QHBoxLayout(search_container)
        search_container_layout.setContentsMargins(0, 0, 0, 0)
        search_container_layout.setSpacing(5)

        # Agregar barra de búsqueda al contenedor
        search = QLineEdit()
        search.setPlaceholderText("Buscar")
        search.setFixedWidth(300)
        search_container_layout.addWidget(search)

        # Agregar botón de búsqueda
        button_search = QPushButton()
        button_search.setIcon(QIcon(r"ui/resources/img/search.png"))
        button_search.setFixedSize(50, 50)
        button_search.setIconSize(QSize(50, 50))
        button_search.setStyleSheet("border: none;")
        search_container_layout.addWidget(button_search)

        # Agregar contenedor de búsqueda al encabezado
        header_layout.addWidget(search_container, alignment=Qt.AlignCenter)

        # Creamos el sidebar
        self.sidebar = QFrame()
        self.sidebar.setStyleSheet(""" QFrame { background-color: #2f3136; border: none; } """)
        self.sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        # items del menu en el sidebar
        menu_items = ["Inicio", "Proveedores", "Productos", "Análisis"]
        self.stacked_widget = QStackedWidget()

        for item in menu_items:
            btn = QPushButton(item)
            btn.setObjectName("menu_button")  # Asignar un nombre de objeto (opcional)
            btn.setProperty("class", "MenuButton")  # Aplicar la clase para los estilos
            btn.clicked.connect(lambda checked, text=item: self.on_menu_click(text))
            sidebar_layout.addWidget(btn)

            # Agregar la vista correspondiente al stacked widget
            if item == "Inicio":
                # Si el item es "Inicio", creamos una instancia de InicioView
                page = InicioView()
            elif item == "Proveedores":
                # Si el item es "Proveedores", creamos una instancia de ProveedorView
                page = ProveedorView()
            elif item == "Productos":
                # Si el item es "Productos", creamos una instancia de ProductosView
                page = ProductosView()
            elif item == "Análisis":
                # Si el item es "Análisis", creamos una instancia de AnalisisView
                page = AnalisisView()

            # Agregar la vista al stacked widget
            self.stacked_widget.addWidget(page)

        # Aseguramos que el sidebar ocupe todo el ancho disponible
        sidebar_layout.addStretch()

        # Cremos el area de contenido
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Area de contenido principal
        main_content = QWidget()
        main_content.setStyleSheet("background-color: #36393f;")
        main_content_layout = QVBoxLayout(main_content)
        main_content_layout.addWidget(self.stacked_widget)

        # Agregamos el contenido principal al layout principal
        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        container_layout.addWidget(self.sidebar)
        container_layout.addWidget(main_content, 1)
        content_layout.addWidget(container)
        layout.addWidget(header)
        layout.addWidget(content)

        # Agregamos el pie de página
        footer = QLabel("© 2024 Sistema de Inventario. | Echxvx2610 | Teran")
        footer.setStyleSheet(""" QLabel { background-color: #1e2124; color: #72767d; padding: 10px; } """)
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)

    #funcion para cargar el archivo de estilos 
    def load_stylesheet(self, filepath):
        """Load stylesheet from a file."""
        with open(filepath, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

    # funcion para mostrar y ocultar el sidebar
    def toggle_sidebar(self):
        """Toggle sidebar visibility."""
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()
            
    # funcion para cambiar de vista
    def on_menu_click(self, text):
        """Switch to the selected view."""
        index = ["Inicio", "Proveedores", "Productos", "Análisis"].index(text)
        self.stacked_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows11")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
