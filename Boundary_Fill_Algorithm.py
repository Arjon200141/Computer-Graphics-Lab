import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(10000)

# Constants for colors
FILL_COLOR = 2
BOUNDARY_COLOR = 1
BG_COLOR = 0

# Initialize screen
WIDTH, HEIGHT = 100, 100
screen = np.zeros((HEIGHT, WIDTH), dtype=int)

# Function to draw polygon edges on the screen (Bresenham's Line Algorithm)
def draw_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x2:
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                screen[y][x] = BOUNDARY_COLOR
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                screen[y][x] = BOUNDARY_COLOR
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    if 0 <= x2 < WIDTH and 0 <= y2 < HEIGHT:
        screen[y2][x2] = BOUNDARY_COLOR

# Boundary Fill Algorithm (4-connected)
def boundary_fill(x, y, fill_color, boundary_color):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return
    current = screen[y][x]
    if current != boundary_color and current != fill_color:
        screen[y][x] = fill_color
        boundary_fill(x+1, y, fill_color, boundary_color)
        boundary_fill(x-1, y, fill_color, boundary_color)
        boundary_fill(x, y+1, fill_color, boundary_color)
        boundary_fill(x, y-1, fill_color, boundary_color)

# User input
n = int(input("Enter number of polygon vertices: "))
points = []
for i in range(n):
    x, y = map(int, input(f"Enter x y of point {i+1}: ").split())
    points.append((x, y))

# Draw polygon
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    draw_line(x1, y1, x2, y2)

# Get seed point
seed_x, seed_y = map(int, input("Enter seed point (x y): ").split())

# Fill
boundary_fill(seed_x, seed_y, FILL_COLOR, BOUNDARY_COLOR)

# Display the result
plt.imshow(screen, cmap='gray')
plt.title("Boundary Fill Result")
plt.show()
