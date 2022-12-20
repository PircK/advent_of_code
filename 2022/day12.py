from dijkstar import Graph, find_path

grid = []

# read grid
with open('input_12.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        grid.append(line)

# find start and goal
goal = None
start = None
for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        elem = row[j]
        if elem == 'E':
            goal = (i,j)
        elif elem == 'S':
            start = (i,j)


altitudes = {'S': 0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 
            'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 
            't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'E':27}

# find all possible moves
moves = {}
moves[goal] = []
n = len(grid) # rows
m = len(grid[0]) # columns
for i in range(n):
    row = grid[i]
    for j in range(m):
        elem = row[j]
        altitude = altitudes[elem]
        moves[(i,j)] = []
        for move in [(0,-1), (0,1), (-1,0), (1,0)]:
            if i + move[0] > n - 1 or i + move[0] < 0 or j + move[1] > m - 1 or j + move[1] < 0:
                continue
            else:
                e = grid[i + move[0]][j + move[1]]
                alt = altitudes[e]
                if altitude == alt or altitude + 1 == alt:
                    moves[(i,j)].append(move)
                
print(moves)
# find optimal path
graph = Graph()
for k in moves.keys():
    node = k[0] * m + k[1] + 1
    for move in moves[k]:
        new_pos = (k[0] + move[0], k[1] + move[1])
        new_node = new_pos[0] * m + new_pos[1] + 1
        graph.add_edge(node, new_node, 1)

start_node = start[0] * m + start[1] + 1
goal_node = goal[0] * m + goal[1] + 1
path = find_path(graph, start_node, goal_node)

print(path)





