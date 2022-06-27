import pygame,draw,game
pygame.init()
height,width = 600,800
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
def drawGrid():
  for i in range(0,height,10):
    pygame.draw.rect(window,(125,125,125),(i,1,1,height),border_radius=0)
  for j in range(0,width,10):
    pygame.draw.rect(window,(125,125,125),(1,j,width,1),border_radius=0)

game.InitGrid()
      

  


pygame.display.set_caption("Deez Nut")
window.fill(BGC)
drawGrid()
game.game(window)




