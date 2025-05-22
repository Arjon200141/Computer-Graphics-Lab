import matplotlib.pyplot as plt
# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0.0, 0.0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        print(f"Clipped Line: ({x1:.2f}, {y1:.2f}) to ({x2:.2f}, {y2:.2f})")
        return (x1, y1, x2, y2)
    else:
        print("Line rejected.")
        return None

# -------- Input --------
print("Enter Clipping Window Coordinates:")
xmin = float(input("xmin: "))
ymin = float(input("ymin: "))
xmax = float(input("xmax: "))
ymax = float(input("ymax: "))

print("\nEnter Line Endpoints:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# -------- Clipping --------
result = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# -------- Plotting --------
fig, ax = plt.subplots()
# Draw clipping window
clipping_rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                              linewidth=2, edgecolor='black', facecolor='none', label='Clipping Window')
ax.add_patch(clipping_rect)

# Original line in red
plt.plot([x1, x2], [y1, y2], 'r--', label='Original Line')

# Clipped line in green
if result:
    cx1, cy1, cx2, cy2 = result
    plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label='Clipped Line')

# Labels and display
plt.title('Cohen–Sutherland Line Clipping')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
