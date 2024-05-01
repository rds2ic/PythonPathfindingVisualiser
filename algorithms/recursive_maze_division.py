import pygame
import math
import random


def recursive_division_maze_generation(grid, update_display, row_start, row_end, col_start, col_end, orientation, surrounding_walls, start, end):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    try:
        # MUST FIX LIST OUT OF INDEX ERROR
        # REFRENCE https://github.com/clementmihailescu/Pathfinding-Visualizer/blob/master/public/browser/mazeAlgorithms/recursiveDivisionMaze.js
        # REFRENCE https://github.com/clementmihailescu/Pathfinding-Visualizer/blob/master/public/browser/board.js
        if row_end < row_start or col_end < col_start:
            return

        if not surrounding_walls:
            for row in grid:
                for pixel in row:
                    if pixel != start and pixel != end:
                        r = pixel.row
                        c = pixel.col
                        if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid) - 1:
                            pixel.make_barrier()
                            update_display()
        surrounding_walls = True
        # grid rows and cols stored in a way that each array in the grid stores a column and in each of those colmn arrays stores a pixe l so to index a pixel at row r and col c you do grid[c][r]
        if orientation == 'horizontal':
            possible_rows = [i for i in range(row_start, row_end + 1, 2)]
            possible_cols = [i for i in range(col_start - 1, col_end + 2, 2)]
            # int(random.random() * len(possible_rows))
            random_row_index = math.floor(random.random() * len(possible_rows))
            # int(random.random() * len(possible_cols))
            random_col_index = math.floor(random.random() * len(possible_cols))
            current_row = possible_rows[random_row_index]
            random_col = possible_cols[random_col_index]
            for row in grid:
                for pixel in row:
                    c = pixel.row
                    r = pixel.col
                    if r == current_row and c != random_col and c >= col_start - 1 and c <= col_end + 1:
                        if not pixel.is_start() and not pixel.is_end():
                            pixel.make_barrier()
                            update_display()
            if current_row - 2 - row_start > col_end - col_start:
                recursive_division_maze_generation(grid, update_display, row_start,
                                                   current_row - 2, col_start, col_end, orientation, surrounding_walls, start, end)
            else:
                recursive_division_maze_generation(grid, update_display, row_start,
                                                   current_row - 2, col_start, col_end, 'vertical', surrounding_walls, start, end)
            if row_end - current_row + 2 > col_end - col_start:
                recursive_division_maze_generation(grid, update_display, current_row + 2, row_end,
                                                   col_start, col_end, orientation, surrounding_walls, start, end)
            else:
                recursive_division_maze_generation(grid, update_display, current_row + 2, row_end,
                                                   col_start, col_end, "vertical", surrounding_walls, start, end)
        else:
            possible_cols = [i for i in range(col_start, col_end + 1, 2)]
            possible_rows = [i for i in range(row_start - 1, row_end + 2, 2)]

            # int(random.random() * len(possible_cols))
            random_col_index = math.floor(random.random() * len(possible_cols))
            # int(random.random() * len(possible_rows))
            random_row_index = math.floor(random.random() * len(possible_rows))

            current_col = possible_cols[random_col_index]
            random_row = possible_rows[random_row_index]

            for row in grid:
                for pixel in row:
                    c = pixel.row
                    r = pixel.col
                    if c == current_col and r != random_row and r >= row_start - 1 and r <= row_end + 1:
                        if not pixel.is_start() and not pixel.is_end():
                            pixel.make_barrier()
                            update_display()

            if row_end - row_start > current_col - 2 - col_start:
                recursive_division_maze_generation(grid, update_display, row_start, row_end, col_start,
                                                   current_col - 2, "horizontal", surrounding_walls, start, end)
            else:
                recursive_division_maze_generation(grid, update_display, row_start, row_end, col_start,
                                                   current_col - 2, orientation, surrounding_walls, start, end)
            if row_end - row_start > col_end - current_col + 2:
                recursive_division_maze_generation(grid, update_display, row_start, row_end,
                                                   current_col + 2, col_end, "horizontal", surrounding_walls, start, end)
            else:
                recursive_division_maze_generation(grid, update_display, row_start, row_end,
                                                   current_col + 2, col_end, orientation, surrounding_walls, start, end)
    except:
        pass
