import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def continued_fraction(x, limit=100):
    """Find the continued fraction expansion of a nonterminating decimal number."""
    whole_part = int(x)
    frac_part = x - whole_part
    result = [whole_part]
    for i in range(limit):
        if frac_part == 0:
            break
        reciprocal = 1 / frac_part
        whole_part = int(reciprocal)
        frac_part = reciprocal - whole_part
        result.append(whole_part)
    return result

# define initial matrix
initial_matrix = np.zeros((25, 25**2), dtype=int)
initial_matrix[12, :] = 1

# define the function that checks and updates the matrix
def update_matrix(matrix):
    updated_matrix = matrix.copy()
    height, width = matrix.shape

    # loop over each cell in the matrix
    for i in range(height):
        for j in range(width):
            # check the number of black cells surrounding the current cell
            n_black = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x, y) != (i, j) and x >= 0 and y >= 0 and x < height and y < width:
                        if matrix[x, y] == 1:
                            n_black += 1

            # invert the cell color if a white cell borders 2 black cells
            if matrix[i, j] == 0 and n_black == 2:
                updated_matrix[i, j] = 1
            elif matrix[i, j] == 1 and (n_black == 0 or n_black > 2):
                updated_matrix[i, j] = 0

    return updated_matrix

# Set up figure and axis
fig, ax = plt.subplots()

# Set plot title
ax.set_title("Cellular Automata")

# Plot the initial matrix
im = ax.imshow(initial_matrix, cmap=plt.cm.binary)
# Define the update function
def update(frame):
    # update the matrix for the specified number of generations
    updated_matrix = update_matrix(initial_matrix)
    im.set_data(updated_matrix)
    initial_matrix[:] = updated_matrix[:]
    return [im]

# Animate the plot
num_generations = 121
ani = animation.FuncAnimation(fig, update, frames=num_generations, interval=100, blit=True)

# Show the plot
plt.show()
