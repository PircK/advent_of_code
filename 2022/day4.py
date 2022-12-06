included = 0
with open('input_4.txt') as f:
    for line in f.readlines():
        elf1, elf2 = line.strip('\n').split(',')
        a,b = map(int, elf1.split('-'))
        c,d = map(int, elf2.split('-'))
        if a >= c and b <= d: # a b within c d
            included += 1
        elif c >= a and d <= b: # c d within a b
            included += 1
print(included)

# part two
overlap = 0
with open('input_4.txt') as f:
    for line in f.readlines():
        elf1, elf2 = line.strip('\n').split(',')
        a,b = map(int, elf1.split('-'))
        c,d = map(int, elf2.split('-'))
        if b < c or d < a:
            continue
        else:
            overlap += 1
print(overlap)