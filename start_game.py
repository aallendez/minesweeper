""" 
    When the player starts the game and presses on the first cell in the grid, it will call this function which will distribute the mines in the grid.
"""

from collections import deque
import random

def generate_mines(grid, first_row, first_col, num_mines=20):
    """
    Generate mines after the first cell is clicked, ensuring an irregular safe area.
    """
    height = len(grid)
    width = len(grid[0])
    
    # Get initial safe cells with randomized expansion
    safe_cells = irregular_safe_area(grid, first_row, first_col)
    
    # Create a list of all possible cell coordinates
    all_cells = [(r, c) for r in range(height) for c in range(width)]
    
    # Remove safe cells from possible mine locations
    available_cells = [cell for cell in all_cells if cell not in safe_cells]
    
    # Exclude the first cell and its neighbors from mine placement
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            neighbor_row = first_row + dx
            neighbor_col = first_col + dy
            if (0 <= neighbor_row < height and 0 <= neighbor_col < width):
                available_cells = [cell for cell in available_cells if cell != (neighbor_row, neighbor_col)]
    
    # Randomly select cells for mine placement
    mine_cells = random.sample(available_cells, min(num_mines, len(available_cells)))
    
    # Place mines in the grid
    for row, col in mine_cells:
        grid[row][col] = 'M'
    
    return grid

def irregular_safe_area(grid, start_row, start_col, min_safe_cells=12):
    """
    Creates an irregular-shaped safe area using randomized expansion.
    Uses a modified BFS with random probability of expansion.
    """
    height = len(grid)
    width = len(grid[0])
    safe_cells = set()
    queue = deque([(start_row, start_col)])
    safe_cells.add((start_row, start_col))
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    while queue and len(safe_cells) < min_safe_cells:
        row, col = queue.popleft()
        
        # Randomize direction order for irregular expansion
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < height and 0 <= new_col < width 
                    and (new_row, new_col) not in safe_cells
                    # Random probability of expansion (70%)
                    and random.random() < 0.7):
                safe_cells.add((new_row, new_col))
                queue.append((new_row, new_col))
    
    return safe_cells
