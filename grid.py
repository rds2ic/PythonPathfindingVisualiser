import pygame
from pixel import Pixel


class Grid:
    def __init__(self, rows, width) -> None:
        self.rows = rows
        self.width = width
        self.grid = [[Pixel(row, col, width//rows, rows)
                      for col in range(rows)] for row in range(rows)]

    def draw(self, win):
        width = self.width // self.rows
        for row in self.grid:
            for pixel in row:
                pixel.draw(win)
        for i in range(self.rows):
            pygame.draw.line(win, (128, 128, 128),
                             (0, i * width), (self.width, i * width))
            for j in range(self.rows):
                pygame.draw.line(win, (128, 128, 128),
                                 (j * width, 0), (j * width, self.width))
