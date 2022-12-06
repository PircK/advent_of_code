def move_crates(S, n, start, goal):
    # part 1
    for _ in range(n):
        crate = S[start].pop()
        S[goal].append(crate)
    return S

def move_crates_2(S, n, start, goal):
    # part 2
    crates = []
    for _ in range(n):
        crates.insert(0, S[start].pop())
    S[goal].extend(crates)
    return S

stacks = []
S = None
with open('input_5.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line.startswith('move'):
            _ , n, _ , start, _ , goal = line.split(' ')
            S = move_crates(S, int(n) ,int(start)-1, int(goal)-1)
            #S = move_crates_2(S, int(n) ,int(start)-1, int(goal)-1)
        elif '1' in line:
            n = map(int, line.split('   '))
            k = max(n)
            S = [[] for _ in range(k)]
            
            for i in stacks:
                empty = 0
                place = 0
                for j in i:
                    if j == '':
                        empty += 1
                        if empty == 4:
                            place += 1
                            empty = 0
                    else:
                        S[place].insert(0, j.strip('[').strip(']'))
                        empty = 0
                        place += 1
        else:
            s = line.split(' ')
            stacks.append(s)

# crates on top
top = ''
for i in S:
    top += i[-1]
print(top)