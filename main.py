import sys
import pygame
from settings import Settings
from snack import Snake
from food import Food
#from button import Button
from scoreboard import Scoreboard


def levelup(score):
    k = score / 150
    speed = 10
    if k > 0:
        speed = k + 10
    return speed


def clock(speed):
    pygame.time.Clock().tick(speed)


def run_game():
    pygame.init()
    score = 0
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Gluttonous Snake")
    snake = Snake()
    food = Food()
    active = True
    '''play_button = Button(ai_settings, screen, "Play")
    if not active:
        play_button.draw_button()'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == pygame.K_SPACE and not active:
                    return run_game()
                elif event.key == pygame.K_q:
                    sys.exit()
        screen.fill(ai_settings.bg_color)
        if active:
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen, (140, 0, 100), rect, 0)
        if not active:
            Scoreboard.printS(screen, (350, 300), 'YOU ARE DEAD!', (230, 0, 0), False, 100)
            Scoreboard.printS(screen, (500, 420), 'press space to try again', (0, 0, 50), False, 30)
            Scoreboard.printS(screen, (513, 445), 'press Q to exit game', (0, 0, 50), False, 30)
        if food.rect == snake.body[0]:
            score = Scoreboard.addscore(score)
            food.remove()
            snake.addnode()
        food.set(ai_settings)
        pygame.draw.rect(screen, (0, 150, 21), food.rect, 0)
        Scoreboard.printS(screen, (50, 620), 'Scores: ' + str(score), (0, 0, 0))
        speed = levelup(score)
        active = snake.judge(ai_settings)
        pygame.display.update()
        clock(speed)
run_game()
