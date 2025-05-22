import matplotlib.pyplot as plt
import numpy as np
from collections import deque

def flood_fill(matrix, start_row, start_col, new_color):
    rows, cols = len(matrix), len(matrix[0])
    original_color = matrix[start_row][start_col]
    if original_color == new_color:
        return matrix

    queue = deque()
    queue.append((start_row, start_col))
    matrix[start_row][start_col] = new_color

    while queue:
        r, c = queue.popleft()

        # Check 4 neighbors: up, down, left, right
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == original_color:
                matrix[nr][nc] = new_color
                queue.append((nr, nc))

    return matrix

def input_matrix():
    print("Enter matrix row-wise, separated by spaces:")
    print("Enter an empty line to finish input.")

    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        row = list(map(int, line.strip().split()))
        matrix.append(row)
    return matrix

def plot_matrices(original, filled):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(original, cmap='viridis', interpolation='none')
    ax[0].set_title('Original Matrix')
    ax[0].axis('off')

    ax[1].imshow(filled, cmap='viridis', interpolation='none')
    ax[1].set_title('Flood Filled Matrix')
    ax[1].axis('off')

    plt.show()

def main():
    matrix = input_matrix()
    if not matrix:
        print("Empty matrix input. Exiting.")
        return

    # Convert to numpy array for plotting original easily
    original_matrix = np.array(matrix)

    start_row = int(input("Enter start row (0-indexed): "))
    start_col = int(input("Enter start column (0-indexed): "))
    new_color = int(input("Enter new color (integer): "))

    if start_row < 0 or start_row >= len(matrix) or start_col < 0 or start_col >= len(matrix[0]):
        print("Invalid start point.")
        return

    filled_matrix = flood_fill(matrix, start_row, start_col, new_color)
    filled_matrix_np = np.array(filled_matrix)

    plot_matrices(original_matrix, filled_matrix_np)

if __name__ == "__main__":
    main()
