﻿# Python Pathfinding Visuzalizer

Uses pygame to visualize different pathfinding algorithms

# How to use

A 50x50 grid will be drawn on screen. Technically the usable grid will be 48x48 as the outer layers are borders.
You can place the start and ending nodes by pressing your mouse button. After the start and end nodes have been placed,
you can start adding barriers. You can right click a node to delete it. After you are happy with something you have drawn,
press space to start the algorithm. You can press backspace to clear the grid. If you press the a key, a maze will be generated.
Right now it is a bit clunky and doesnt work very well. You can also press the c key to change pathfinding and maze generating algorithms
(currently only one maze generating algorithm).

# Requirments

This was written in python 3.8.5. Other than that, you must have pygame installed. This can be done with the command 'pip install pygame' on windows,
and may vary on other systems. To run this use the pathfinding.py file.
