import tkinter as tk

PATHFINDING_ALGORITHMS = {'A*', 'Djikstras'}
MAZE_GENERATING_ALGORITHMS = {
    'Recursive Division'}


def algorithms_input_box(update_display, prev_pathfinding_algorithm='A*', prev_maze_algorithm='Recursive Division'):
    update_display()
    algorithm_get = ''

    root = tk.Tk()
    root.title('Algorithm')

    mainFrame = tk.Frame(root)
    mainFrame.grid(column=0, row=0, sticky=(
        tk.N, tk.W, tk.E, tk.S))  # type: ignore
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.pack(pady=100, padx=100)

    pathfinding_algorithm = tk.StringVar(root)
    pathfinding_algorithm.set(prev_pathfinding_algorithm)

    pathfinding_popupMenu = tk.OptionMenu(
        mainFrame, pathfinding_algorithm, *PATHFINDING_ALGORITHMS)
    tk.Label(mainFrame, text='Choose a pathfinding algorithm:').grid(
        row=1, column=1)
    pathfinding_popupMenu.grid(row=2, column=1)

    maze_algorithm = tk.StringVar(root)
    maze_algorithm.set(prev_maze_algorithm)
    maze_popupMenu = tk.OptionMenu(
        mainFrame, maze_algorithm, *MAZE_GENERATING_ALGORITHMS)
    tk.Label(mainFrame, text='Choose a maze generating algorithm').grid(
        row=3, column=1)
    maze_popupMenu.grid(row=4, column=1)

    tk.Button(mainFrame, text='Confirm',
              command=root.destroy).grid(row=5, column=1)

    tk.Label(mainFrame, text='Press \'h\' when in the program for help.').grid(
        row=6, column=1)

    def change_dropdown(*args):
        pathfinding_algorithm_get = pathfinding_algorithm.get()
        maze_algorithm_get = maze_algorithm.get()
    pathfinding_algorithm.trace('w', change_dropdown)
    maze_algorithm.trace('w', change_dropdown)
    root.mainloop()
    pathfinding_algorithm_get = pathfinding_algorithm.get()
    maze_algorithm_get = maze_algorithm.get()
    return pathfinding_algorithm_get, maze_algorithm_get
