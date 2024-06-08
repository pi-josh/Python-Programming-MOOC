# Write your solution here
n = int(input("Layers: "))

size = 2 * n - 1
    
# Create an empty grid
grid = []
for i in range(size):
    grid.append([''] * size)

# Fill the grid with the appropriate letters
for layer in range(n):
    letter = chr(ord('A') + (n - layer - 1))
    for i in range(layer, size - layer):
        # Top row
        grid[layer][i] = letter
        # Bottom row
        grid[size - layer - 1][i] = letter
        # Left column
        grid[i][layer] = letter
        # Right column
        grid[i][size - layer - 1] = letter

# Print the grid
for row in grid:
    print("".join(row))