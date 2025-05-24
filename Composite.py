import math
import numpy as np
import matplotlib.pyplot as plt

def get_translation_matrix(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def get_scaling_matrix(sx, sy):
    return np.array([[sx, 0,  0],
                     [0,  sy, 0],
                     [0,  0,  1]])

def get_rotation_matrix(angle):
    rad = math.radians(angle)
    cos_theta = math.cos(rad)
    sin_theta = math.sin(rad)
    return np.array([[cos_theta, -sin_theta, 0],
                     [sin_theta,  cos_theta, 0],
                     [0,         0,         1]])

def apply_transformation(points, transformation_matrix):
    transformed_points = []
    for x, y in points:
        vec = np.array([x, y, 1])
        result = np.dot(transformation_matrix, vec)
        transformed_points.append((result[0], result[1]))
    return transformed_points

def print_points(points, title):
    print(f"\n{title}")
    for i, (x, y) in enumerate(points):
        print(f"Point {i + 1}: ({x:.2f}, {y:.2f})")

def plot_points(original, transformed):
    # Extract coordinates
    ox, oy = zip(*original)
    tx, ty = zip(*transformed)

    # Plot original points
    plt.figure(figsize=(8, 6))
    plt.plot(ox + (ox[0],), oy + (oy[0],), 'bo-', label='Original Shape')  # Close the shape
    plt.plot(tx + (tx[0],), ty + (ty[0],), 'ro-', label='Transformed Shape')  # Close the shape

    plt.title('Composite Transformation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

# Input points
n = int(input("Enter number of points: "))
points = []
for i in range(n):
    x = float(input(f"Enter x for point {i+1}: "))
    y = float(input(f"Enter y for point {i+1}: "))
    points.append((x, y))

composite_matrix = np.identity(3)

while True:
    print("\nChoose transformation:")
    print("1. Translation")
    print("2. Scaling")
    print("3. Rotation")
    print("4. Apply composite transformation and plot")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        tx = float(input("Enter translation along X (tx): "))
        ty = float(input("Enter translation along Y (ty): "))
        T = get_translation_matrix(tx, ty)
        composite_matrix = np.dot(T, composite_matrix)

    elif choice == '2':
        sx = float(input("Enter scaling factor along X (sx): "))
        sy = float(input("Enter scaling factor along Y (sy): "))
        S = get_scaling_matrix(sx, sy)
        composite_matrix = np.dot(S, composite_matrix)

    elif choice == '3':
        angle = float(input("Enter rotation angle in degrees: "))
        R = get_rotation_matrix(angle)
        composite_matrix = np.dot(R, composite_matrix)

    elif choice == '4':
        final_points = apply_transformation(points, composite_matrix)
        print_points(points, "Original Points")
        print_points(final_points, "Transformed Points")
        plot_points(points, final_points)
        break

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
