import pygame
import sys
import random

# Define event types BEFORE using them
X_DETECT = pygame.USEREVENT + 1
Y_DETECT = pygame.USEREVENT + 2

class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.colors = color
        self.vel_x = 10
        self.vel_y = 10
        self.x_pos = random.randint(0, 500 - 30)
        self.y_pos = random.randint(0, 500 - 30)
        self.image = pygame.Surface((30, 30))
        self.image.fill(random.choice(self.colors))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Trigger events on collision
        if self.rect.left <= 0 or self.rect.right >= 500:
            pygame.event.post(pygame.event.Event(X_DETECT))
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            pygame.event.post(pygame.event.Event(Y_DETECT))

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Create sprites
square1 = Square(colors)
square2 = Square(colors)
all_sprites = pygame.sprite.Group(square1, square2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == X_DETECT:
            square1.vel_x *= -1
            square2.vel_x *= -1
            square1.image.fill(random.choice(square1.colors))
            square2.image.fill(random.choice(square2.colors))
        if event.type == Y_DETECT:
            square1.vel_y *= -1
            square2.vel_y *= -1
            square1.image.fill(random.choice(square1.colors))
            square2.image.fill(random.choice(square2.colors))

    screen.fill("black")
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)   