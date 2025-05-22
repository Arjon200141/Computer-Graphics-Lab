import matplotlib.pyplot as plt

def translate_point(x, y, tx, ty):
    return x + tx, y + ty

def get_points():
    n = int(input("Enter number of points: "))
    return [tuple(map(float, input(f"Point {i+1} (x y): ").split())) for i in range(n)]

def translate():
    points = get_points()
    tx = float(input("Translation along x (tx): "))
    ty = float(input("Translation along y (ty): "))
    translated = [translate_point(x, y, tx, ty) for x, y in points]

    x1, y1 = zip(*(points + [points[0]]))
    x2, y2 = zip(*(translated + [translated[0]]))

    plt.figure()
    plt.plot(x1, y1, label="Original", color='blue')
    plt.plot(x2, y2, label="Translated", color='red')
    plt.title("2D Translation")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    translate()
