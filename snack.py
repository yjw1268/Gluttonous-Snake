import pygame


class Snake():
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()

    def addnode(self):
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    def delnode(self):
        self.body.pop()

    def move(self):
        self.addnode()
        self.delnode()

    def judge(self, ai_settings):
        if self.body[0].x not in range(ai_settings.screen_width):
            return False
        if self.body[0].y not in range(ai_settings.screen_height):
            return False
        if self.body[0] in self.body[1:]:
            return False
        return True

    def changedirection(self, curkey):
        lr = [pygame.K_LEFT, pygame.K_RIGHT]
        ud = [pygame.K_UP, pygame.K_DOWN]
        if curkey in lr + ud:
            if (curkey in lr) and (self.dirction in lr):
                return
            if (curkey in ud) and (self.dirction in ud):
                return
            self.dirction = curkey
