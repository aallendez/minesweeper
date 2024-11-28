from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class StartScreenWidget(QWidget):
    def __init__(self, start_game_callback):
        """
            Initialize the start screen widget.
            O(1) all the time. Since you are only initializing the widget.
        """
        super().__init__()

        # Set up main layout
        layout = QVBoxLayout()  # O(1)
        layout.setAlignment(Qt.AlignCenter)  # O(1)
        layout.setSpacing(20)  # O(1)

        # Green welcome label
        welcome_label = QLabel("Welcome to Minesweeper!")  # O(1)
        welcome_label.setFont(QFont("Arial", 24, QFont.Bold))  # O(1)
        welcome_label.setAlignment(Qt.AlignCenter)  # O(1)
        welcome_label.setStyleSheet("color: #28a745; background: transparent;")  # O(1)
        layout.addWidget(welcome_label, alignment=Qt.AlignCenter)  # O(1)

        # Nickname input
        self.nickname_input = QLineEdit()  # O(1)
        self.nickname_input.setPlaceholderText("Enter your nickname")  # O(1)
        self.nickname_input.setFixedWidth(300)  # O(1)
        self.nickname_input.setFixedHeight(40)  # O(1)
        self.nickname_input.setStyleSheet(
            """
            QLineEdit {
                padding: 5px;  
                font-size: 16px;  
                border: 2px solid #ccc;  
                border-radius: 10px;  
                background: transparent;  
            }
            QLineEdit:focus {
                border-color: #28a745;  
                outline: none;  
            }
            """
        )
        self.nickname_input.textChanged.connect(self.enable_start_button)  # O(1)
        layout.addWidget(self.nickname_input, alignment=Qt.AlignCenter)  # O(1)

        # Start game button
        self.start_button = QPushButton("Start Game")  # O(1)
        self.start_button.setFixedWidth(200)  # O(1)
        self.start_button.setFixedHeight(50)  # O(1)
        self.start_button.setFont(QFont("Arial", 14))  # O(1)
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: #28a745;  
                color: white;  
                border-radius: 10px;  
            }
            QPushButton:hover {
                background-color: #218838;  
            }
            QPushButton:pressed {
                background-color: #1e7e34;  
            }
            QPushButton:disabled {
                background-color: #ccc;  
                color: #666;  
            }
            """
        )
        self.start_button.setEnabled(False)  # O(1)
        self.start_button.clicked.connect(start_game_callback)  # O(1)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)  # O(1)

        # Set main layout
        self.setLayout(layout)  # O(1)
        self.setStyleSheet("background-color: #f0f0f0;")  # O(1)

    def enable_start_button(self):
        """
            Enable start button only when nickname is entered.
            O(n) where n is the length of the input text.
        """
        if self.nickname_input.text().strip():  # O(n) where n is the length of the input text
            self.start_button.setEnabled(True)  # O(1)
        else:
            self.start_button.setEnabled(False)  # O(1)
