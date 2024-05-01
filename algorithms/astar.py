import pygame
from queue import PriorityQueue


def h(start, end):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


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


def aStar(update_display, grid, start, end):
    # f(n) is basically g(n) + h(n)
    # g(n) is the distance from the start to the current node
    # h(n) is an estimate of the distance between two points
    end_pos = end.get_pos()
    count = 0
    open_set = PriorityQueue()
    previous_nodes = {}
    g = {pixel: float('inf') for row in grid for pixel in row}
    g[start] = 0  # this is 0 as it isn't coming from any previous node
    f = {pixel: float('inf') for row in grid for pixel in row}
    # f is the addition of g which is 0 at the strt with the h
    f[start] = h(start.get_pos(), end_pos)
    open_set.put((f[start], count, start))
    # keeps track of all items in priority queue as the builtin object can't do that
    open_set_hash = {start}

    while not open_set.empty():  # runs until all viable nodes have been in and out of the queue
        # pygame.time.Clock().tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    for row in grid:
                        for pixel in row:
                            if not pixel.is_start():
                                pixel.reset()
                                pixel.neighbours = []
                                return False

                    return False
        # returns which node we are currently checking and removes it from the priority queue
        current = open_set.get()[2]
        # removes the current node from the hased queue
        open_set_hash.remove(current)
        if current == end:  # checks if we have found the end node
            backtrack_path(previous_nodes, current, update_display, start, end)
            return True
        for neighbour in current.neighbours:
            # this is the g value for any neighbour as it is the current g plus 1 as its one away
            temp_g = g[current] + 1
            if temp_g < g[neighbour]:  # checks if it is less
                # sets the previous node of the neighbour to the current node
                previous_nodes[neighbour] = current
                g[neighbour] = temp_g  # updates the g value to the new g value
                # updates the f value to the heuristic of the neighbour and the new g value
                f[neighbour] = temp_g + h(neighbour.get_pos(), end_pos)
                if neighbour not in open_set_hash:  # checks if neighbour node not in nodes to be checked
                    count += 1  # used to determine which node to check if f values are equal
                    open_set.put((f[neighbour], count, neighbour))
                    # adds the neighbours node to PriorityQueue and hash
                    open_set_hash.add(neighbour)
                    neighbour.make_open()  # visualizes the node as being checked
        start.make_start()
        end.make_end()
        update_display()
        if current != start:
            current.make_closed()  # visualizes the node as checked and not the target node
    return False
