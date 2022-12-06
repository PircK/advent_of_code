priorities = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 
            'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 
            't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
            'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 
            'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 
            'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
priority = 0
with open('input_3.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        n = len(line)
        comp1, comp2 = set(line[:int(n/2)]), set(line[int(n/2):])
        common_item = comp1.intersection(comp2)
        #print(line.strip('\n'))
        #print(comp1, '   ', comp2)
        #print(common_item, priorities[list(common_item)[0]])
        priority += priorities[list(common_item)[0]]
print(priority)


# part two
group_priority = 0
i = 0
group = []
with open('input_3.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        i += 1
        group.append(line)
        if i == 3:
            i = 0
            common_item = set(group[0]).intersection(set(group[1]).intersection(set(group[2])))
            group_priority += priorities[list(common_item)[0]]
            group = []
print(group_priority)



