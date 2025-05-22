import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

def draw_line(x1, y1, x2, y2):
    points = bresenham_line(x1, y1, x2, y2)

    x_coords, y_coords = zip(*points)

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, color='blue', marker='o', linestyle='-')  # Line now visible
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# User Input
try:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    draw_line(x1, y1, x2, y2)
except ValueError:
    print("Please enter valid integer coordinates.")
