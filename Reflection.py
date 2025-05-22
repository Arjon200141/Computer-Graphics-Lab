import matplotlib.pyplot as plt

def reflect_shape(points, mode):
    if mode == "x":
        return [(x, -y) for x, y in points]
    elif mode == "y":
        return [(-x, y) for x, y in points]
    elif mode == "origin":
        return [(-x, -y) for x, y in points]
    else:
        raise ValueError("Invalid reflection mode")

def get_points():
    n = int(input("Enter number of points: "))
    return [tuple(map(float, input(f"Point {i+1} (x y): ").split())) for i in range(n)]

def reflect():
    points = get_points()
    mode = input("Reflection axis (x/y/origin): ").lower()
    reflected = reflect_shape(points, mode)

    x1, y1 = zip(*(points + [points[0]]))
    x2, y2 = zip(*(reflected + [reflected[0]]))

    plt.figure()
    plt.plot(x1, y1, label="Original", color='blue')
    plt.plot(x2, y2, label=f"Reflected over {mode}", color='purple')
    plt.title("2D Reflection")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    reflect()
