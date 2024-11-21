from collections import deque

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout, QPushButton
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

from start_game import generate_mines

CELL_SIZE = 60
GRID_WIDTH = 10
GRID_HEIGHT = 10

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
        self.timer_label = QLabel("Time: 00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 16))
        layout.addWidget(self.timer_label)
        
        # Game grid frame
        self.grid_frame = QFrame()
        self.grid_frame.setLayout(QGridLayout())  # Initialize an empty layout
        layout.addWidget(self.grid_frame, alignment=Qt.AlignCenter)
        
        # "Start Again" button
        self.restart_button = QPushButton("Start Again")
        self.restart_button.clicked.connect(self.start_game)
        self.restart_button.setVisible(False)  # Initially hidden
        layout.addWidget(self.restart_button)
        
        self.setLayout(layout)
        
        # Start the game for the first time
        self.start_game()
    
    def start_game(self):
        """Initialize or restart the game state."""
        # Reset timer
        self.time_elapsed = 0
        self.timer_label.setText("Time: 00:00")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        # Reset game state
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.cells = []
        self.first_click = True

        # Clear and rebuild the grid layout
        grid_layout = self.grid_frame.layout()  # Get the existing layout
        grid_layout.setSpacing(1)  # No space between cells
        grid_layout.setContentsMargins(10, 10, 10, 10)  # No margin around the grid

        for i in reversed(range(grid_layout.count())): 
            widget = grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for row in range(GRID_HEIGHT):
            row_cells = []
            for col in range(GRID_WIDTH):
                cell = QLabel()
                cell.setFixedSize(CELL_SIZE, CELL_SIZE)
                color = "#90EE90" if (row + col) % 2 == 0 else "#66CC66"
                cell.setStyleSheet(f"background-color: {color}; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")
                
                # Make cells clickable
                cell.mousePressEvent = lambda e, r=row, c=col: self.handle_mouse_event(e, r, c)
                
                grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Hide the restart button
        self.restart_button.setVisible(False)
        print("Game started/restarted!")

    def update_timer(self):
        self.time_elapsed += 1
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f"Time: {minutes:02}:{seconds:02}")
        
    def handle_mouse_event(self, event, row, col):
        """Handle mouse events for cell clicks"""
        if event.button() == Qt.LeftButton:
            self.handle_click(row, col)
        elif event.button() == Qt.RightButton:
            self.handle_right_click(row, col)
        
    def handle_click(self, row, col):
        """Handle cell clicks"""
        if self.first_click:
            self.first_click = False
            # Generate mines after first click
            self.grid = generate_mines(self.grid, row, col)
            # Start the timer on first click
            self.timer.start(1000)
            
        # Prevent digging if the cell is flagged
        if self.cells[row][col].text() == "🚩":
            print("Cell is flagged, cannot dig.")
            return
        
        # Handle the click
        if self.grid[row][col] == 'M':
            self.game_over()
        else:
            self.reveal_cell(row, col)
        
    def handle_right_click(self, row, col):
        """Handle right clicks"""
        print(f"Right clicked on cell ({row}, {col})")
        cell = self.cells[row][col]
        if cell.text() == "🚩":
            # Remove flag
            cell.setText("")
            print(f"Unflagged cell ({row}, {col})")
        else:
            # Add flag
            cell.setText("🚩")
            print(f"Flagged cell ({row}, {col})")

    def reveal_cell(self, start_row, start_col):
        """
        Reveal the contents of a cell and cascade to safe neighbors using BFS
        until unsafe cells (cells with adjacent mines) are reached.
        """
        visited = set()
        queue = deque([(start_row, start_col)])  # Start BFS from the clicked cell

        while queue:
            row, col = queue.popleft()

            # Skip if the cell is already visited
            if (row, col) in visited:
                continue
            visited.add((row, col))

            cell = self.cells[row][col]

            # Skip flagged cells
            if cell.text() == "🚩":
                continue

            # Count adjacent mines
            mine_count = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < GRID_HEIGHT and 0 <= new_col < GRID_WIDTH and
                    self.grid[new_row][new_col] == 'M'):
                    mine_count += 1

            # Update the cell display
            cell.setText(str(mine_count) if mine_count > 0 else "")
            cell.setStyleSheet("background-color: #ccc; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")

            # If the cell has adjacent mines, stop expanding
            if mine_count > 0:
                continue

            # If no adjacent mines, enqueue all neighbors
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < GRID_HEIGHT and 0 <= new_col < GRID_WIDTH and
                    (new_row, new_col) not in visited):
                    queue.append((new_row, new_col))

        # Check for win condition
        self.check_win()

    def check_win(self):
        """Check if all non-mine cells have been revealed"""
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell = self.cells[row][col]
                # If cell is not revealed (still green) and not a mine, game isn't won yet
                if (self.grid[row][col] != 'M' and 
                    ("#90EE90" in cell.styleSheet() or "#66CC66" in cell.styleSheet())):
                    return
        
        # If we get here, all non-mine cells are revealed
        self.game_won()

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
        
        # Disable further clicks on cells
        for row in self.cells:
            for cell in row:
                cell.setEnabled(False)  # Disable the cell

        # Show the restart button
        self.restart_button.setVisible(True)
        
    def game_won(self):
        """Handle game won state"""
        # Stop the timer
        self.timer.stop()
        
        # Flag all mines
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 'M':
                    self.cells[row][col].setText("🚩")
        
        # Disable further clicks on cells
        for row in self.cells:
            for cell in row:
                cell.setEnabled(False)
        
        # Show the restart button
        self.restart_button.setVisible(True)