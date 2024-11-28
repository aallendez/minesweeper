from collections import deque

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout, QPushButton, QMessageBox, QHBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

from start_game import generate_mines
from game_state_storage import GameStateManager
from Leaderboard import LeaderboardWidget  # Import LeaderboardWidget

CELL_SIZE = 60
GRID_WIDTH = 10
GRID_HEIGHT = 10

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Init Lives
        self.live_count = 3
        self.move_count = 0
        self.total_mines = 20  # Add this line to store total mines
        self.flags_placed = 0  # Add this line to track placed flags
        
        # Create a horizontal layout for the labels
        header_layout = QHBoxLayout()  # Add this line
        
        # Timer Label
        self.timer_label = QLabel("Time: 00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 16))
        header_layout.addWidget(self.timer_label)  # Change layout to header_layout
        
        # Add Mines Left Label
        self.mines_label = QLabel(f"Mines Left: {self.total_mines}")
        self.mines_label.setAlignment(Qt.AlignCenter)
        self.mines_label.setFont(QFont("Arial", 16))
        header_layout.addWidget(self.mines_label)  # Change layout to header_layout
        
        # Lives Label
        self.lives_label = QLabel(f"Lives: {self.live_count}")
        self.lives_label.setAlignment(Qt.AlignCenter)
        self.lives_label.setFont(QFont("Arial", 16))
        header_layout.addWidget(self.lives_label)  # Change layout to header_layout
        
        layout.addLayout(header_layout)  # Add the horizontal layout to the main layout
        
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
        
        # Load the game state manager
        self.state_manager = GameStateManager()
        
        # Start the game for the first time
        self.start_game()
        
        self.nickname = ""
        
        # Add reference to LeaderboardWidget
        self.leaderboard_widget = None  # Will be set from MinesweeperWindow
    
    def set_nickname(self, nickname):
        """
        Set the nickname
        Best Case: O(1) - Set the nickname
        Average Case: O(1) - Set the nickname
        Worst Case: O(1) - Set the nickname
        """
        self.nickname = nickname # O(1)
    
    def set_leaderboard_widget(self, leaderboard_widget):
        """
        Set reference to the leaderboard widget
        Best Case: O(1) - Set reference to the leaderboard widget
        Average Case: O(1) - Set reference to the leaderboard widget
        Worst Case: O(1) - Set reference to the leaderboard widget
        """
        self.leaderboard_widget = leaderboard_widget # O(1)
    
    def start_game(self):
        """
        Initialize or restart the game state.
        Best Case: O(1) - Initialize or restart the game state
        Average Case: O(1) - Initialize or restart the game state
        Worst Case: O(1) - Initialize or restart the game state
        """
        # Reset timer
        self.time_elapsed = 0 # O(1)
        self.timer_label.setText("Time: 00:00") # O(1)
        self.timer = QTimer(self) # O(1)
        self.timer.timeout.connect(self.update_timer) # O(1)
        
        # Reset the amount of mines left
        self.total_mines = 20 # O(1)
        self.mines_label.setText(f"Mines Left: {self.total_mines}")
        
        # Reset Lives
        self.live_count = 3 # O(1)
        self.lives_label.setText(f"Lives: {self.live_count}") # O(1)

        # Reset game state
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)] # O(width * height)
        self.cells = [] # O(1)
        self.first_click = True # O(1)

        # Clear and rebuild the grid layout
        grid_layout = self.grid_frame.layout()  # Get the existing layout
        grid_layout.setSpacing(1)  # No space between cells
        grid_layout.setContentsMargins(10, 10, 10, 10)  # No margin around the grid

        for i in reversed(range(grid_layout.count())): 
            widget = grid_layout.itemAt(i).widget() # O(1)
            if widget:
                widget.setParent(None) # O(1)

        for row in range(GRID_HEIGHT):
            row_cells = []
            for col in range(GRID_WIDTH):
                cell = QLabel() # O(1)
                cell.setFixedSize(CELL_SIZE, CELL_SIZE) # O(1)
                color = "#90EE90" if (row + col) % 2 == 0 else "#66CC66" # O(1)
                cell.setStyleSheet(f"background-color: {color}; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;") # O(1)
                
                # Make cells clickable
                cell.mousePressEvent = lambda e, r=row, c=col: self.handle_mouse_event(e, r, c) # O(1)
                
                grid_layout.addWidget(cell, row, col) # O(1)
                row_cells.append(cell) # O(1)
            self.cells.append(row_cells) # O(1)
            
        # Clear the game state history
        self.state_manager.clear_history() # O(1)

        # Hide the restart button
        self.restart_button.setVisible(False)
        print("Game started/restarted!")

    def update_timer(self):
        """Update the timer
        Best Case: O(1) - Simple timer update
        Average Case: O(1) - Simple timer update
        Worst Case: O(1) - Simple timer update
        """
        self.time_elapsed += 1
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f"Time: {minutes:02}:{seconds:02}")
        
    def handle_mouse_event(self, event, row, col):
        """Handle mouse events for cell clicks
        Best Case: O(1) - Simple flag toggle and counter update
        Average Case: O(1) - Simple flag toggle and counter update
        Worst Case: O(1) - Simple flag toggle and counter update
        """
        if event.button() == Qt.LeftButton:
            self.handle_click(row, col)
        elif event.button() == Qt.RightButton:
            self.handle_right_click(row, col)
        
    def handle_click(self, row, col):
        """Handle cell clicks
        Every Case: O(1) - one click, check if digged and check if it is mine (not taking 
        into account the time complexity of the functions called inside).
        """
        if self.first_click:
            self.first_click = False
            # Generate mines after first click
            self.grid = generate_mines(self.grid, row, col, self.total_mines)
            # Start the timer on first click
            self.timer.start(1000)
            
        # Increment move count
        self.move_count += 1
            
        # Prevent digging if the cell is flagged
        if self.cells[row][col].text() == "🚩":
            print("Cell is flagged, cannot dig.")
            return
        
        # Handle the click
        if self.grid[row][col] == 'M':
            self.state_manager.push_state(self.grid, self.cells)
            self.game_over()
        else:
            self.reveal_cell(row, col)
        
    def handle_right_click(self, row, col):
        """Handle right clicks
        Every Case: O(1) - one click, check if flagged and add or remove flag
        """
        print(f"Right clicked on cell ({row}, {col})")
        cell = self.cells[row][col]
        if cell.text() == "🚩":
            # Remove flag
            cell.setText("")
            self.flags_placed -= 1
            print(f"Unflagged cell ({row}, {col})")
        else:
            # Add flag
            cell.setText("🚩")
            self.flags_placed += 1
            print(f"Flagged cell ({row}, {col})")
        
        # Update mines left display
        self.mines_label.setText(f"Mines Left: {self.total_mines - self.flags_placed}")

    # Uses BFS to reveal cells
    def reveal_cell(self, start_row, start_col):
        """
        BFS implementation to reveal cells.
        
        Time Complexity Analysis:
        - Worst Case: O(N) where N is total number of cells (GRID_WIDTH * GRID_HEIGHT)
          Occurs when there are no mines and all cells need to be revealed
        - Average Case: O(K) where K is the number of connected safe cells
          Usually much smaller than N as mines break up the connected regions
        - Best Case: O(1) when clicking on a cell with adjacent mines
        
        Space Complexity: O(N) for visited set and queue
        
        Why BFS is optimal for this task:
        1. Guarantees shortest path exploration from start cell
        2. Reveals cells in a visually intuitive "wave-like" pattern
        3. More memory efficient than DFS for this case as stack depth
           could be large in DFS
        4. Prevents stack overflow that could occur with recursive DFS
           in large empty areas
        """
        
        # Store current game state
        self.state_manager.push_state(self.grid, self.cells)
        
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
        """Check if all non-mine cells have been revealed
        Complexity: O(N) where N is total grid size
        Must check every cell's state
        Worst Case: O(N) - Must check every cell
        """
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
        """
        Count adjacent mines for a cell
        Complexity: O(1 * n) - Always checks exactly 8 adjacent cells where n is 8
        Worst Case: O(1 * n) - Always checks exactly 8 adjacent cells where n is 8
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < GRID_HEIGHT and 
                    0 <= new_col < GRID_WIDTH and 
                    self.grid[new_row][new_col] == 'M'):
                    count += 1
        return count
        
    def undo_last_move(self):
        """Restore previous game state
        Complexity: O(N) where N is grid size (height * width)
        Must restore state of every cell
        Worst Case: O(N) - Must restore state of every cell (height * width)
        """
        previous_state = self.state_manager.pop_state()
        if previous_state:
            # Restore gird
            self.grid = previous_state.grid
            
            for row in range(GRID_HEIGHT):
                for col in range(GRID_WIDTH):
                    saved_cell = previous_state.cells_state[row][col]
                    self.cells[row][col].setText(saved_cell['text'])
                    self.cells[row][col].setStyleSheet(saved_cell['style'])
                    self.cells[row][col].setEnabled(True)
                    
        # Resume timer
        self.timer.start(1000)
        
    def game_over(self):
        """Handle game over state
        Best Case: O(1) - Only one mine remains to be revealed
        Average Case: O(height * width) - Reveal all mines and disable all cells
        Worst Case: O(height * width) - Reveal all mines and disable all cells
        """
        # Reveal all mines
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 'M':
                    self.cells[row][col].setStyleSheet("background-color: red; border: 1px solid black; text-align: center; font-size: 24px; display: flex; padding-left: 17px;")
                    self.cells[row][col].setText("💣")
        
        # Stop the timer
        self.timer.stop()
        
        if self.live_count > 0 and not self.first_click and self.move_count > 2:
            # Ask player if they want to save the game state
            reply = QMessageBox.question(self, "Oops! You stepped in the wrong place", "Would you like to undo your last move?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Restore previous game state and decrement lives
                self.live_count -= 1
                self.lives_label.setText(f"Lives: {self.live_count}")
                self.undo_last_move()
            else:
                # Disable further clicks on cells
                for row in self.cells:
                    for cell in row:
                        cell.setEnabled(False)  # Disable the cell
                # Show the restart button
                self.restart_button.setVisible(True)
        else:
            # Disable further clicks on cells
            for row in self.cells:
                for cell in row:
                    cell.setEnabled(False)  # Disable the cell
            # Show the restart button
            self.restart_button.setVisible(True)
        
    def game_won(self):
        """Handle game won state
        Complexity: O(height * width) where height and width are grid size
        Must flag all mines and disable all cells
        Worst Case: O(height * width) - Must flag all mines and disable all cells
        """
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
        
        # Update leaderboard
        print(f"Leaderboard Widget: {self.leaderboard_widget}, Nickname: {self.nickname}")
        if self.leaderboard_widget and self.nickname:
            time_taken = self.time_elapsed
            print(f"Writing to leaderboard: {self.nickname}, Time: {time_taken}")
            self.leaderboard_widget.write_to_leaderboard_csv(self.nickname, time_taken)
            self.leaderboard_widget.load_and_display_leaderboard()
