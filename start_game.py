""" 
    When the player starts the game and presses on the first cell in the grid, it will call this function which will distribute the mines in the grid.
"""

from collections import deque
import random

def generate_mines(grid, first_row, first_col, num_mines=20):
    """
    Generate mines after the first cell is clicked, ensuring the clicked cell
    and its immediate neighbors are safe.
    
    Args:
        grid: 2D list representing the game grid
        first_row: row of the first clicked cell
        first_col: column of the first clicked cell
        num_mines: number of mines to place (default 10)
    """
    height = len(grid)
    width = len(grid[0])
    
    # Get safe cells using BFS
    safe_cells = breadth_first_search(grid, first_row, first_col)
    
    # Create a list of all possible cell coordinates
    all_cells = [(r, c) for r in range(height) for c in range(width)]
    
    # Remove safe cells from possible mine locations
    available_cells = [cell for cell in all_cells if cell not in safe_cells]
    
    # Randomly select cells for mine placement
    mine_cells = random.sample(available_cells, min(num_mines, len(available_cells)))
    
    # Place mines in the grid
    for row, col in mine_cells:
        grid[row][col] = 'M'  # 'M' represents a mine
    
    return grid

def breadth_first_search(grid, start_row, start_col, max_depth=1):
    height = len(grid)
    width = len(grid[0])
    safe_cells = set()
    queue = deque([(start_row, start_col, 0)])  # (row, col, depth)
    safe_cells.add((start_row, start_col))
    
    # Define the 8 possible directions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Perform BFS up to the specified depth
    while queue:
        row, col, depth = queue.popleft()
        
        if depth < max_depth:
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < height and 0 <= new_col < width 
                        and (new_row, new_col) not in safe_cells):
                    safe_cells.add((new_row, new_col))
                    queue.append((new_row, new_col, depth + 1))
    
    return safe_cells
