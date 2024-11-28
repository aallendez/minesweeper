class GameState:
    def __init__(self, grid, cells_state):
        """
        This function initializes a stack data structure where the game state is stored 
        each time the player makes a move. When the player clicks on a cell, the current 
        state is stored in the stack. When the player clicks on the "Undo" button (if they have
        lives left), the previous state is retrieved from the stack by popping the last element of the
        stack.
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
        Case is always O(height * width + m * n) where m is the number of rows and n is the number of cells in each row since you are creating a new GameState and appending it to the history list.
        """
        state = GameState(grid, cells)  # O(height * width + m * n) Creating a new GameState
        self.history.append(state)  # O(1) amortized - List append
        
    def pop_state(self):
        """
        Return to previous state
        Case is always O(1) since you are only popping from the history list.
        """
        if self.history:  # O(1) 
            return self.history.pop()  # O(1) 
        return None  # O(1) 
    
    def clear_history(self):
        """Clear all history
        Case is always O(1) since you are only clearing the history list.
        """
        self.history.clear()  # O(1) 
