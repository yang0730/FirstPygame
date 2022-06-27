import pygame,draw
paused = False
Grid=[]
def InitGrid():
  for i in range(0,599):
    Grid.append([])
    for j in range(0,799):
      Grid[i].append(0)

def check(x,y):
  testX = [x-1,x,x+1]
  testY = [y-1,y,y+1]
  result = 0
  for i in testX:
    for j in testY:
      if not(i==x and j==y):
        if Grid[i][i] ==1:
          result += 1
  if (result==2 or result ==3) and Grid[x][y] == 1 :
    return True
  elif Grid[x][y] ==0 and result == 3:
    return True
  return False
  
def game(wnd):
  if not paused:
    for i in Grid:
      for j in Grid[i]:
        if Grid[i][j] != 0 and check(i,j):
          draw.block(wnd,i,j)
    pygame.display.update()
  if paused:

    pygame.display.update()


