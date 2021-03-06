import pygame
from pygame.locals import *
from numpy.random import randint


class Ball(pygame.sprite.Sprite):
    image = pygame.Surface((8, 8))
    image.fill((255, 255, 255))

    def __init__(self, screen, screen_height, screen_width, player1, player2):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.SCR_WID = screen_width
        self.SCR_HEI = screen_height
        self.player1, self.player2 = player1, player2
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.SCR_WID / 2, self.SCR_HEI / 2
        sign_x = randint(0, 2)
        sign_y = randint(0, 2)
        speed = randint(5, 7)
        self.speed_x = (-1 ** sign_x) * speed
        self.speed_y = (-1 ** sign_y) * speed
        self.size = 8

    def restart(self):
        self.__init__(self.screen, self.SCR_HEI, self.SCR_HEI,
                      self.player1, self.player2)

    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0:
            self.speed_y *= -1
        elif self.rect.y >= self.SCR_HEI - self.size:
            self.speed_y *= -1

        if self.rect.x <= 0:
            self.restart()
            self.player1.score += 1
        elif self.rect.x >= self.SCR_WID - self.size:
            self.restart()
            self.speed_x = 3
            self.player2.score += 1

        if (self.player1.x - self.player1.padWid <= self.rect.x
           <= self.player1.x + self.player1.padWid):

            if (self.player1.y - (self.player1.padHei / 2) + 22 <= self.rect.y
                    <= self.player1.y + self.player1.padHei):
                self.speed_x *= -1

        if self.rect.x >= self.player2.x - self.player2.padWid:
            if (self.player2.y - (self.player2.padHei / 2) + 22 <= self.rect.y
                    <= self.player2.y + self.player2.padHei):
                self.speed_x *= -1

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.rect.x, self.rect.y, self.size, self.size))