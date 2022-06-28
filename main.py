import pygame,draw,game,time
pygame.init()
height,width = 300,400
BGC = 0,0,0
window = pygame.display.set_mode((width,height))



game.InitGrid()

pygame.display.set_caption("Deez Nut")
window.fill(BGC)
time.sleep(0.5)
draw.clearGrid(window)


while 1:
  draw.drawGrid(window,width,height)
  game.game(window)
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      pos=pygame.mouse.get_pos()
      x=pos[0]//10
      y=pos[1]//10  
      if game.Grid[x][y] == 1:
        game.Grid[x][y] = 0
        draw.unblock(window,x,y)
      else: 
        game.Grid[x][y] =1
        draw.block(window,x,y)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
      game.paused = not game.paused





