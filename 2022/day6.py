# part one
with open('input_6.txt') as f:
    line = f.readline()
    for i in range(4,len(line)):
        four = list(line[i-4:i])
        four_set = set(four)
        if len(four_set) == 4:
            print(i)
            break

# part two
with open('input_6.txt') as f:
    line = f.readline()
    for i in range(14,len(line)):
        fourteen = list(line[i-14:i])
        fourteen_set = set(fourteen)
        if len(fourteen_set) == 14:
            print(i)
            break