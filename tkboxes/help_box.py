import tkinter as tk


def help_box():
    root = tk.Tk()
    root.title('Help')

    mainFrame = tk.Frame(root)
    mainFrame.grid(column=0, row=0, sticky=(
        tk.N, tk.W, tk.E, tk.S))  # type: ignore
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.pack(pady=100, padx=100)

    tk.Label(mainFrame, text='Use your left mouse button to place start, end and barrier nodes.').grid(
        row=1, column=1)
    tk.Label(mainFrame, text='Use your right mouse button to delete a node.').grid(
        row=2, column=1)
    tk.Label(mainFrame, text='Use backspace to clear the board.').grid(
        row=3, column=1)
    tk.Label(mainFrame, text='Use c to choose the pathfinding and maze generating algorithms.').grid(
        row=4, column=1)
    tk.Label(mainFrame, text='Use space to start the pathfinding algorithm.').grid(
        row=5, column=1)
    tk.Label(mainFrame, text='Use m to start the maze generating algorithm.').grid(
        row=5, column=1)

    root.mainloop()
