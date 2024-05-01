import pygame
from queue import PriorityQueue


def backtrack_path(previous_nodes, current, update_display, start, end):
    # keeps checking if the current node we are checking is in previous nodes. The first current is the end node
    while current in previous_nodes:
        current = previous_nodes[current]  # sets current to the node before
        # print(current.get_pos())
        current.make_path()  # sets current to a path
        start.make_start()
        end.make_end()
        pygame.time.delay(20)
        update_display()


def djikstras(update_display, grid, start, end):
    # djikstras doesnt use the h(n) function so is not as directed as a star
    count = 0
    open_set = PriorityQueue()
    previous_nodes = {}
    g = {pixel: float('inf') for row in grid for pixel in row}
    g[start] = 0
    open_set.put((g[start], count, start))
    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            backtrack_path(previous_nodes, current, update_display, start, end)
            return True
        for neighbour in current.neighbours:
            neighbours_g = g[current] + 1
            if neighbours_g < g[neighbour]:
                previous_nodes[neighbour] = current
                g[neighbour] = neighbours_g
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((g[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        start.make_start()
        end.make_end()
        update_display()
        if current != start:
            current.make_closed()
    return False
