import numpy as np

# read data
grid = []
with open('input_8.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        grid.append(list(line))

n = len(grid)
m = len(grid[0])
visible_trees = [[0 for _ in range(m)] for _ in range(n)]

grid = np.array(grid)

# rows
for i in range(n):
    left_h = 0
    right_h = 0
    for j in range(m):
        h_left = int(grid[i][j])
        if h_left > left_h:
            left_h = h_left
            visible_trees[i][j] = 1
        h_right = int(grid[i][m-j-1])
        if h_right > right_h:
            right_h = h_right
            visible_trees[i][m-j-1] = 1

    visible_trees[i][0] = 1
    visible_trees[i][m-1] = 1

# columns
for j in range(m):
    top_h = 0
    bottom_h = 0
    for i in range(n):
        h_top = int(grid[i][j])
        if h_top > top_h:
            top_h = h_top
            visible_trees[i][j] = 1
        h_bottom = int(grid[n-i-1][j])
        if h_bottom > bottom_h:
            bottom_h = h_bottom
            visible_trees[n-i-1][j] = 1

    visible_trees[0][j] = 1
    visible_trees[n-1][j] = 1
   
# visible_trees
print(sum([sum(row) for row in visible_trees]))
    


# PART 2
# scenic view