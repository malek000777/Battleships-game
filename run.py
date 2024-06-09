import random


# Function to create a grid
def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))