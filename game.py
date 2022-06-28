import pygame,draw,time
paused = True
Grid=[]
PreGrid=[]

def InitGrid():
  for i in range(40):
    Grid.append([])
    PreGrid.append([])
    for j in range(30):
      Grid[i].append(0)
      PreGrid[i].append(0)

def check(x,y):
  testX = [(x-1),x,(x+1)]
  testY = [(y-1),y,(y+1)]
  result = 0
  for i in testX:
    for j in testY:
      if not(i==x and j==y):
        if i > 40 or j >30 or i<0 or j<0:
          pass
        elif PreGrid[i][j] ==1:
          result += 1
  if PreGrid[x][y] == 1 :
    if result > 1 and result < 4:
      pass
      return True
    else:
      Grid[x][y]=0
      return False
  elif PreGrid[x][y] ==0:
    if result == 3:
      Grid[x][y] = 1
      return True
  else:
    Grid[x][y]=0
    return False
  
def game(wnd):
  count = 0
  if not paused:
    for i in range(0,len(Grid)-1):
      for j in range(0,len(Grid[i])-1):
        if check(i,j):
          if Grid[i][j] != PreGrid[i][j]:
            count += 1
            draw.block(wnd,i,j)
        else:
          if Grid[i][j] != PreGrid[i][j]:
            draw.unblock(wnd,i,j)
    updatePreGrid()
    pygame.display.update()
    updateblocks(wnd)
  if paused:
    draw.drawGrid(wnd,400,300)
    pass
  time.sleep(0.5)


def updatePreGrid():
  for i in range(len(Grid)):
    for j in range(len(Grid[i])):
      PreGrid[i][j] = Grid[i][j]
    
      


def updateblocks(wnd):
  for i in range(0,len(Grid)-1):
    for j in range(0,len(Grid[i])-1):
      if Grid[i][j] ==1:
        draw.block(wnd,i,j)
      else:
        draw.unblock(wnd,i,j)
  pygame.display.update()