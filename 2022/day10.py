cycle = 0
X = 1
strength = 0

def calculate_strength(strength, cycle, X):
    if cycle in [20,60,100,140,180,220]:
        strength += X * cycle
    return strength

with open('input_10.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line == 'noop':
            cycle += 1
            strength = calculate_strength(strength, cycle, X)
        else:
            _, V = line.split(' ')
            cycle += 1
            strength = calculate_strength(strength, cycle, X)
            cycle += 1
            strength = calculate_strength(strength, cycle, X)
            X += int(V)

print(strength)