import pygame
pygame.init()
def block(Coord):
  pygame.draw.rect(window, (255,255,255), (Coord[0],Coord[1],10,10), border_radius=1)
  
height,width = 600,800
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Deez Nut")
window.fill(BGC)

pygame.display.update()


