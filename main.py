import sys
from PySide6.QtWidgets import QApplication, QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox 
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, Slot 

# classes de UI reescritas em PySide6
from login import Login
from register import Register
from sistema import Sistema
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "eco_icon.ico")


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eco-vida Sustentabilidade")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Erro: Ícone não encontrado em {icon_path}. Usando ícone padrão.")
            
            self.setWindowIcon(QIcon()) 
        self.setFixedSize(600, 490) 

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignCenter)

        # Título da tela inicial
        self.title_label = QLabel("♻")
        self.title_label.setFont(QFont("Arial", 40, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.welcome_label = QLabel("Seja bem-vindo(a) ao Eco-vida!")
        self.welcome_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.welcome_label)

        # Botão para abrir o registro/login
        self.enter_button = QPushButton("Entrar")
        self.enter_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.enter_button.setStyleSheet("""
            QPushButton {
                background-color: #2D6A4F;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 25px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2D6A4F; /* Mesmo hover para consistência */
            }
        """)
        self.enter_button.clicked.connect(self.show_auth_screens)
        self.layout.addWidget(self.enter_button, alignment=Qt.AlignCenter)

        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)
        self.stacked_widget.hide() 

        self.setup_auth_screens()
        self.apply_qss() 

    def apply_qss(self):
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b; /* Dark background */
                color: #ffffff; /* White text */
                font-family: 'Segoe UI', 'Arial';
            }
            QLabel {
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #4CAF50; /* Green */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 25px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #3e8e41; /* Even darker on press */
            }
        """)

    def setup_auth_screens(self):
        
        self.login_screen = Login(self)
        self.register_screen = Register(self)

        self.stacked_widget.addWidget(self.login_screen)    
        self.stacked_widget.addWidget(self.register_screen) 

        # Conectar sinais das telas
        self.login_screen.login_successful.connect(self.show_sistema_screen)
        self.login_screen.go_to_register.connect(self.show_register_screen)
        self.register_screen.registration_successful.connect(self.show_login_screen_after_register)
        self.register_screen.go_to_login.connect(self.show_login_screen)

        self.sistema_screen = None 


    def show_auth_screens(self):
        
        self.title_label.hide()
        self.welcome_label.hide()
        self.enter_button.hide()
        self.stacked_widget.show()

        
        self.setFixedSize(self.login_screen.size())
        self.stacked_widget.setCurrentWidget(self.login_screen) 

    @Slot(int)
    def show_sistema_screen(self, user_id):
        
        self.stacked_widget.hide()

       
        if self.sistema_screen is not None:
            self.sistema_screen.close() 
            self.sistema_screen.deleteLater() 

        self.sistema_screen = Sistema(user_id, self)
        self.sistema_screen.logout_successful.connect(self.show_login_screen_after_logout)
        self.sistema_screen.show() 

        self.hide() 


    @Slot()
    def show_login_screen(self):
        self.setFixedSize(self.login_screen.size())
        self.stacked_widget.setCurrentWidget(self.login_screen)
        
        self.login_screen.senha_entry.clear()


    @Slot()
    def show_register_screen(self):
        self.setFixedSize(self.register_screen.size())
        self.stacked_widget.setCurrentWidget(self.register_screen)
        
        self.register_screen.nome_entry.clear()
        self.register_screen.email_entry.clear()
        self.register_screen.senha_entry.clear()


    @Slot()
    def show_login_screen_after_register(self):
        QMessageBox.information(self, "Registro Concluído", "Seu cadastro foi realizado com sucesso! Faça login para continuar.")
        self.show_login_screen()


    @Slot()
    def show_login_screen_after_logout(self):
        
        self.show()
        self.stacked_widget.show() 
        self.show_login_screen() 
        self.setFixedSize(self.login_screen.size())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show() 
    sys.exit(app.exec())