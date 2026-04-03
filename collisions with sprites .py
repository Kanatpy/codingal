import pygame
import random

screenY,screenX = 800,600
velocity = 7
font_size = 72

pygame.init()

font = pygame.font.SysFont("arial",font_size)

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,Xchange,Ychange):
        self.rect.x = max(min(self.rect.x + Xchange,screenX - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + Ychange,screenY - self.rect.height),0)

screen = pygame.display.set_mode((screenX,screenY))
screen.fill("white")
pygame.display.set_caption("sprites with collisions")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

spr1 = sprite(pygame.Color("red"),20,20)
spr1.rect.x,spr1.rect.y = random.randint(0,screenX),random.randint(0,screenY)
all_sprites.add(spr1)

spr2 = sprite(pygame.Color("blue"),20,20)
spr2.rect.x,spr2.rect.y = random.randint(0,screenX),random.randint(0,screenY)
all_sprites.add(spr2)

winning = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not winning:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT])*velocity
        Y_change = (keys[pygame.K_DOWN] -keys[pygame.K_UP])*velocity
        spr1.move(x_change,Y_change)
        if spr1.rect.colliderect(spr2.rect):
            all_sprites.remove(spr2)
            winning = True
    screen.fill("white")
    all_sprites.draw(screen)

    if winning:
        win_text = font.render("You Win",True,(0,0,0))
        screen.blit(win_text,((screenX-win_text.get_width())//2,(screenY-win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(60)