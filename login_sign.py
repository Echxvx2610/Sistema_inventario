import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui.tools import operaciones_BD

class ModernLoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.setFixedSize(400, 520)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                font-family: Arial;
            }
            QLineEdit {
                padding: 12px;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                font-size: 14px;
                margin: 8px 0;
            }
            QPushButton {
                padding: 12px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#loginButton {
                background-color: #0052CC;
                color: white;
                border: none;
            }
            QPushButton#toggleButton {
                background-color: transparent;
                border: none;
                color: #0052CC;
                text-align: center;
                padding: 15px 0;
            }
            QPushButton#toggleButton:checked {
                background-color: #0052CC;
                color: white;
                border-radius: 8px;
            }
            QLabel#headerLabel {
                font-size: 24px;
                font-weight: bold;
                margin: 20px 0;
            }
            QLabel#linkLabel {
                color: #0052CC;
                text-decoration: none;
            }
        """)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(main_layout)

        # Header
        header_label = QLabel("Bienvenido")
        header_label.setObjectName("headerLabel")
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # Toggle buttons container
        toggle_container = QWidget()
        toggle_layout = QHBoxLayout(toggle_container)
        toggle_layout.setSpacing(0)
        toggle_layout.setContentsMargins(0, 0, 0, 20)

        # Toggle buttons
        self.login_toggle = QPushButton("Iniciar Sesión")
        self.login_toggle.setObjectName("toggleButton")
        self.login_toggle.setCheckable(True)
        self.login_toggle.setChecked(True)
        self.login_toggle.clicked.connect(self.show_login)

        self.signup_toggle = QPushButton("Registrate")
        self.signup_toggle.setObjectName("toggleButton")
        self.signup_toggle.setCheckable(True)
        self.signup_toggle.clicked.connect(self.show_signup)

        toggle_layout.addWidget(self.login_toggle)
        toggle_layout.addWidget(self.signup_toggle)
        main_layout.addWidget(toggle_container)

        # Stacked widget for login/signup forms
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Login form
        login_widget = QWidget()
        login_layout = QVBoxLayout(login_widget)
        login_layout.setContentsMargins(0, 0, 0, 0)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre de usuario")
        login_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)
        login_layout.addWidget(self.password_input)

        forgot_password = QLabel("Olvidaste tu contraseña?")
        forgot_password.setAlignment(Qt.AlignCenter)
        forgot_password.setObjectName("linkLabel")
        login_layout.addWidget(forgot_password)

        login_button = QPushButton("Iniciar Sesión")
        login_button.setObjectName("loginButton")
        login_button.clicked.connect(self.iniciar_sesion)
        login_layout.addWidget(login_button)

        signup_link = QLabel("No tienes una cuenta? <a href='#' style='color: #0052CC; text-decoration: none;'>Registrate</a>")
        signup_link.setTextFormat(Qt.RichText)
        signup_link.setAlignment(Qt.AlignCenter)
        signup_link.linkActivated.connect(self.show_signup)
        login_layout.addWidget(signup_link)
        login_layout.addStretch()

        # Signup form
        signup_widget = QWidget()
        signup_layout = QVBoxLayout(signup_widget)
        signup_layout.setContentsMargins(0, 0, 0, 0)

        self.signup_username = QLineEdit()
        self.signup_username.setPlaceholderText("Nombre de usuario")
        signup_layout.addWidget(self.signup_username)

        self.signup_email = QLineEdit()
        self.signup_email.setPlaceholderText("Direccion de correo")
        signup_layout.addWidget(self.signup_email)

        self.signup_password = QLineEdit()
        self.signup_password.setPlaceholderText("Contraseña")
        self.signup_password.setEchoMode(QLineEdit.Password)
        signup_layout.addWidget(self.signup_password)

        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Confirmar Contraseña")
        self.confirm_password.setEchoMode(QLineEdit.Password)
        signup_layout.addWidget(self.confirm_password)

        signup_button = QPushButton("Registrarse")
        signup_button.setObjectName("loginButton")
        signup_button.clicked.connect(self.registrar_usuario)  # Conecta al registro
        signup_layout.addWidget(signup_button)

        login_link = QLabel("Ya tienes una cuenta? <a href='#' style='color: #0052CC; text-decoration: none;'>Inicia Sesion</a>")
        login_link.setTextFormat(Qt.RichText)
        login_link.setAlignment(Qt.AlignCenter)
        login_link.linkActivated.connect(self.show_login)
        signup_layout.addWidget(login_link)
        signup_layout.addStretch()

        # Add widgets to stacked widget
        self.stacked_widget.addWidget(login_widget)
        self.stacked_widget.addWidget(signup_widget)



    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)
        self.login_toggle.setChecked(True)
        self.signup_toggle.setChecked(False)

    def show_signup(self):
        self.stacked_widget.setCurrentIndex(1)
        self.login_toggle.setChecked(False)
        self.signup_toggle.setChecked(True)

    def registrar_usuario(self):
        """
        Obtener datos del formulario y registrar al usuario en la base de datos.
        """
        nombre_usuario = self.signup_username.text()
        email = self.signup_email.text()
        contraseña = self.signup_password.text()
        confirmar_contraseña = self.confirm_password.text()

        if not nombre_usuario or not email or not contraseña or not confirmar_contraseña:
            operaciones_BD.mostrar_error("Todos los campos son obligatorios.")
            return

        if contraseña != confirmar_contraseña:
            operaciones_BD.mostrar_error("Las contraseñas no coinciden.")
            return

        resultado = operaciones_BD.registrar_usuario(nombre_usuario, email, contraseña)
        if resultado:
            QMessageBox.information(self, "Registro exitoso", "Usuario registrado correctamente.")
            self.show_login()

    def iniciar_sesion(self):
        """
        Validar las credenciales de inicio de sesión.
        """
        nombre_usuario = self.username_input.text()
        contraseña = self.password_input.text()

        if not nombre_usuario or not contraseña:
            operaciones_BD.mostrar_error("Por favor, ingresa tu nombre de usuario y contraseña.")
            return

        resultado = operaciones_BD.validar_usuario(nombre_usuario, contraseña)

        if resultado:
            nivel_acceso = resultado[0]  # Extraer el nivel de acceso
            QMessageBox.information(self, "Inicio de sesión exitoso", f"Bienvenido, {nombre_usuario}.")
            # Aquí puedes redirigir al usuario a otra ventana o función según su nivel de acceso.
            self.close()  # Por ejemplo, cerrar el formulario de inicio de sesión
        else:
            operaciones_BD.mostrar_error("Nombre de usuario o contraseña incorrectos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernLoginForm()
    window.show()
    sys.exit(app.exec())

