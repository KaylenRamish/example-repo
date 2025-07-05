## Minesweeper Grid Updater
# Description
This Python project implements a basic Minesweeper grid updater. Given a grid of cells containing either:

# for mines, or

- for empty cells,

the program calculates how many mines are adjacent (in all 8 directions) to each empty cell and replaces the empty cells with that number. Cells that contain mines remain unchanged.

# How It Works
Input: A 2D grid (list of lists) where:

"#" represents a mine.

"-" represents an empty cell.

# Processing:

For every empty cell, the code counts how many of its 8 neighboring cells contain mines.

Each empty cell is replaced with the corresponding mine count.

Output: A new grid with mine counts in place of empty cells.

# Example
Input Grid
diff
Copy
Edit
- - - # #
- # - - -
- - # - -
- # # - -
- - - - -
Output Grid
bash
Copy
Edit
1 2 2 # #
2 # 4 3 2
3 5 # 3 1
2 # # 3 1
1 2 3 2 0
How to Use
Make sure you have Python 3 installed. Run the code with the following command:

python minesweeper.py
The code will display the updated grid in your console.
