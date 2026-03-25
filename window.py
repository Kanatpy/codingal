import pygame

pygame.init()

screen = pygame.display.set_mode((800,600),pygame.RESIZABLE)
pygame.display.set_caption("A RANDOM WINDOW")
img =pygame.image.load("pebbles.jpg")
pebbles = pygame.transform.scale_by((img).convert_alpha(),0.5)
pebbles_rect=pebbles.get_rect(center=(400,300))
txt = pygame.font.Font(None,36).render("PEBBLES da cat",True,(255,255,255))
txt_rect = txt.get_rect(center = (400,200))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("magenta")
    screen.blit(pebbles,pebbles_rect)
    screen.blit(txt,txt_rect)

    pygame.display.flip()
    clock.tick(60)
