class GameState:
    def __init__(self, grid, cells_state):
        self.grid = [row[:] for row in grid]  # Deep copy of grid
        self.cells_state = []
        # Store relevant cell information (text and style)
        for row in cells_state:
            cell_row = []
            for cell in row:
                cell_row.append({
                    'text': cell.text(),
                    'style': cell.styleSheet()
                })
            self.cells_state.append(cell_row)

class GameStateManager:
    def __init__(self):
        self.history = []
        
    def push_state(self, grid, cells):
        """Store current game state"""
        state = GameState(grid, cells)
        self.history.append(state)
        
    def pop_state(self):
        """Return to previous state"""
        if self.history:
            return self.history.pop()
        return None
    
    def clear_history(self):
        """Clear all history"""
        self.history.clear()
