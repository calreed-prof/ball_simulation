import pygame
import sys
import random
import time
import math

# intialize pygame
pygame.init()

# screen settings
screen_length, screen_width = 550, 550
screen = pygame.display.set_mode((screen_width, screen_length))

def random_color():
    """Returns a random hex (xxx,xxx,xxx)"""
    hex1 = random.randint(0,255)
    hex2 = random.randint(0,255)
    hex3 = random.randint(0,255)

    random_hex = (hex1, hex2, hex3)
    return random_hex

class Ball():
    def __init__(self, x, y, color, radius, time_created):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.velocity_x = 0
        self.velocity_y = 0
        self.time_created = time_created

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def apply_gravity(self):
        gravity_str = .8
        self.velocity_y += gravity_str
        self.y += self.velocity_y
        self.x += self.velocity_x

    def middle_gravity(self):
        gravity_str = .8
        self.x += self.velocity_x
        if self.y >= screen_length / 2:
            self.velocity_y -= gravity_str
            self.y += self.velocity_y
        if self.y <= screen_length / 2:
            self.velocity_y += gravity_str
            self.y += self.velocity_y

    def wall_collision_detection(self):
        if self.y > screen_length - self.radius:
            self.velocity_y = -self.velocity_y *.9
            self.y = screen_length - self.radius
            # self.color = random_color()

        if self.y < 0 + self.radius:
            self.velocity_y = -self.velocity_y *.9
            self.y = 0 + self.radius
            # self.color = random_color()

        if self.x > screen_width - self.radius:
            self.velocity_x = -self.velocity_x * .9
            self.x = screen_width - self.radius
            # self.color = random_color()

        if self.x < 0 + self.radius:
            self.velocity_x = -self.velocity_x * .9
            self.x = 0 + self.radius
            # self.color = random_color()

def create_ball(x, y):
    # x = random.randint(0,int(screen_width))
    # y = random.randint(0,int(screen_length/2))
    color = random_color()
    radius = 12
    time_created = time.time()
    ball = Ball(x, y, color, radius, time_created)
    balls.append(ball)

def draw_circle_border():
    center_x = screen_width / 2
    center_y = screen_length / 2
    pygame.draw.circle(screen, (255,255,255), (center_x,center_y), 200, 3)

def draw_middle_line():
    pygame.draw.line(screen, (255,255,255), (0, screen_length / 2), (screen_width, screen_length / 2), 1)

# This will hold all the balls
balls = []
# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            create_ball(mouse_x, mouse_y)

    # This will keep track of the mouse position to print the ball at the right point
    mouse_x, mouse_y = pygame.mouse.get_pos()
    time_now = time.time()

    # Time out Function
    balls = [ball for ball in balls if time_now - ball.time_created < 15]
    for ball in balls:
        ball.draw_ball()
        # ball.apply_gravity()
        ball.wall_collision_detection()
        ball.middle_gravity()

    # Draws line in the middle of the screen
    draw_middle_line()

    # goes through each ball and compares each ball to eachother
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[i].x - balls[j].x
            dy = balls[i].y - balls[j].y
            distance = math.sqrt(dx**2 + dy**2)

    print(f"fps: {clock.get_fps():.2f}", end='\r')

    # In loop system
    clock.tick(60)
    pygame.display.flip()
    screen.fill((0,0,0))

pygame.quit()
sys.exit()
