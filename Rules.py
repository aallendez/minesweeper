from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class RulesWidget(QWidget):
    def __init__(self):
        """
        Initialize the RulesWidget
        Best Case: O(1) - Initialize the RulesWidget
        Average Case: O(1) - Initialize the RulesWidget
        Worst Case: O(1) - Initialize the RulesWidget
        """
        super().__init__()

        # Set up main layout
        layout = QVBoxLayout()  # O(1) 
        layout.setSpacing(10)  # O(1) 
        self.setLayout(layout)  # O(1) 

        # Header label
        header_label = QLabel("Rules of Minesweeper")  # O(1) 
        header_label.setFont(QFont("Arial", 24, QFont.Bold))  # O(1) 
        header_label.setAlignment(Qt.AlignCenter)  # O(1) 
        layout.addWidget(header_label)  # O(1) 

        # Rules list
        rules = [  # O(1) 
            "1. The game is played on a grid of cells.",
            "2. Some cells contain mines, while others are safe.",
            "3. Your goal is to uncover all safe cells.",
            "4. If you uncover a cell with a mine, you lose the game.",
            "5. Uncover all safe cells to win!"
        ]
        
        rules_text = QLabel("\n\n".join(rules))  # O(n) where n is the number of rules - Joining the rules into a single string
        rules_text.setFont(QFont("Arial", 16))  # O(1) 
        rules_text.setAlignment(Qt.AlignLeft)  # O(1) 
        rules_text.setWordWrap(True)  # O(1) 
        rules_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)  # O(1) 
        rules_text.setStyleSheet("background-color: #4DAA4D; margin-top: 10px; font-weight: bold; padding: 20px 10px; border-radius: 10px;")  # O(1) 
        layout.addWidget(rules_text)  # O(1) 

        # Add stretch after the rules to push everything to the top
        layout.addStretch()  # O(1) 