import pygame
pygame.init()
height,width = 600,800
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
def drawGrid():
  for i in range(0,height,10):
    pygame.draw.rect(window,(125,125,125),(i,1,1,height),border_radius=0)
  for j in range(0,width,10):
    pygame.draw.rect(window,(125,125,125),(1,j,width,1),border_radius=0)
      
def block(x,y):
  pygame.draw.rect(window, (255,255,255), (x,y,10,10), border_radius=0)

def unblock(x,y):
  pygame.draw.rect(window, (0,0,0), (x,y,10,10), border_radius=0)
  


pygame.display.set_caption("Deez Nut")
window.fill(BGC)
drawGrid()
block(100,100)
block(100,110)
pygame.display.update()


