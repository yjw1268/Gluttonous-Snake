import pygame


class Scoreboard():
    def __init__(self):
        self.scores = 0
        self.addscore()

    def addscore(score):
        add = 50
        score += add
        return score

    def printS(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
        cur_font = pygame.font.SysFont("宋体", font_size)
        cur_font.set_bold(font_bold)
        cur_font.set_italic(font_italic)
        text_fmt = cur_font.render(text, 1, color)
        screen.blit(text_fmt, pos)
