class GameState:
    def __init__(self, grid, cells_state):
        """
        Initialize the GameState
        Best Case: O(height * width) - Copying the grid
        Average Case: O(height * width) - Copying the grid
        Worst Case: O(height * width) - Copying the grid
        """
        self.grid = [row[:] for row in grid]  # O(height * width) 
        self.cells_state = []  # O(1) 
        
        # Store relevant cell information (text and style) O (rows * cells)
        for row in cells_state:  # O(m) where m is the number of rows in cells_state
            cell_row = []  # O(1) 
            for cell in row:  # O(n) where n is the number of cells in each row
                cell_row.append({  # O(1) 
                    'text': cell.text(),  # O(1) 
                    'style': cell.styleSheet()  # O(1) 
                })
            self.cells_state.append(cell_row)  # O(1) 

class GameStateManager:
    def __init__(self):
        self.history = []  # O(1) 
        
    def push_state(self, grid, cells):
        """Store current game state
        Best Case: O(1) - No cells to store
        Average Case: O(height * width + m * n) - Creating a new GameState
        Worst Case: O(height * width + m * n) - Creating a new GameState
        """
        state = GameState(grid, cells)  # O(height * width + m * n) Creating a new GameState
        self.history.append(state)  # O(1) 
        
    def pop_state(self):
        """
        Return to previous state
        Best Case: O(1) - No states to return to
        Average Case: O(1) - Return to previous state
        Worst Case: O(1) - Return to previous state
        """
        if self.history:  # O(1) 
            return self.history.pop()  # O(1) 
        return None  # O(1) 
    
    def clear_history(self):
        """Clear all history
        Best Case: O(1) - No states to clear
        Average Case: O(1) - Clear all states
        Worst Case: O(1) - Clear all states
        """
        self.history.clear()  # O(1) 
