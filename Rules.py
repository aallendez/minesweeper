from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class RulesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.setLayout(layout)
        
        # Header label
        header_label = QLabel("Rules of Minesweeper")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)
        
        # Rules list
        rules = [
            "1. The game is played on a grid of cells.",
            "2. Some cells contain mines, while others are safe.",
            "3. Your goal is to uncover all safe cells.",
            "4. If you uncover a cell with a mine, you lose the game.",
            "5. Uncover all safe cells to win!"
        ]
        
        rules_text = QLabel("\n\n".join(rules))
        rules_text.setFont(QFont("Arial", 16))
        rules_text.setAlignment(Qt.AlignLeft)
        rules_text.setWordWrap(True)
        rules_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        rules_text.setStyleSheet("background-color: #4DAA4D; margin-top: 10px; font-weight: bold; padding: 20px 10px; border-radius: 10px;")
        layout.addWidget(rules_text)
        
        # Add stretch after the rules to push everything to the top
        layout.addStretch()
