from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont

from connection import registrar_usuario
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "eco_icon.ico")


class Register(QWidget):
    registration_successful = Signal()
    go_to_login = Signal()

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

        titulo = QLabel("♻")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 40, QFont.Bold))
        main_layout.addWidget(titulo)

        title_label = QLabel("Registrar Usuário")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        main_layout.addWidget(title_label)

        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(25, 0, 25, 0)
        form_layout.setSpacing(10)

        nome_label = QLabel("Nome:")
        nome_label.setFont(QFont("Arial", 14))
        self.nome_entry = QLineEdit()
        self.nome_entry.setPlaceholderText("Seu nome completo")
        self.nome_entry.setFont(QFont("Arial", 12))
        self.nome_entry.setMinimumWidth(250) 
        form_layout.addWidget(nome_label)
        form_layout.addWidget(self.nome_entry)

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

        register_button = QPushButton("Registrar")
        register_button.setFont(QFont("Arial", 16, QFont.Bold))
        register_button.clicked.connect(self.button_register)
        main_layout.addWidget(register_button, alignment=Qt.AlignCenter)

        login_button = QPushButton("Logar")
        login_button.setFont(QFont("Arial", 12, QFont.Bold))
        login_button.setStyleSheet("QPushButton { background-color: transparent; border: none; color: #4CAF50; } QPushButton:hover { text-decoration: underline; }")
        login_button.clicked.connect(self.abrir_login)
        main_layout.addWidget(login_button, alignment=Qt.AlignCenter)

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
                padding: 10px; /* Padding ajustado */
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

    def button_register(self):
        nome = self.nome_entry.text()
        email = self.email_entry.text()
        senha = self.senha_entry.text()

        if not nome or not email or not senha:
            QMessageBox.warning(self, "Campos vazios", "Por favor, preencha todos os campos.")
            return

        sucesso = registrar_usuario(nome, email, senha)
        if sucesso:
            QMessageBox.information(self, "Sucesso", "Usuário registrado com sucesso!")
            self.registration_successful.emit()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao registrar. O e-mail já pode estar cadastrado.")

    def abrir_login(self):
        self.go_to_login.emit()