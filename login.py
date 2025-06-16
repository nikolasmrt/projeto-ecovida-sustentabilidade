from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont

from connection import verificar_login


import os

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "eco_icon.ico")


class Login(QWidget):
    login_successful = Signal(int)
    go_to_register = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Erro: Ícone não encontrado em {icon_path}. Usando ícone padrão.")
            
            self.setWindowIcon(QIcon()) 
        self.setFixedSize(640, 640)

        self.setup_ui()
        self.apply_qss()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(15)

        logo_label = QLabel("♻")
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setFont(QFont("Arial", 40, QFont.Bold))
        main_layout.addWidget(logo_label)

        title_label = QLabel("Login")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        main_layout.addWidget(title_label)

        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(25, 0, 25, 0)
        form_layout.setSpacing(10)

        email_label = QLabel("E-mail:")
        email_label.setFont(QFont("Arial", 14))
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("seu.email@exemplo.com")
        self.email_entry.setFont(QFont("Arial", 12))
        self.email_entry.setMinimumWidth(250)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_entry)

        password_label = QLabel("Senha:")
        password_label.setFont(QFont("Arial", 14))
        self.senha_entry = QLineEdit()
        self.senha_entry.setEchoMode(QLineEdit.Password)
        self.senha_entry.setPlaceholderText("********")
        self.senha_entry.setFont(QFont("Arial", 12))
        self.senha_entry.setMinimumWidth(250)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.senha_entry)

        main_layout.addLayout(form_layout)

        login_button = QPushButton("Logar")
        login_button.setFont(QFont("Arial", 16, QFont.Bold))
        login_button.clicked.connect(self.login)
        main_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        register_link_layout = QHBoxLayout()
        register_link_layout.addStretch()
        register_label = QLabel("Não tem conta?")
        register_label.setFont(QFont("Arial", 10))
        register_link = QPushButton("Crie uma aqui!")
        register_link.setFont(QFont("Arial", 10, QFont.Bold))
        
        register_link.setStyleSheet("QPushButton { border: none; color: white; } QPushButton:hover { text-decoration: underline; }")
        register_link.clicked.connect(self.abrir_registro)
        register_link_layout.addWidget(register_label)
        register_link_layout.addWidget(register_link)
        register_link_layout.addStretch()
        main_layout.addLayout(register_link_layout)


    def apply_qss(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-family: 'Segoe UI', 'Arial';
            }
            QLabel {
                color: #e0e0e0;
            }
            QLineEdit {
                background-color: #3c3c3c;
                border: 1px solid #555555;
                border-radius: 8px;
                padding: 10px;
                color: #ffffff;
                selection-background-color: #4CAF50;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 25px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    def login(self):
        email = self.email_entry.text()
        senha = self.senha_entry.text()

        if not email or not senha:
            QMessageBox.warning(self, "Campos vazios", "Por favor, preencha todos os campos.")
            return

        usuario_id = verificar_login(email, senha)

        if usuario_id:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            self.login_successful.emit(usuario_id)
        else:
            QMessageBox.critical(self, "Erro", "Credenciais inválidas.")

    def abrir_registro(self):
        self.go_to_register.emit()