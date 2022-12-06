elf_counter = 1
best_elf = 0
most_calories = 0
calories = 0
elfs = []
with open('input_1.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            elf_counter += 1
            if calories > most_calories:
                best_elf = elf_counter
                most_calories = calories
            elfs.append(calories)
            calories = 0
        else:
            calories += int(line)

print(best_elf, most_calories)

# second part: top 3 elfs
elfs_sorted = sorted(elfs, reverse=True)
sum = sum(elfs_sorted[:3])
print(sum)

