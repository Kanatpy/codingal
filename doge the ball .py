import pygame, random, sys

class Ball:
    def __init__(self, color, velocity_y, velocity_x):
        self.x = random.randint(40, 800 - 40)
        self.y = random.randint(40, 800 - 40)
        self.radius = 20
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.center_x = self.x + self.radius
        self.center_y = self.y + self.radius
    
    def draw_ball(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.center_x = self.x + self.radius
        self.center_y = self.y + self.radius
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

class Player:
    def __init__(self, color, width, height):
        self.pos_x = 0
        self.pos_y = 0
        self.color = color
        self.width = width
        self.height = height

    def draw_player(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("AVOID DA BALL")
clock = pygame.time.Clock()
font = pygame.font.SysFont("jetbrains mono", 50)
lose_txt = font.render("ya stink", True, "white")
txt_rect = lose_txt.get_rect(center=(400, 400))


enemies = [Ball("red", random.randint(5, 15), random.randint(5, 15)) for _ in range(20)]

player = Player("blue", 40, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.pos_x = mouse_x - player.width // 2
    player.pos_y = mouse_y - player.height // 2

    player_rect = pygame.Rect(player.pos_x, player.pos_y, player.width, player.height)
    
    for enemy in enemies:  
        if enemy.x <= 0 or enemy.x >= 800 - enemy.radius * 2:
            enemy.velocity_x *= -0.95
        if enemy.y <= 0 or enemy.y >= 800 - enemy.radius * 2:
            enemy.velocity_y *= -0.95

        enemy.draw_ball()
        if player_rect.collidepoint(enemy.center_x, enemy.center_y):
            screen.blit(lose_txt, txt_rect)
            pygame.display.flip()
            pygame.time.wait(2500)
            pygame.quit()
            sys.exit()

    player.draw_player()
    pygame.display.flip()
    clock.tick(60)   