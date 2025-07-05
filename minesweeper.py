def is_valid_position(grid, row, col):
    # Check if the position is within bounds of the grid
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def count_adjacent_mines(grid, row, col):
    # Define the possible adjacent positions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_position(grid, new_row, new_col) and grid[new_row][new_col] == '#':
            count += 1

    return count

def update_grid(grid):
    new_grid = [['0' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == '-':
                # Count adjacent mines and update the cell
                mine_count = count_adjacent_mines(grid, row_idx, col_idx)
                new_grid[row_idx][col_idx] = str(mine_count)
            else:
                # Cell already has a mine, keep it as is
                new_grid[row_idx][col_idx] = cell

    return new_grid

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Example input
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Update the grid and print the result
output_grid = update_grid(input_grid)
print_grid(output_grid)
