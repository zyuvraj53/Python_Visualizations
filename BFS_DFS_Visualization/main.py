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
PURPLE = (125, 0, 255)

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
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
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

  # Highlight the current cell
  
  #!! Perhaps here too it will be x + 1, y + 1, w + 1, w + 1
  def highlight(self):
    x = self.i * w
    y = self.j * w
    pygame.draw.rect(screen, BLACK, (x, y, w, w))

  def hightlight_goal(self):
    x = self.i * w
    y = self.j * w
    pygame.draw.rect(screen, RED, (x, y, w, w))
    
  def dfs_highlight(self):
    x = self.i * w
    y = self.j * w
    pygame.draw.rect(screen, PURPLE, (x, y, w, w))
    
  # Show cell and its walls
  def show(self):
    x = self.i * w
    y = self.j * w

    # Draw cell walls only if they are still present
    if self.walls[0]:  # Top
      pygame.draw.line(screen, RED, (x, y), (x + w, y), 1)
    if self.walls[1]:  # Right
      pygame.draw.line(screen, RED, (x + w, y), (x + w, y + w), 1)
    if self.walls[2]:  # Bottom
      pygame.draw.line(screen, RED, (x + w, y + w), (x, y + w), 1)
    if self.walls[3]:  # Left
      pygame.draw.line(screen, RED, (x, y + w), (x, y), 1)

    # Fill visited cells with green
    if self.visited:
      pygame.draw.rect(screen, GREEN, (x  + 1, y + 1, w + 1, w + 1))
      ### TODO:
      #Used a bit of a hack here, I have shifted the cells coloring by one pixel so that one of the overlapping cell's wall is seen while the other one gets covered, this should be fixed by separating the cells and their walls, and not having them overlap, of by taking the walls inside the cell

# Remove walls between two cells
def remove_walls(a, b):
  dx = a.i - b.i
  if dx == 1:
    a.walls[3] = False  # Remove left wall
    b.walls[1] = False  # Remove right wall
  elif dx == -1:
    a.walls[1] = False
    b.walls[3] = False

  dy = a.j - b.j
  if dy == 1:
    a.walls[0] = False  # Remove top wall
    b.walls[2] = False  # Remove bottom wall
  elif dy == -1:
    a.walls[2] = False
    b.walls[0] = False


# Populate grid with cells
for j in range(rows):
  for i in range(cols):
    grid.append(Cell(i, j))

# Set starting point
current = grid[0]

# Set endpoint
goal_cell = random.choice(grid)

#def DFS(current_cell = grid[0], dfs_visited = None):
  #if dfs_visited is None:
    #dfs_visited = []

  #if current_cell is goal_cell:
    #return
  
  #dfs_visited.append(current_cell)
  
  #top = current_cell.index(current_cell.i, current_cell.j - 1)
  #right = current_cell.index(current_cell.i + 1, current_cell.j)
  #bottom = current_cell.index(current_cell.i, current_cell.j + 1)
  #left = current_cell.index(current_cell.i - 1, current_cell.j)
  
  #directions = [top, right, bottom, left]
  
  #random.shuffle(directions)
  
  #for direction in directions:
    #new_cell = direction
    #if new_cell.index(new_cell.i, new_cell.j) is not None and new_cell not in dfs_visited:
      #DFS(new_cell, dfs_visited)
      #new_cell.dfs_highlight()
      #pygame.display.update()

dfs_visited = []
current_cell = grid[0]
def DFS_step():
  global currennt_cell
  if current_cell == goal_cell:
    return
  
  dfs_visited.append(current_cell)
  current_cell.dfs_highlight()
  
  top = current_cell.index(current_cell.i, current_cell.j - 1)
  right = current_cell.index(current_cell.i + 1, current_cell.j)
  bottom = current_cell.index(current_cell.i, current_cell.j + 1)
  left = current_cell.index(current_cell.i - 1, current_cell.j)
  
  directions = [top, right, bottom, left]
  
  random.shuffle(directions)
  
  new_cell = None
  
  for direction in directions:
    if direction is not None:
      if direction is top and not current_cell.walls[0]:
        new_cell = grid[direction]
      elif direction is right and not current_cell.walls[1]:
        new_cell = grid[direction]
      elif direction is bottom and not current_cell.walls[2]:
        new_cell = grid[direction]
      elif direction is left and not current_cell.walls[3]:
        new_cell = grid[direction] 
  current_cell = new_cell
  
# Main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  # Fill screen
  screen.fill(WHITE)

  # Show all cells
  for cell in grid:
    cell.show()

  # Mark current cell as visited and highlight it
  current.visited = True
  current.highlight()

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

  if len(stack) == 0:
    # Choose a random cell to be the goal, if you want to highlight the last cell, change this line from being the random cell to being the last cell
    goal_cell.hightlight_goal()
    DFS_step()
  
  # Update the screen
  pygame.display.update()
  clock.tick(60)
