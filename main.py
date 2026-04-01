import pygame


pygame.init()
screen = pygame.display.set_mode((800,400))

pygame.display.set_caption("window")
clock = pygame.time.Clock()

block_x = 50
block_y = 50
y_pos = 400
x_pos = 375

vel_x = 0
vel_y = 0



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                vel_x += 7
                pygame.display.update()

            if event.key == pygame.K_a:
                vel_x -= 7
                pygame.display.update()

            if event.key == pygame.K_w:
                vel_y -= 7
                pygame.display.update()

            if event.key == pygame.K_s:
                vel_y += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                vel_x -= 7
                pygame.display.update()

            if event.key == pygame.K_a:
                vel_x += 7
                pygame.display.update()

            if event.key == pygame.K_w:
                vel_y += 7
                pygame.display.update()

            if event.key == pygame.K_s:
                vel_y -= 7               

    y_pos += vel_y
    x_pos += vel_x

    screen.fill("black")
    block =pygame.draw.rect(screen, ("Blue"), (x_pos, y_pos, 70, 70))
    block =pygame.draw.rect(screen, ("white"), (x_pos, y_pos, block_y, block_x))

    if x_pos < 0:
        x_pos=0
    if x_pos > 750:
        x_pos= 750
    if y_pos<0:
        y_pos = 0
    if y_pos >350:
        y_pos = 350

    pygame.display.update()
    clock.tick(60)