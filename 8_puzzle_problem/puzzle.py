import pygame
from sys import exit

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('8-Puzzle Problem')
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  
  pygame.display.update()
  clock.tick(60)