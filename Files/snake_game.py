import pygame
import time
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH = 800
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры блока змейки
BLOCK_SIZE = 20
INITIAL_SPEED = 3
LEVEL_UP_SCORE = 5

# Шрифт
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Отображение счёта
def show_score(score, level):
    value = score_font.render(f"Ваш счёт: {score} | Уровень: {level}", True, BLUE)
    screen.blit(value, [10, 10])

# Рисование змейки
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

# Сообщение на экране
def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    screen.blit(msg_surface, [WIDTH / 6, HEIGHT / 3])

# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    clock = pygame.time.Clock()
    speed = INITIAL_SPEED
    level = 1

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            message("Вы проиграли! Нажмите Q - выйти или C - заново", RED)
            show_score(length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = BLOCK_SIZE

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_score(length_of_snake - 1, level)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

            if (length_of_snake - 1) % LEVEL_UP_SCORE == 0:
                level += 1
                speed += 5

        clock.tick(speed)

    pygame.quit()
    sys.exit()

# Запуск игры
game_loop()
