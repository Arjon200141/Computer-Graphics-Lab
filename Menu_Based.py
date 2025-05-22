import math
import matplotlib.pyplot as plt

def translate(x, y, tx, ty):
    return x + tx, y + ty

def scale(x, y, sx, sy):
    return x * sx, y * sy

def rotate(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return xr, yr

def reflect(x, y, axis):
    if axis == 'x':
        return x, -y
    elif axis == 'y':
        return -x, y
    elif axis == 'origin':
        return -x, -y
    elif axis == 'xy':
        return y, x
    else:
        print("Invalid axis! Choose from x, y, origin, or xy.")
        return x, y

def shear(x, y, shx, shy):
    return x + shx * y, y + shy * x

def plot_points(original, transformed, title):
    plt.figure()
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)
    plt.grid(True)

    plt.plot(original[0], original[1], 'bo', label='Original Point')
    plt.plot(transformed[0], transformed[1], 'ro', label='Transformed Point')

    plt.plot([original[0], transformed[0]], [original[1], transformed[1]], 'k--', label='Transformation Line')

    plt.legend()
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.show()

def main():
    while True:
        print("\n--- 2D Transformation Menu ---")
        print("1. Translation")
        print("2. Scaling")
        print("3. Rotation")
        print("4. Reflection")
        print("5. Shearing")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '6':
            print("Exiting the program.")
            break

        x = float(input("Enter x-coordinate: "))
        y = float(input("Enter y-coordinate: "))
        original = (x, y)

        if choice == '1':
            tx = float(input("Enter translation in x (tx): "))
            ty = float(input("Enter translation in y (ty): "))
            result = translate(x, y, tx, ty)
            title = f"Translation by ({tx}, {ty})"
        elif choice == '2':
            sx = float(input("Enter scaling factor in x (sx): "))
            sy = float(input("Enter scaling factor in y (sy): "))
            result = scale(x, y, sx, sy)
            title = f"Scaling by ({sx}, {sy})"
        elif choice == '3':
            angle = float(input("Enter rotation angle in degrees: "))
            result = rotate(x, y, angle)
            title = f"Rotation by {angle}°"
        elif choice == '4':
            axis = input("Reflect about which axis? (x/y/origin/xy): ").lower()
            result = reflect(x, y, axis)
            title = f"Reflection about {axis}-axis"
        elif choice == '5':
            shx = float(input("Enter shearing factor in x (shx): "))
            shy = float(input("Enter shearing factor in y (shy): "))
            result = shear(x, y, shx, shy)
            title = f"Shearing by ({shx}, {shy})"
        else:
            print("Invalid choice! Try again.")
            continue

        print(f"Result after transformation: ({result[0]:.2f}, {result[1]:.2f})")
        plot_points(original, result, title)

if __name__ == "__main__":
    main()
