import numpy as np
import tkinter as tk
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

#input
x = np.e**1/3
n = 27
cf = continued_fraction(x, n**2)
a = np.array(cf[:n**2]).reshape((n, n))

# Set NumPy print options for better readability
np.set_printoptions(threshold=np.inf, linewidth=200)

# Custom print format
format_str = " ".join(["{:2d}" for _ in range(n)])
for row in a:
    print(format_str.format(*row))

# Convert array to bitwise representation
a_bits = np.unpackbits(a.astype('uint8'), axis=1)

# Set up Tkinter window and table
root = tk.Tk()
table = tk.Frame(root)

# Create table header
header = tk.Label(table, text="Bitwise representation of array")
header.grid(row=0, column=0, columnspan=8)

# Create table rows
for i, row in enumerate(a_bits):
    for j, bit in enumerate(row):
        label = tk.Label(table, text=str(bit))
        label.grid(row=i+1, column=j)

# Pack table and start mainloop
table.pack()
root.mainloop()