import pygame
import math
import random
from sys import exit

pygame.init()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
width, height = 800, 600

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze Generator')
clock = pygame.time.Clock()

# Cell size
w = 40

# Calculate columns and rows
cols, rows = width // w, height // w

# Grid and stack
grid = []
stack = []


# Cell Class
class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left
        self.visited = False

    # Convert 2D grid to 1D index
    def index(self, i, j):
        if i < 0 or j < 0 or i >= cols or j >= rows:
            return None  # Return None for invalid indices
        return i + j * cols

    # Check for unvisited neighboring cells
    def check_neighbors(self):
        neighbors = []

        top = self.index(self.i, self.j - 1)
        right = self.index(self.i + 1, self.j)
        bottom = self.index(self.i, self.j + 1)
        left = self.index(self.i - 1, self.j)

        if top is not None and not grid[top].visited:
            neighbors.append(grid[top])
        if right is not None and not grid[right].visited:
            neighbors.append(grid[right])
        if bottom is not None and not grid[bottom].visited:
            neighbors.append(grid[bottom])
        if left is not None and not grid[left].visited:
            neighbors.append(grid[left])

        if len(neighbors) > 0:
            r = math.floor(random.random() * len(neighbors))
            return neighbors[r]
        else:
            return None

    # Show cell and its walls
    def show(self):
        x = self.i * w
        y = self.j * w

        # Draw cell walls
        if self.walls[0]:  # Top wall
            pygame.draw.line(screen, RED, (x, y), (x + w, y), 1)
        if self.walls[1]:  # Right wall
            pygame.draw.line(screen, RED, (x + w, y), (x + w, y + w), 1)
        if self.walls[2]:  # Bottom wall
            pygame.draw.line(screen, RED, (x + w, y + w), (x, y + w), 1)
        if self.walls[3]:  # Left wall
            pygame.draw.line(screen, RED, (x, y + w), (x, y), 1)

        # Fill visited cells with green (for visualization)
        if self.visited:
            pygame.draw.rect(screen, GREEN, (x, y, w, w), 1)


# Remove walls between two cells
def remove_walls(a, b):
    dx = a.i - b.i
    if dx == 1:
        a.walls[3] = False  # Remove left wall of a
        b.walls[1] = False  # Remove right wall of b
    elif dx == -1:
        a.walls[1] = False  # Remove right wall of a
        b.walls[3] = False  # Remove left wall of b

    dy = a.j - b.j
    if dy == 1:
        a.walls[0] = False  # Remove top wall of a
        b.walls[2] = False  # Remove bottom wall of b
    elif dy == -1:
        a.walls[2] = False  # Remove bottom wall of a
        b.walls[0] = False  # Remove top wall of b


# Populate grid with cells
for j in range(rows):
    for i in range(cols):
        grid.append(Cell(i, j))

# Set starting point
current = grid[0]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill screen with white background
    screen.fill(WHITE)

    # Show all cells (walls and visited status)
    for cell in grid:
        cell.show()

    # Mark current cell as visited and highlight it
    current.visited = True

    # Step 1: Check unvisited neighbors
    next_cell = current.check_neighbors()
    if next_cell:
        next_cell.visited = True

        # Step 2: Push current cell to stack
        stack.append(current)

        # Step 3: Remove walls between current and next cell
        remove_walls(current, next_cell)

        # Step 4: Move to next cell
        current = next_cell
    elif len(stack) > 0:
        # Backtrack if no neighbors
        current = stack.pop()

    # Update the screen
    pygame.display.update()
    clock.tick(60)
