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

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")

background = pygame.transform.scale(pygame.image.load("backround.png"), (screen_width,screen_height))
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
num_of_enemies = 6

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
    over_text = game_font.render("GAME OVER", True, (255, 0,0))
    screen.blit(over_text, (350, 200))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX_val, enemyY_val, bulletX_val, bulletY_val):
    distance = math.sqrt((enemyX_val - bulletX_val) ** 2 + (enemyY_val - bulletY_val) ** 2)
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
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

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
            pygame.display.update()
            continue

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0 or enemyX[i] >= screen_width - enemyImg[i].get_width():
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, screen_width - enemyImg[i].get_width())
            enemyY[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
            enemy_vel_x += 3
            enemy_vel_y += 5

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_vel
        if bulletY <= 0:
            bulletY = player_start_y
            bullet_state = "ready"

    player(playerX, playerY)
    show_da_score()
    pygame.display.update()
