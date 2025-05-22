import matplotlib.pyplot as plt

def DDA_line(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    # Calculate increment
    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

# Get user input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Get DDA line points
line_points = DDA_line(x1, y1, x2, y2)

# Separate x and y for plotting
x_coords, y_coords = zip(*line_points)

# Plotting
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, marker='o', color='blue')
plt.title("DDA Line Drawing")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
