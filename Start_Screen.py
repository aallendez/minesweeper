from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class StartScreenWidget(QWidget):
    def __init__(self, start_game_callback):
        super().__init__()

        # Set up main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center all elements
        layout.setSpacing(20)  # Add spacing between elements

        # Green welcome label
        welcome_label = QLabel("Welcome to Minesweeper!")
        welcome_label.setFont(QFont("Arial", 24, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("color: #28a745; background: transparent;")  # Green text, transparent background
        layout.addWidget(welcome_label, alignment=Qt.AlignCenter)  # Center the label

        # Nickname input
        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("Enter your nickname")
        self.nickname_input.setFixedWidth(300)  # Adjust width
        self.nickname_input.setFixedHeight(40)  # Adjust height
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
                border-color: #28a745;  /* Green border on focus */
                outline: none;
            }
            """
        )
        self.nickname_input.textChanged.connect(self.enable_start_button)
        layout.addWidget(self.nickname_input, alignment=Qt.AlignCenter)  # Center the input field

        # Start game button
        self.start_button = QPushButton("Start Game")
        self.start_button.setFixedWidth(200)
        self.start_button.setFixedHeight(50)
        self.start_button.setFont(QFont("Arial", 14))
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: #28a745;  /* Green background */
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
        self.start_button.setEnabled(False)  # Initially disabled
        self.start_button.clicked.connect(start_game_callback)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)  # Center the button

        # Set main layout
        self.setLayout(layout)
        self.setStyleSheet("background-color: #f0f0f0;")  # Light background color

    def enable_start_button(self):
        """Enable start button only when nickname is entered."""
        if self.nickname_input.text().strip():
            self.start_button.setEnabled(True)
        else:
            self.start_button.setEnabled(False)
