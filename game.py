import pygame,draw
paused = False

def game(wnd):
  if not paused:
    draw.block(wnd,100,100)
    pygame.display.update()
  if paused:

    pygame.display.update()


