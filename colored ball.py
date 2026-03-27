import pygame
from random import choice

pygame.init()
screenx,screeny = 500,500
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("colored ball")
colors = [(0,0,0),(255,255,255)]

current_color =choice(colors)
x,y = 30,30
sprx,spry = 60,60
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_a]: x -= 3
        if pressed[pygame.K_d]: x += 3
        if pressed[pygame.K_w]: y -= 3
        if pressed[pygame.K_s]: y += 3

        if x >= screenx-60:
            x = screenx - 60
            current_color = choice(colors)
        if x <= 0:
            x = 0
            current_color = choice(colors)
        if y >= screenx-60:
            y = screenx - 60
            current_color = choice(colors)
        if y <= 0:
            y = 0
            current_color = choice(colors)
    screen.fill("grey")
    pygame.draw.rect(screen,current_color,(x,y,sprx,spry))
    pygame.display.flip()
    clock.tick(60)