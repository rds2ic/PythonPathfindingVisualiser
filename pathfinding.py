import pygame

# importing all self built modules
from grid import Grid

from algorithms.astar import aStar
from algorithms.djikstras import djikstras
from algorithms.recursive_maze_division import recursive_division_maze_generation
from algorithms.bidirectional import bidirectional

from tkboxes.algorithms_input_box import algorithms_input_box
from tkboxes.help_box import help_box

# pygame setup
pygame.init()
WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinding')


def update_display(win, grid):
    # draws everything to the screen
    grid.draw(win)
    pygame.display.update()


def get_clicked_pos(pos, rows):
    # calculates row and col of mouse clicked positions
    x, y = pos
    width = WIDTH // rows
    row = x // width
    col = y // width
    return row, col


PATHFINDING_ALGORITHMS = {'A*': aStar, 'Djikstras': djikstras}
MAZE_GENERATING_ALGORITHMS = {
    'Recursive Division': recursive_division_maze_generation}


def main(win, rows):
    grid = Grid(rows, WIDTH)
    run = True
    start = None
    end = None
    started = False
    algorithm_str, maze_str = algorithms_input_box(lambda: update_display(
        win, grid))
    algorithm = PATHFINDING_ALGORITHMS[algorithm_str]
    maze = MAZE_GENERATING_ALGORITHMS[maze_str]
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                # print('Mouse Clicked')
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows)
                pixel = grid.grid[row][col]
                # changing the value of the pixel
                if not pixel.is_border():
                    if not start and pixel != end:
                        start = pixel
                        start.make_start()
                    elif not end and pixel != start:
                        end = pixel
                        end.make_end()
                    elif pixel != start and pixel != end:
                        pixel.make_barrier()
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows)
                pixel = grid.grid[row][col]
                # resetting the pixel
                if not pixel.is_border():
                    pixel.reset()
                    if pixel == start:
                        start = None
                    if pixel == end:
                        end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started and start and end:
                    # starts pathfinding algorithm
                    for row in grid.grid:
                        for pixel in row:
                            if pixel.is_closed() or pixel.is_open() or pixel.is_path():
                                pixel.reset()
                            pixel.update_neighbours(grid.grid)
                    started = True
                    algorithm(lambda: update_display(
                        win, grid), grid.grid, start, end)
                    started = False
                if event.key == pygame.K_BACKSPACE and not started:
                    # clears screen
                    for row in grid.grid:
                        for pixel in row:
                            if not pixel.is_border():
                                pixel.reset()
                                pixel.neighbours = []
                                pixel.create_borders()
                    start = None
                    end = None
                if event.key == pygame.K_c and not started:
                    # brings ui box for changing algorithms
                    for row in grid.grid:
                        for pixel in row:
                            if pixel.is_closed() or pixel.is_open() or pixel.is_path():
                                pixel.reset()
                    algorithm_str, maze_str = algorithms_input_box(
                        lambda: update_display(win, grid), algorithm_str)
                    algorithm = PATHFINDING_ALGORITHMS[algorithm_str]
                    maze = MAZE_GENERATING_ALGORITHMS[maze_str]
                if event.key == pygame.K_m:
                    # generates maze using maze generation algorithm
                    for row in grid.grid:
                        for pixel in row:
                            pixel.reset()
                            pixel.update_neighbours(grid.grid)
                    start = None
                    end = None
                    maze(
                        grid.grid, lambda: update_display(
                            win, grid), 1, rows - 1, 1, rows - 1, 'horizontal', False, start, end)
                if event.key == pygame.K_h:
                    # provides help box
                    help_box()

        update_display(win, grid)


if __name__ == "__main__":
    main(WIN, 50)
