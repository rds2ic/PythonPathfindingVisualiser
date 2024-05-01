import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (253, 106, 2)
TURQUOISE = (64, 224, 208)


class Pixel:
    def __init__(self, row, col, width, total_rows) -> None:
        self.row = row
        self.x = row * width
        self.col = col
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.colour = WHITE
        self.neighbours = []
        self.create_borders()

    def get_pos(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.colour,
                         (self.x, self.y, self.width, self.width))

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour == GREEN

    def reset(self):
        if self.colour != YELLOW:
            self.colour = WHITE

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == TURQUOISE

    def is_path(self):
        return self.colour == PURPLE

    def is_border(self):
        return self.colour == YELLOW

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def make_border(self):
        self.colour = YELLOW

    def update_neighbours(self, grid):
        self.neighbours = []
        # checking pixel above
        if self.row > 0 and not grid[self.row-1][self.col].is_border() and not grid[self.row-1][self.col].is_barrier():
            self.neighbours.append(grid[self.row-1][self.col])
        # checking pixel to the left
        if self.col > 0 and not grid[self.row][self.col-1].is_border() and not grid[self.row][self.col-1].is_barrier():
            self.neighbours.append(grid[self.row][self.col-1])
        # checking pixel below
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_border() and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        # checking pixel to the right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_border() and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False

    def create_borders(self):
        if self.row == 0 or self.row == self.total_rows - 1 or self.col == 0 or self.col == self.total_rows - 1:
            self.colour = YELLOW
            # print(f'Pixel at {self.row}, {self.col} has a colour of {self.colour}')
