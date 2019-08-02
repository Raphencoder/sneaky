import pygame
import sys
import os
from snake import Snake
from food import FoodSpawer

SCREEN_LENGTH = 400
MIDDLE_SCREEN = round(SCREEN_LENGTH / 2)


window = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_LENGTH))
pygame.display.set_caption("snake")
fps = pygame.time.Clock()
score = 0

snake = Snake(SCREEN_LENGTH, MIDDLE_SCREEN)
FoodSpawner = FoodSpawer(SCREEN_LENGTH, MIDDLE_SCREEN)


def game_over():
    os.system('clear')
    print("Game over\nScore: " + str(score))
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction_to("RIGHT")
            if event.key == pygame.K_UP:
                snake.change_direction_to("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction_to("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction_to("LEFT")
    foodPos = FoodSpawner.spawn_food(snake.body)
    snake.move()
    if snake.eat(foodPos):
        score += 10
        FoodSpawner.isFoodOnScreen = False

    window.fill(pygame.Color(225, 225, 225))

    for pos in snake.get_body():
        pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.draw.rect(window, pygame.Color(0, 225, 0), pygame.Rect(foodPos[0], foodPos[1], 20, 20))

    if snake.check_collision() == 1:
        game_over()

    pygame.display.flip()
    fps.tick(round(SCREEN_LENGTH / 40))