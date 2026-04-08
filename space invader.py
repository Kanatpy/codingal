import math , pygame,random

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

screen = pygame.display.set_mode((screen_width,screen_height))
backround = pygame.image.load("backround.png")
icon = pygame.display.set_icon(pygame.image.load("icon.png"))

player_img = pygame.image.load("player.png")
playerX = player_start_x
playerY = player_start_y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY= []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemie.png"))
    enemyX.append(random.randint(0,screen_width-60))
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyX_change.append(enemy_vel_x)
    enemyY_change.append(enemy_vel_y)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = player_start_y
bulletX_change = 0
bulletY_change = bullet_vel
bullet_state = "ready ta go"

score_value = 0
game_font = pygame.font.SysFont("arial")
textX = 10
textY = 10

def show_da_score():
    score = game_font.render("Score: ",+str(score_value),True,(255,255,255))
    screen.blit(score,(textX,textY))
def GAMEOVER():