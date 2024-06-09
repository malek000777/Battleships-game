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