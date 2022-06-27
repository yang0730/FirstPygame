import pygame
def block(wnd,x,y):
  pygame.draw.rect(wnd, (255,255,255), (x,y,10,10), border_radius=0)

def unblock(wnd,x,y):
  pygame.draw.rect(wnd, (0,0,0), (x,y,10,10), border_radius=0)