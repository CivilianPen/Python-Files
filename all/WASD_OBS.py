import os
import keyboard
import time
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 500))
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont("Calibri", 150)
font_lower = pygame.font.SysFont("Calibri", 100)

W = font.render("W", True, (0, 0, 0))
A = font.render("A", True, (0, 0, 0))
S = font.render("S", True, (0, 0, 0))
D = font.render("D", True, (0, 0, 0))
shift = font_lower.render("shift", True, (0, 0, 0))
ctrl = font_lower.render("ctrl", True, (0, 0, 0))
space = font_lower.render("space", True, (0, 0, 0))
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
    
    screen.fill((135, 135, 135))
    
    
    if keyboard.is_pressed('w'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(200, 0, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(200, 0, 200, 200))

    if keyboard.is_pressed('a'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(0, 200, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 200, 200, 200))
        
    if keyboard.is_pressed('s'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(200, 200, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(200, 200, 200, 200))
            
    if keyboard.is_pressed('d'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(400, 200, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(400, 200, 200, 200))

    if keyboard.is_pressed('shift'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(0, 0, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, 200, 200))

    if keyboard.is_pressed('ctrl'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(400, 0, 200, 200))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(400, 0, 200, 200))

    if keyboard.is_pressed('space'):
        pygame.draw.rect(screen, (122,255,111), pygame.Rect(0, 400, 600, 100))
    else:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 400, 600, 100))
        
    screen.blit(W,(230,40))
    screen.blit(A,(60,240))
    screen.blit(S,(260,240))
    screen.blit(D,(450,240))
    screen.blit(shift,(10,60))
    screen.blit(ctrl,(430,60))
    screen.blit(space,(185,400))
        
        
    pygame.display.flip()
    clock.tick(60)
    
