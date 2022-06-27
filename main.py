import pygame
pygame.init()
height,width = 600,800
BGC = 0,0,0
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Deez Nut")
window.fill(BGC)

pygame.display.update()