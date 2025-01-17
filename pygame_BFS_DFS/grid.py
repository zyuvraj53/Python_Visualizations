#class Grid:
  #def __init__(self, width, height, sections = (16, 16)):
    #self.width = width
    #self.height = height
    #self.rows, self.cols = sections
    #self.grid = self.make_grid()
  
  #def make_grid(self):
    #return [[Grid.Cell(self.width // self.cols, self.height // self.rows) for _ in range(self.cols)] for _ in range(self.rows)]
  
  #def visualize_grid(self):
    #pass
    ## Create a pygame initializer
    ## Create a grid of all black, consisting of the sections with walls
    
  #def make_maze(self):
    #pass
    ## Create an all black grid with visualize_grid
    ## Create a maze out of the grid that was created
    ## Store the maze in a variable, without overwriting it with a search, as multiple algorithms might have to run in a single maze
  
  #def make_new_maze(self):
    #pass
    ## Create a new grid of all black, visualize that grid, and make a new maze, overwrite the maze variable with this one now
  
  #def BFS(self):
    #pass
  
  #class Cell:
    #def __init__(self, width, height, wall = [True, True, True, True], visited = False):
      #self.wall = wall
      #self.visited = visited
      #self.height = height 
      #self.widht = width 

#if __name__ == '__main__':
  #grid = Grid(800, 600)
  