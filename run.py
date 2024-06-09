import random


# Function to create a grid
def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Function to place battleships randomly on the grid
def place_battleships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        grid[x][y] = 'S'

# Function to check if a guess is on the grid and not already guessed
def is_valid_guess(guess, size, guessed_cells):
    x, y = guess
    return (0 <= x < size) and (0 <= y < size) and (guess not in guessed_cells)