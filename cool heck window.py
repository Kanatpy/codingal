import pygame

pygame.init()

screen = pygame.display.set_mode((1000,200))
pygame.display.set_caption("SOME TEXT")

txt = pygame.font.Font(None,50).render("TEXT",True,"white")
txt_rect = txt.get_rect(center=(500,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("BLUE")
    screen.blit(txt,txt_rect)
    pygame.display.flip()