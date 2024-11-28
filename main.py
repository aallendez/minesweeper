""" 
    MINESWEEPER GAME
    
    Algorithms:
        - BFS for placing mines in the grid and revealing cells (worst case O(n))
        - Mergesort for sorting the leaderboard
        
    Data Structures:
        - 2D matrix for the grid
        - Stack for the game state history
"""
import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from start_game import generate_mines
from collections import deque

# Import Our Own Functions and Classes
from Leaderboard import LeaderboardWidget
from Rules import RulesWidget
from Start_Screen import StartScreenWidget
from game import GameWidget

CELL_SIZE = 60
GRID_WIDTH = 10
GRID_HEIGHT = 10

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, 
    QHBoxLayout, QFrame, QPushButton, QStackedWidget, QTextEdit, QLineEdit
)

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the MinesweeperWindow
        Best Case: O(1) - Initialize the MinesweeperWindow
        Average Case: O(1) - Initialize the MinesweeperWindow
        Worst Case: O(1) - Initialize the MinesweeperWindow
        """
        super().__init__()
        self.setWindowTitle("Minesweeper")  # O(1)
        self.setGeometry(100, 100, 800, 600)  # O(1)

        # Main widget and layout
        main_widget = QWidget()  # O(1)
        main_layout = QVBoxLayout()  # O(1)
        
        # Menu buttons in horizontal layout
        menu_layout = QHBoxLayout()  # O(1)

        # Adding spacers for centering
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))  # O(1)

        self.game_btn = QPushButton("Game")  # O(1)
        leaderboard_btn = QPushButton("Leaderboard")  # O(1)
        rules_btn = QPushButton("Rules")  # O(1)
        
        # Initially hide the game button
        self.game_btn.hide()  # O(1)
        
        for btn in [self.game_btn, leaderboard_btn, rules_btn]:  # O(3) - Iterating through 3 buttons
            btn.setFixedHeight(40)  # O(1)
            btn.setStyleSheet("font-size: 14px; padding: 5px 15px;")  # O(1)
            menu_layout.addWidget(btn)  # O(1)
        
        # Add a spacer on the right to center the buttons
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))  # O(1)

        # Create the start screen
        self.start_screen = StartScreenWidget(self.start_game)  # O(1)
        self.stacked_widget = QStackedWidget()  # O(1)
        self.stacked_widget.addWidget(self.start_screen)  # O(1)

        # Create game widget and other widgets
        self.game_widget = GameWidget()  # O(1)
        self.leaderboard_widget = LeaderboardWidget()  # O(1)
        self.rules_widget = RulesWidget()  # O(1)

        self.stacked_widget.addWidget(self.game_widget)  # O(1)
        self.stacked_widget.addWidget(self.leaderboard_widget)  # O(1)
        self.stacked_widget.addWidget(self.rules_widget)  # O(1)
        
        # Connect buttons
        self.game_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.game_widget))  # O(1)
        leaderboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.leaderboard_widget))  # O(1)
        rules_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.rules_widget))  # O(1)
        
        # Add menu layout to the main layout
        main_layout.addLayout(menu_layout)  # O(1)

        # Add stacked widget to main layout
        main_layout.addWidget(self.stacked_widget)  # O(1)
        main_widget.setLayout(main_layout)  # O(1)
        self.setCentralWidget(main_widget)  # O(1)
        
        # Connect game widget to leaderboard
        self.game_widget.set_leaderboard_widget(self.leaderboard_widget)  # O(1)

    def start_game(self):
        """Start the game
        Best Case: O(1) - Start the game
        Average Case: O(1) - Start the game
        Worst Case: O(1) - Start the game
        """
        nickname = self.start_screen.nickname_input.text()  # O(1)
        if nickname:  # O(1)
            self.game_widget.set_nickname(nickname)  # O(1)
            print(f"Starting game for {nickname}!")  # O(1)
            self.stacked_widget.setCurrentWidget(self.game_widget)  # O(1)
            self.game_btn.show()  # O(1)
        else:  # O(1)
            print("Please enter a nickname.")  # O(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinesweeperWindow()
    window.show()
    sys.exit(app.exec())

