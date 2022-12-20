moves = []
pos_val = {}
val_pos = {}
current_pos = 0
with open('input_20.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        moves.append(int(line))
        pos_val[current_pos] = int(line)
        val_pos[int(line)] = current_pos
        current_pos += 1

n = len(moves)
for m in moves:
    print(m)
    p = val_pos[m]

    if m < 0:
        m += n-1
    
    for i in range(0, m):
        pos1 = (p + i) % n
        pos2 = (p + i + 1) % n
        val1 = pos_val[pos1]
        val2 = pos_val[pos2]
        pos_val[pos1] = val2 
        pos_val[pos2] = val1
        val_pos[val1] += 1
        val_pos[val2] -= 1
    
    print(pos_val)

index = val_pos[0]
numbers = [(index + i) % n for i in [1000, 2000, 3000]]

sum = 0
for i in numbers:
    sum += pos_val[i]
print(sum)

    
