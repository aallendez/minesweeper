from Rules import RulesWidget
from Leaderboard import LeaderboardWidget
from Start_Screen import StartScreenWidget
from game import GameWidget

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Menu buttons in horizontal layout
        menu_layout = QHBoxLayout()  # Horizontal layout for menu

        # Adding spacers for centering
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        game_btn = QPushButton("Game")
        leaderboard_btn = QPushButton("Leaderboard")
        rules_btn = QPushButton("Rules")
        
        for btn in [game_btn, leaderboard_btn, rules_btn]:
            btn.setFixedHeight(40)
            btn.setStyleSheet("font-size: 14px; padding: 5px 15px;")  # Style the buttons
            menu_layout.addWidget(btn)
        
        # Add a spacer on the right to center the buttons
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Create the start screen
        self.start_screen = StartScreenWidget(self.start_game)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.start_screen)

        # Create game widget and other widgets
        self.game_widget = GameWidget()
        self.leaderboard_widget = LeaderboardWidget()
        self.rules_widget = RulesWidget()

        self.stacked_widget.addWidget(self.game_widget)
        self.stacked_widget.addWidget(self.leaderboard_widget)
        self.stacked_widget.addWidget(self.rules_widget)
        
        # Connect buttons
        game_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.game_widget))
        leaderboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.leaderboard_widget))
        rules_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.rules_widget))
        
        # Add menu layout to the main layout
        main_layout.addLayout(menu_layout)

        # Add stacked widget to main layout
        main_layout.addWidget(self.stacked_widget)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def start_game(self):
        nickname = self.start_screen.nickname_input.text()
        if nickname:
            print(f"Starting game for {nickname}!")  # You can use this nickname in your game logic
            self.stacked_widget.setCurrentWidget(self.game_widget)
        else:
            print("Please enter a nickname.")
