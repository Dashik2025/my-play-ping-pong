import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Настройки цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Настройки мяча
BALL_RADIUS = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Настройки ракеток
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Настройки шаров-преград
OBSTACLE_RADIUS = 10
obstacles = []
for _ in range(20):
    obstacle_x = random.randint(0, SCREEN_WIDTH)
    obstacle_y = random.randint(0, SCREEN_HEIGHT)
    obstacles.append((obstacle_x, obstacle_y))

# Основной цикл игры
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение ракеток
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5

    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отскок от стен и ракеток
    if ball_y < 0 or ball_y > SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed_y *= -1
    if ball_x < PADDLE_WIDTH and ball_y > paddle1_y and ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
    elif ball_x < 0:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
    if ball_x > SCREEN_WIDTH - PADDLE_WIDTH - BALL_RADIUS and ball_y > paddle2_y and ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
    elif ball_x > SCREEN_WIDTH - BALL_RADIUS:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2

    # Проверка столкновения с шарами-преградами
    for i, (obstacle_x, obstacle_y) in enumerate(obstacles):
        distance = ((ball_x - obstacle_x) ** 2 + (ball_y - obstacle_y) ** 2) ** 0.5
        if distance < BALL_RADIUS + OBSTACLE_RADIUS:
            ball_speed_x *= -1
            ball_speed_y *= -1
            obstacles.pop(i)

    # Отрисовка всего
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    for obstacle_x, obstacle_y in obstacles:
        pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (obstacle_x, obstacle_y), OBSTACLE_RADIUS)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

