import pygame
import numpy

LADO = 400
SCREEN_WIDTH = LADO
SCREEN_HEIGHT = LADO
area_dentro = 0
area_total = 0

# Intialize the pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("QUANTO VALE PI")

# Game Loop
running = True


def show_circle():
    pygame.draw.circle(screen, (0, 0, 255), (LADO / 2, LADO / 2), LADO / 2)
    pygame.draw.circle(screen, (155, 155, 155), (LADO / 2, LADO / 2), LADO / 2 - 1)


def show_point(x, y):
    global area_dentro, area_total
    area_total += 1
    if (x - LADO / 2) ** 2 + (y - LADO / 2) ** 2 <= (LADO / 2) ** 2:
        area_dentro += 1
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)
    pygame.draw.circle(screen, color, (x, y), 2)


def point():
    x = LADO * numpy.random.uniform(0, 1)
    y = LADO * numpy.random.uniform(0, 1)
    show_point(x, y)


while running:
    screen.fill((155, 155, 155))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    show_circle()
    for i in range(200):
        point()

    print(4 * area_dentro / area_total)
    pygame.display.update()
