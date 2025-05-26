import matplotlib.pyplot as plt
import numpy as np

step_count = 0

def plot_polygon(points, label):
    global step_count
    x_vals = [p[0] for p in points] + [points[0][0]]
    y_vals = [p[1] for p in points] + [points[0][1]]
    plt.plot(x_vals, y_vals, marker='o', label=f"{label} (Step {step_count})")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

def get_user_shape():
    choice = input("Choose option:\n1. Default Triangle\n2. Custom Shape\nEnter 1 or 2: ")
    if choice == '1':
        print("Using default triangle...")
        return [(100, 100), (150, 200), (200, 100)]
    elif choice == '2':
        num_vertices = int(input("Enter number of vertices: "))
        points = []
        for i in range(num_vertices):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            points.append((x, y))
        return points
    else:
        print("Invalid input. Defaulting to triangle.")
        return [(100, 100), (150, 200), (200, 100)]

def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

def rotate(points, angle_deg, pivot=(0,0)):
    px, py = pivot
    angle_rad = np.radians(angle_deg)
    cos_val = np.cos(angle_rad)
    sin_val = np.sin(angle_rad)
    translated = [(x - px, y - py) for x, y in points]
    rotated = [(x * cos_val - y * sin_val, x * sin_val + y * cos_val) for x, y in translated]
    translated_back = [(x + px, y + py) for x, y in rotated]
    return translated_back

def scale(points, sx, sy, pivot=(0,0)):
    px, py = pivot
    translated = [(x - px, y - py) for x, y in points]
    scaled = [(x * sx, y * sy) for x, y in translated]
    translated_back = [(x + px, y + py) for x, y in scaled]
    return translated_back

def reflect_axis(points, axis):
    if axis == 'x':
        return [(x, -y) for x, y in points]
    elif axis == 'y':
        return [(-x, y) for x, y in points]
    elif axis == 'xy':
        return [(-x, -y) for x, y in points]
    else:
        print("Invalid axis! Use 'x', 'y', or 'xy'.")
        return points

def reflect_point(points, px, py):
    return [(2 * px - x, 2 * py - y) for x, y in points]

def shear(points, shx, shy):
    return [(x + shx * y, y + shy * x) for x, y in points]

def show_menu():
    print("\nMenu:")
    print("1. Translation")
    print("2. Rotation")
    print("3. Scaling")
    print("4. Reflection (Axis)")
    print("5. Reflection (Point)")
    print("6. Shearing")
    print("7. Exit and Show Plot")

def main():
    global step_count

    points = get_user_shape()

    px = float(input("Enter initial pivot X (default 0): ") or 0)
    py = float(input("Enter initial pivot Y (default 0): ") or 0)
    current_pivot = (px, py)

    plt.figure(figsize=(10, 8))
    plot_polygon(points, "Original")
    step_count += 1

    while True:
        show_menu()
        choice = input("Choose a transformation: ")

        if choice == '1':
            tx = float(input("Enter translation in X: "))
            ty = float(input("Enter translation in Y: "))
            points = translate(points, tx, ty)
            current_pivot = (current_pivot[0] + tx, current_pivot[1] + ty)
            print(f"\nAfter translation by ({tx}, {ty}). New pivot: {current_pivot}")
            plot_polygon(points, f'Translation {step_count}')
            step_count += 1

        elif choice == '2':
            use_current = input("Use current pivot (y/n)? ").lower()
            if use_current == 'y':
                pivot = current_pivot
            else:
                px = float(input("Enter pivot X: "))
                py = float(input("Enter pivot Y: "))
                pivot = (px, py)
            angle = float(input("Enter angle of rotation (in degrees): "))
            points = rotate(points, angle, pivot)
            print(f"\nAfter rotation by {angle}° around {pivot}: {points}")
            plot_polygon(points, f'Rotation {step_count}')
            step_count += 1

        elif choice == '3':
            sx = float(input("Enter scaling factor in X: "))
            sy = float(input("Enter scaling factor in Y: "))
            points = scale(points, sx, sy, current_pivot)
            print(f"\nAfter scaling by ({sx}, {sy}) around {current_pivot}: {points}")
            plot_polygon(points, f'Scaling {step_count}')
            step_count += 1

        elif choice == '4':
            axis = input("Enter axis for reflection (x/y/xy): ").lower()
            points = reflect_axis(points, axis)
            print(f"\nAfter reflection over {axis}-axis: {points}")
            plot_polygon(points, f'Reflection-{axis.upper()} {step_count}')
            step_count += 1

        elif choice == '5':
            px = float(input("Enter X coordinate of point: "))
            py = float(input("Enter Y coordinate of point: "))
            points = reflect_point(points, px, py)
            print(f"\nAfter reflection over point ({px}, {py}): {points}")
            plot_polygon(points, f'PtReflect {step_count}')
            step_count += 1

        elif choice == '6':
            shx = float(input("Enter shear factor in X: "))
            shy = float(input("Enter shear factor in Y: "))
            points = shear(points, shx, shy)
            print(f"\nAfter shearing ({shx}, {shy}): {points}")
            plot_polygon(points, f'Shear {step_count}')
            step_count += 1

        elif choice == '7':
            print("Exiting and displaying plot.")
            break

        else:
            print("Invalid choice. Please try again.")

    plt.title("Composite Transformation of Polygon")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    main()
