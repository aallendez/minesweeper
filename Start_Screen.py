from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class StartScreenWidget(QWidget):
    def __init__(self, start_game_callback):
        super().__init__()
        layout = QVBoxLayout()

        # Header label
        header_label = QLabel("Welcome to Minesweeper!")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)

        # Nickname input
        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("Enter your nickname")
        layout.addWidget(self.nickname_input)

        # Start game button
        start_button = QPushButton("Start Game")
        start_button.clicked.connect(start_game_callback)
        layout.addWidget(start_button)

        self.setLayout(layout)
