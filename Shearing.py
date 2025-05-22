import matplotlib.pyplot as plt

def shear_point(x, y, shx=0, shy=0):
    return x + shx * y, y + shy * x

def get_points():
    n = int(input("Enter number of points: "))
    return [tuple(map(float, input(f"Point {i+1} (x y): ").split())) for i in range(n)]

def shear():
    points = get_points()
    shx = float(input("Shear along X (shx): "))
    shy = float(input("Shear along Y (shy): "))
    sheared = [shear_point(x, y, shx, shy) for x, y in points]

    x1, y1 = zip(*(points + [points[0]]))
    x2, y2 = zip(*(sheared + [sheared[0]]))

    plt.figure()
    plt.plot(x1, y1, label="Original", color='blue')
    plt.plot(x2, y2, label="Sheared", color='orange')
    plt.title("2D Shearing")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    shear()
