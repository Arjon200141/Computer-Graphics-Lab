import matplotlib.pyplot as plt
import numpy as np

# Take input from the user
a = float(input("Enter the semi-major axis (a): "))
b = float(input("Enter the semi-minor axis (b): "))

# Generate values for theta from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for the ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plot the ellipse
plt.figure(figsize=(6,6))
plt.plot(x, y, label=f"Ellipse: a={a}, b={b}")
plt.title("Ellipse Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.axis('equal')  # Equal scaling on both axes
plt.legend()
plt.show()
