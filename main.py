import pygame
pygame.init()
def block(x,y):
  pygame.draw.rect(window, (255,255,255), (x,y,10,10), border_radius=0)

def unblock(x,y):
  pygame.draw.rect(window, (0,0,0), (x,y,10,10), border_radius=0)
  
height,width = 600,800
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Deez Nut")
window.fill(BGC)
block(100,100)
block(100,110)
pygame.display.update()


