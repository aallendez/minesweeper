""" 
    When the player starts the game and presses on the first cell in the grid, it will call this function which will distribute the mines in the grid.
"""

from collections import deque
import random

def generate_mines(grid, first_row, first_col, num_mines):
    """
    Generate mines after the first cell is clicked, ensuring an equal distribution across the grid.
    Best Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    Average Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    Worst Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    """
    height = len(grid)  # O(1)
    width = len(grid[0])  # O(1)
    
    # Get initial safe cells with randomized expansion
    safe_cells = irregular_safe_area(grid, first_row, first_col)  # O(height * width) in worst case
    # Space Complexity: O(height * width) for safe_cells

    # Create a list of all possible cell coordinates
    all_cells = [(r, c) for r in range(height) for c in range(width)]  # O(height * width)
    # Space Complexity: O(height * width) for all_cells
    
    # Remove safe cells from possible mine locations
    available_cells = [cell for cell in all_cells if cell not in safe_cells]  # O(height * width)
    # Space Complexity: O(height * width) for available_cells
    
    # Exclude the first cell and its neighbors from mine placement
    for dx in [-1, 0, 1]:  # O(1)
        for dy in [-1, 0, 1]:  # O(1)
            neighbor_row = first_row + dx  # O(1)
            neighbor_col = first_col + dy  # O(1)
            if (0 <= neighbor_row < height and 0 <= neighbor_col < width):  # O(1)
                available_cells = [cell for cell in available_cells if cell != (neighbor_row, neighbor_col)]  # O(n)
    
    # Calculate mines per row
    mines_per_row = num_mines // height  # O(1)
    remaining_mines = num_mines % height  # O(1)
    
    # Place mines in each row
    for row in range(height):  # O(height)
        # Determine how many mines to place in this row
        mines_in_this_row = mines_per_row + (1 if row < remaining_mines else 0)  # O(1)
        
        # Randomly select cells for mine placement in this row
        if mines_in_this_row > 0:  # O(1)
            row_cells = [(row, c) for c in range(width) if (row, c) in available_cells]  # O(width)
            mine_cells = random.sample(row_cells, min(mines_in_this_row, len(row_cells)))  # O(min(mines_in_this_row, width))
            
            # Place mines in the grid
            for col in mine_cells:  # O(min(mines_in_this_row, width))
                grid[col[0]][col[1]] = 'M'  # O(1)
    
    return grid  # O(1)

def irregular_safe_area(grid, start_row, start_col, min_safe_cells=12):
    """
    Creates an irregular-shaped safe area using randomized expansion.
    Uses a modified BFS with random probability of expansion.
    Best Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    Average Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    Worst Case: O(height * width) - When the safe cells are already determined and all cells are filtered.
    """
    height = len(grid)  # O(1)
    width = len(grid[0])  # O(1)
    safe_cells = set()  # O(1)
    queue = deque([(start_row, start_col)])  # O(1)
    safe_cells.add((start_row, start_col))  # O(1)
    
    directions = [  # O(1)
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    while queue and len(safe_cells) < min_safe_cells:  # O(height * width) in worst case
        row, col = queue.popleft()  # O(1)
        
        # Randomize direction order for irregular expansion
        random.shuffle(directions)  # O(1)
        
        for dx, dy in directions:  # O(1)
            new_row, new_col = row + dx, col + dy  # O(1)
            if (0 <= new_row < height and 0 <= new_col < width  # O(1)
                    and (new_row, new_col) not in safe_cells  # O(1)
                    # Random probability of expansion (70%)
                    and random.random() < 0.7):  # O(1)
                safe_cells.add((new_row, new_col))  # O(1)
                queue.append((new_row, new_col))  # O(1)
    
    return safe_cells  # O(1)
