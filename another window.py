import pygame
pygame.init()

screen = pygame.display.set_mode((4,4),pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
