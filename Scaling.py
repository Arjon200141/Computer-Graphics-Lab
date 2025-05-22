import matplotlib.pyplot as plt

def scale_point(x, y, sx, sy):
    return x * sx, y * sy

def get_points():
    n = int(input("Enter number of points: "))
    return [tuple(map(float, input(f"Point {i+1} (x y): ").split())) for i in range(n)]

def scale():
    points = get_points()
    sx = float(input("Scale factor X (sx): "))
    sy = float(input("Scale factor Y (sy): "))
    scaled = [scale_point(x, y, sx, sy) for x, y in points]

    x1, y1 = zip(*(points + [points[0]]))
    x2, y2 = zip(*(scaled + [scaled[0]]))

    plt.figure()
    plt.plot(x1, y1, label="Original", color='blue')
    plt.plot(x2, y2, label="Scaled", color='green')
    plt.title("2D Scaling")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    scale()
