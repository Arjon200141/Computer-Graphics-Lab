import matplotlib.pyplot as plt

def inside(p, cp1, cp2):
    # Return True if point p is inside the clipping edge (cp1 to cp2)
    return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) - (cp2[1] - cp1[1]) * (p[0] - cp1[0]) >= 0

def compute_intersection(p1, p2, cp1, cp2):
    # Compute intersection point of line segment p1-p2 with edge cp1-cp2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = cp1
    x4, y4 = cp2

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        return None  # lines are parallel

    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return [px, py]

def sutherland_hodgman(subject_polygon, clip_polygon):
    output_list = subject_polygon
    for i in range(len(clip_polygon)):
        input_list = output_list
        output_list = []

        cp1 = clip_polygon[i]
        cp2 = clip_polygon[(i + 1) % len(clip_polygon)]

        for j in range(len(input_list)):
            current = input_list[j]
            prev = input_list[j - 1]

            if inside(current, cp1, cp2):
                if not inside(prev, cp1, cp2):
                    inter_point = compute_intersection(prev, current, cp1, cp2)
                    if inter_point:
                        output_list.append(inter_point)
                output_list.append(current)
            elif inside(prev, cp1, cp2):
                inter_point = compute_intersection(prev, current, cp1, cp2)
                if inter_point:
                    output_list.append(inter_point)
    return output_list

def get_polygon_input(name):
    n = int(input(f"\nEnter number of vertices for {name} polygon: "))
    polygon = []
    print(f"Enter {n} vertices (x y) for {name} polygon:")
    for _ in range(n):
        x, y = map(float, input().split())
        polygon.append([x, y])
    return polygon

def plot_polygons(subject, clipper, result):
    plt.figure(figsize=(8, 8))

    # Plot Subject polygon (Blue)
    subject_closed = subject + [subject[0]]
    xs, ys = zip(*subject_closed)
    plt.plot(xs, ys, 'b-', label='Subject Polygon', linewidth=2)

    # Plot Clipping polygon (Red)
    clipper_closed = clipper + [clipper[0]]
    xc, yc = zip(*clipper_closed)
    plt.plot(xc, yc, 'r--', label='Clipping Polygon', linewidth=2)

    # Plot Clipped polygon (Green)
    if result:
        result_closed = result + [result[0]]
        xr, yr = zip(*result_closed)
        plt.plot(xr, yr, 'g-', label='Clipped Polygon', linewidth=2)
        plt.fill(xr, yr, 'green', alpha=0.3)

    plt.title("Polygon Clipping (Sutherland–Hodgman Algorithm)")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.show()

# === Main Program ===
if __name__ == "__main__":
    subject_polygon = get_polygon_input("Subject")
    clip_polygon = get_polygon_input("Clipping")

    clipped_polygon = sutherland_hodgman(subject_polygon, clip_polygon)
    print("\nClipped Polygon Coordinates:")
    for point in clipped_polygon:
        print(f"({point[0]:.2f}, {point[1]:.2f})")

    plot_polygons(subject_polygon, clip_polygon, clipped_polygon)
