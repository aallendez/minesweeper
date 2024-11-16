""" 
    MINESWEEPER GAME
    
    Algorithms:
        - BFS for placing mines in the grid
        - Quicksort for sorting the leaderboard
        - Hashmap for the milestones and benchmarks (medallas)
        
    Data Structures:
        - 2D matrix for the grid
        - List for the leaderboard
        - Queue for the BFS ???
    
    Optional:
        - Dijkstra for finding the shortest path to the nearest mine
"""
import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from start_game import generate_mines

CELL_SIZE = 60
GRID_WIDTH = 10
GRID_HEIGHT = 10

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, 
    QHBoxLayout, QFrame, QPushButton, QStackedWidget
)

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Header
        header_label = QLabel("Minesweeper")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(header_label)
        
        # Timer Label
        self.time_elapsed = 0  # Store elapsed time in seconds
        self.timer_label = QLabel("Time: 00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 16))
        layout.addWidget(self.timer_label)

        # Start the timer
        print("Starting timer")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Update every second

        # Initialize game state
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.cells = []  # Store QLabel references
        self.first_click = True
        
        # Game grid
        grid_frame = QFrame()
        grid_layout = QGridLayout(grid_frame)
        grid_layout.setSpacing(0)

        for row in range(GRID_HEIGHT):
            row_cells = []
            for col in range(GRID_WIDTH):
                cell = QLabel()
                cell.setFixedSize(CELL_SIZE, CELL_SIZE)
                color = "#90EE90" if (row + col) % 2 == 0 else "#66CC66"
                cell.setStyleSheet(f"background-color: {color}; border: 1px solid black;")
                
                # Make cells clickable
                cell.mousePressEvent = lambda e, r=row, c=col: self.handle_click(r, c)
                
                grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)
        
        layout.addWidget(grid_frame, alignment=Qt.AlignCenter)
        self.setLayout(layout)
    
    def update_timer(self):
        self.time_elapsed += 1
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f"Time: {minutes:02}:{seconds:02}")
        
    def handle_click(self, row, col):
        """Handle cell clicks"""
        if self.first_click:
            self.first_click = False
            # Generate mines after first click
            self.grid = generate_mines(self.grid, row, col)
            # Start the timer on first click
            self.timer.start(1000)
        
        # Handle the click
        if self.grid[row][col] == 'M':
            self.game_over()
        else:
            self.reveal_cell(row, col)
        
    def reveal_cell(self, row, col, visited=None):
        # Reveal the contents of a cell and handle cascading empty cells.
        if visited is None:
            visited = set()
            
        # Skip if the cell has already been visited
        if (row, col) in visited:
            return
        visited.add((row, col))
        
        cell = self.cells[row][col]
        if self.grid[row][col] == 'M':
            cell.setStyleSheet("background-color: red; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")
            cell.setText("💣")
        else:
            # Calculate number of adjacent mines
            mine_count = self.count_adjacent_mines(row, col)
            cell.setText(str(mine_count) if mine_count > 0 else "")
            cell.setStyleSheet("background-color: #ccc; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")
            
            # If there are no adjacent mines, reveal adjacent cells
            if mine_count == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue  # Skip the current cell
                        
                        new_row, new_col = row + dx, col + dy
                        if (0 <= new_row < GRID_HEIGHT and 
                            0 <= new_col < GRID_WIDTH):
                            self.reveal_cell(new_row, new_col, visited)  # Pass the visited set

        
    def count_adjacent_mines(self, row, col):
        """Count adjacent mines for a cell"""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < GRID_HEIGHT and 
                    0 <= new_col < GRID_WIDTH and 
                    self.grid[new_row][new_col] == 'M'):
                    count += 1
        return count
        
    def game_over(self):
        """Handle game over state"""
        # Reveal all mines
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 'M':
                    self.cells[row][col].setStyleSheet("background-color: red; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")
                    self.cells[row][col].setText("💣")
        
        # Stop the timer
        self.timer.stop()
        
    def game_won(self):
        """Handle game won state"""
        # Stop the timer
        self.timer.stop()

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

class MilestonesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        header_label = QLabel("Milestones")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)
        
        # Add your milestones content here
        self.setLayout(layout)

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()  # Vertical layout for main stacking

        # Menu buttons in horizontal layout
        menu_layout = QHBoxLayout()  # Horizontal layout for menu

        # Adding spacers for centering
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        game_btn = QPushButton("Game")
        leaderboard_btn = QPushButton("Leaderboard")
        milestones_btn = QPushButton("Milestones")

        for btn in [game_btn, leaderboard_btn, milestones_btn]:
            btn.setFixedHeight(40)
            btn.setStyleSheet("font-size: 14px; padding: 5px 15px;")  # Style the buttons
            menu_layout.addWidget(btn)
        
        # Add a spacer on the right to center the buttons
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        self.game_widget = GameWidget()
        self.leaderboard_widget = LeaderboardWidget()
        self.milestones_widget = MilestonesWidget()

        self.stacked_widget.addWidget(self.game_widget)
        self.stacked_widget.addWidget(self.leaderboard_widget)
        self.stacked_widget.addWidget(self.milestones_widget)

        # Connect buttons
        game_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.game_widget))
        leaderboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.leaderboard_widget))
        milestones_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.milestones_widget))

        # Add layouts to main layout
        main_layout.addLayout(menu_layout)
        main_layout.addWidget(self.stacked_widget)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinesweeperWindow()  # Changed from LeaderboardWidget to MinesweeperWindow
    window.show()
    sys.exit(app.exec())