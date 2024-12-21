from sys import exit
import pygame

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  
  pygame.display.update()
  clock.tick(60)
  