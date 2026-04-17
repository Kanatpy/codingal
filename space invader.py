import math
import pygame
import random
import sys

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_vel_x = 4
enemy_vel_y = 40
bullet_vel = 10
collision_distance = 27

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("backround music.mp3")
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play(-1)

shootSFX = pygame.mixer.Sound("shoot.mp3")
explosionSFX = pygame.mixer.Sound("explosion.mp3")
GAMEOVERSFX = pygame.mixer.Sound("GAMEOVER.mp3")

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")

background = pygame.transform.scale(pygame.image.load("backround.png"), (screen_width, screen_height))
pygame.display.set_icon(pygame.image.load("icon.png"))

player_img = pygame.transform.scale_by(pygame.image.load("player.png"), 4)
playerX = player_start_x
playerY = player_start_y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(pygame.transform.scale_by(pygame.image.load("enemie.png"), 4))
    enemyX.append(random.randint(0, screen_width - 60))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyX_change.append(enemy_vel_x)
    enemyY_change.append(enemy_vel_y)

bulletImg = pygame.transform.scale_by(pygame.image.load("bullet.png"), 1.2)
bulletX = 0
bulletY = player_start_y
bullet_state = "ready"

score_value = 0
game_font = pygame.font.SysFont("jetbrains mono", 32)

def show_da_score():
    score = game_font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

def GAMEOVER():
    over_text = game_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (350, 200))
    GAMEOVERSFX.play(1)

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def draw_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < collision_distance

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                shootSFX.play()
                bulletX = playerX
                bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, screen_width - player_img.get_width()))

    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            GAMEOVER()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= screen_width - enemyImg[i].get_width():
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if bullet_state == "fire":
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = player_start_y
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, screen_width - 60)
                enemyY[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
                enemy_vel_x += 3
                enemy_vel_y += 5
                explosionSFX.play()

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == "fire":
        draw_bullet(bulletX, bulletY)
        bulletY -= bullet_vel
        if bulletY <= 0:
            bulletY = player_start_y
            bullet_state = "ready"

    player(playerX, playerY)
    show_da_score()
    pygame.display.update()
