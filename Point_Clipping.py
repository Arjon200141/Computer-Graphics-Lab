import matplotlib.pyplot as plt

def point_clipping(xmin, ymin, xmax, ymax, x, y):
    if xmin <= x <= xmax and ymin <= y <= ymax:
        return "Inside"
    else:
        return "Outside"

# Take input from user
xmin = int(input("Enter xmin of clipping window: "))
ymin = int(input("Enter ymin of clipping window: "))
xmax = int(input("Enter xmax of clipping window: "))
ymax = int(input("Enter ymax of clipping window: "))
x = int(input("Enter x-coordinate of point: "))
y = int(input("Enter y-coordinate of point: "))

# Check point location
result = point_clipping(xmin, ymin, xmax, ymax, x, y)
print(f"The point ({x}, {y}) is {result} the clipping window.")

# Plotting
plt.figure()
plt.title("Point Clipping")
plt.xlim(min(xmin, x) - 10, max(xmax, x) + 10)
plt.ylim(min(ymin, y) - 10, max(ymax, y) + 10)

# Draw clipping window (rectangle)
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'b-', label="Clipping Window")

# Draw the point
if result == "Inside":
    plt.plot(x, y, 'go', label="Point (Inside)")  # green
else:
    plt.plot(x, y, 'ro', label="Point (Outside)")  # red

plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
