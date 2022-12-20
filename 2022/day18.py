neigbours = {}
with open('input_18.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        x,y,z = map(int, line.split(','))
        N = 0
        for n in neigbours.keys():
            nx, ny, nz = n
            if abs(nx - x) + abs(ny - y) + abs(nz - z) == 1:
                neigbours[(nx, ny, nz)] += 1
                N += 1
        neigbours[(x,y,z)] = N
#print(neigbours)

sides = 0
for n in neigbours.keys():
    value = neigbours[n]
    sides += (6 - value)

print(sides)