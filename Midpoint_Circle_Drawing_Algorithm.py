import matplotlib.pyplot as plt

def draw_circle_midpoint(x_center, y_center, radius):
    x = 0
    y = radius
    p = 1 - radius

    points = []

    def plot_circle_points(xc, yc, x, y):
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

    plot_circle_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(x_center, y_center, x, y)

    return points

# Get user input
x_center = int(input("Enter x-coordinate of center: "))
y_center = int(input("Enter y-coordinate of center: "))
radius = int(input("Enter radius of the circle: "))

# Get points and plot
circle_points = draw_circle_midpoint(x_center, y_center, radius)

x_vals, y_vals = zip(*circle_points)

plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='blue', s=10)
plt.title("Midpoint Circle Drawing Algorithm")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
