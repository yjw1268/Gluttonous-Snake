import pygame
import random


class Food():
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)

    def remove(self):
        self.rect.x = -25

    def set(self, ai_settings):
        if self.rect.x == -25:
            allpos = []
            for pos in range(25, ai_settings.screen_width - 25, 25):
                for pos in range(25, ai_settings.screen_height - 25, 25):
                    allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            print(self.rect)
