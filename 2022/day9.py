H_x = 0
H_y = 0
T_x = 0
T_y = 0
T_positions = set()
T_positions.add((0,0))

def move(x,y,direction):
    if direction == 'D': # down
        y -= 1
    elif direction == 'U': # up
        y += 1
    elif direction == 'L': # left
        x -= 1
    elif direction == 'R': # right
        x += 1
    return x,y

with open('input_9.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        direction, distance = line.split(' ')

        for i in range(int(distance)):
            #print('H ', H_x, H_y)
            #print('T ', T_x, T_y)
            #print('-------------------')

            # move head
            H_x, H_y = move(H_x, H_y, direction)

            # move tail if needed
            dist_x = abs(H_x - T_x)
            dist_y = abs(H_y -T_y)
            if dist_x == 0 and dist_y == 0: # overlapping
                continue
            elif dist_x == 1 and dist_y == 0: # same line, next to each other
                continue
            elif dist_y == 1 and dist_x == 0: # same column, next to each other
                continue
            elif dist_y == 1 and dist_x == 1: # diagonally next to each other
                continue
            elif dist_y == 0 or dist_x == 0: # same line or column but apart
                T_x, T_y = move(T_x, T_y, direction)
            elif dist_y > 1 or dist_x > 1: # we need to do a diagonal move
                T_x, T_y = move(T_x, T_y, direction)
                if direction == 'L' or direction == 'R':
                    if T_y < H_y:
                        T_x, T_y = move(T_x, T_y, 'U')
                    else:
                        T_x, T_y = move(T_x, T_y, 'D')
                else:
                    if T_x < H_x:
                        T_x, T_y = move(T_x, T_y, 'R')
                    else:
                        T_x, T_y = move(T_x, T_y, 'L')
            T_positions.add((T_x, T_y))

#print(T_positions)
print(len(T_positions))


# part 2
pos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]  
T_positions_2 = set()
T_positions_2.add((0,0)) 
with open('input_9.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        direction, distance = line.split(' ')

        for i in range(int(distance)):

            # move head
            pos[0][0], pos[0][1] = move(pos[0][0], pos[0][1], direction)
            for j in range(1, len(pos)):
                H_x = pos[j-1][0]
                H_y = pos[j-1][1]
                T_x = pos[j][0]
                T_y = pos[j][1]

                # move tail if needed
                dist_x = abs(H_x - T_x)
                dist_y = abs(H_y - T_y)
                if dist_x == 0 and dist_y == 0: # overlapping
                    continue
                elif dist_x == 1 and dist_y == 0: # same line, next to each other
                    continue
                elif dist_y == 1 and dist_x == 0: # same column, next to each other
                    continue
                elif dist_y == 1 and dist_x == 1: # diagonally next to each other
                    continue
                elif dist_x == 0: # same column but appart
                    if H_y > T_y:
                        T_x, T_y = move(T_x, T_y, 'U')
                    else:
                        T_x, T_y = move(T_x, T_y, 'D')
                elif dist_y == 0: # same line but apart
                    if H_x > T_x:
                        T_x, T_y = move(T_x, T_y, 'R')
                    else:
                        T_x, T_y = move(T_x, T_y, 'L')
                elif dist_y > 1 or dist_x > 1: # diagonal move
                    if T_y < H_y:
                        T_x, T_y = move(T_x, T_y, 'U')
                    else:
                        T_x, T_y = move(T_x, T_y, 'D')

                    if T_x < H_x:
                        T_x, T_y = move(T_x, T_y, 'R')
                    else:
                        T_x, T_y = move(T_x, T_y, 'L')

                pos[j][0] = T_x
                pos[j][1] = T_y
                
                if j == len(pos) - 1:
                    T_positions_2.add((T_x, T_y))

print(len(T_positions_2))