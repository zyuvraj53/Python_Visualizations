from sys import exit
import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

screen.fill((255,255,255))

pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

class Cell:
  def __init__(self, i, j): 
    self.i = i
    self.j = j
    self.walls = [True, True, True, True]
    self.visited = False

  def checkNeighbors():
    neighbors = []

    top = grid[index(i, j - 1)]
    right = grid[index(i + 1, j)]
    bottom = grid[index(i, j + 1)]
    left = grid[index(i - 1, j)]

    if top and not top.visited:
      neighbors.push(top)
    if right and not right.visited:
      neighbors.push(right)
    if bottom and not bottom.visited:
      neighbors.push(bottom)
    if left and not left.visited:
      neighbors.push(left)

    if neighbors.length > 0:
      r = floor(random(0, neighbors.length))
      return neighbors[r]
    else:
      return None
  
  #this.highlight = function () {
    #var x = this.i * w;
    #var y = this.j * w;
    #noStroke();
    #fill(0, 0, 255, 100);
    #rect(x, y, w, w);
  #};

  def show(self):
    x = self.i * w
    y = self.j * w
    #stroke(255);
    if self.walls[0]:
      pygame.draw.line(screen, RED, (x, y), (x + w, y), 2)
      
    if self.walls[1]:
      pygame.draw.line(screen, RED, (x + w, y), (x + w, y + w), 2)
      
    if self.walls[2]:
      pygame.draw.line(screen, RED, (x + w, y + w), (x, y + w), 2)
      
    if self.walls[3]:
      pygame.draw.line(screen, RED, (x, y + w), (x, y), 2)

    if self.visited:
      #noStroke()
      #fill(255, 0, 255, 100)
      pygmae.draw.rect(surface, GREEN, (x, y, w, w), 2)
      
  def index(self, i, j):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
      return False
    return i + j * cols

w = 20

cols, rows = width // w, height // w

grid = []

for i in range(cols):
  for j in range(rows):
    grid.append(Cell(i, j))
    
current = grid[0]

while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
      
  for cell in grid:
    cell.show()
  
  pygame.display.update()
  clock.tick(60)