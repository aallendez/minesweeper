from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class LeaderboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        header_label = QLabel("Leaderboard")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)

        players = ["Player1: 50s", "Player2: 65s", "Player3: 80s"]
        for player in players:
            player_label = QLabel(player)
            player_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(player_label)
            
        self.setLayout(layout)
