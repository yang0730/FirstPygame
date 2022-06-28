import pygame
def block(wnd,x,y):
  pygame.draw.rect(wnd, (255,255,255), (x*10,y*10,10,10), border_radius=0)
  pygame.display.flip()

def unblock(wnd,x,y):
  pygame.draw.rect(wnd, (0,0,0), (x*10,y*10,10,10), border_radius=0)
  pygame.draw.rect(wnd, (125,125,125), (x*10,y*10,10,1), border_radius=0)
  pygame.draw.rect(wnd, (125,125,125), (x*10,y*10,1,10), border_radius=0)
  pygame.display.flip()
