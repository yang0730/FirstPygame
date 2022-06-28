import pygame,draw,game
pygame.init()
height,width = 150,200
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
def drawGrid():
  for i in range(0,width,10):
    pygame.draw.rect(window,(125,125,125),(i,1,1,height),border_radius=0)
  for j in range(0,height,10):
    pygame.draw.rect(window,(125,125,125),(1,j,width,1),border_radius=0)


game.InitGrid()

pygame.display.set_caption("Deez Nut")
window.fill(BGC)
drawGrid()
#game.game(window)

while 1:
  drawGrid()
  game.game(window)
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
      pos=pygame.mouse.get_pos()
      x=pos[0]//10
      y=pos[1]//10  
      if game.Grid[x][y] == 1:
        game.Grid[x][y] = 0
        draw.unblock(window,x,y)
      else: 
        game.Grid[x][y] =1
        draw.block(window,x,y)
    if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
      game.paused = not game.paused





