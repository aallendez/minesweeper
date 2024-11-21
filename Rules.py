from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class RulesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Header label
        header_label = QLabel("Rules of Minesweeper")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)
        
        # Rules text
        rules_text = QTextEdit()
        rules_text.setText("""
        1. The game is played on a grid of cells.
        2. Some cells contain mines, and others don't.
        3. The goal is to uncover all cells that don't contain mines.
        4. If you uncover a cell with a mine, you lose.
        5. If you uncover all cells without mines, you win.
        """)
        rules_text.setReadOnly(True)  # Make the text non-editable
        rules_text.setFont(QFont("Arial", 14))
        layout.addWidget(rules_text)
