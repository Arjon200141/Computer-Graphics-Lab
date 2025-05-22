import matplotlib.pyplot as plt
import math

def rotate_point(x, y, angle_deg):
    rad = math.radians(angle_deg)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

def get_points():
    n = int(input("Enter number of points: "))
    return [tuple(map(float, input(f"Point {i+1} (x y): ").split())) for i in range(n)]

def rotate():
    points = get_points()
    angle = float(input("Rotation angle (degrees): "))
    direction = input("Direction (clockwise/anticlockwise): ").lower()
    if direction == "clockwise":
        angle = -angle

    rotated = [rotate_point(x, y, angle) for x, y in points]

    x1, y1 = zip(*(points + [points[0]]))
    x2, y2 = zip(*(rotated + [rotated[0]]))

    plt.figure()
    plt.plot(x1, y1, label="Original", color='blue')
    plt.plot(x2, y2, label=f"Rotated {angle}°", color='green')
    plt.title("2D Rotation")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    rotate()
