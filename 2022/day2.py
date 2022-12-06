# scores: rock = 1, paper = 2, scissors = 3, loss = 0, draw = 3, win = 6
score = 0
with open('input_2.txt') as f:
    for line in f.readlines():
        opp, me = line.strip('\n').split(' ')
        if opp == 'A': # rock
            if me == 'X': # rock
                score += 1
                score += 3 # draw
            elif me == 'Y': # paper
                score += 2
                score += 6 # win
            elif me == 'Z': # scissors
                score += 3

        elif opp == 'B': # paper
            if me == 'X': # rock
                score += 1
            elif me == 'Y': # paper
                score += 2
                score += 3
            elif me == 'Z': # scissors
                score += 3
                score += 6

        elif opp == 'C': # scissors
            if me == 'X': # rock
                score += 1
                score += 6
            elif me == 'Y': # paper
                score += 2
            elif me == 'Z': # scissors
                score += 3
                score += 3
print(score)


# second part
# X = loss, Y = draw, Z = win
# rock = 1, paper = 2, scissors = 3, loss = 0, draw = 3, win = 6
correct_score = 0
with open('input_2.txt') as f:
    for line in f.readlines():
        opp, me = line.strip('\n').split(' ')
        if opp == 'A': # rock
            if me == 'X': # loss
                correct_score += 3 # scissors 
            elif me == 'Y': # draw
                correct_score += 1
                correct_score += 3
            elif me == 'Z': # win
                correct_score += 2
                correct_score += 6

        elif opp == 'B': # paper
            if me == 'X': # loss
                correct_score += 1
            elif me == 'Y': # draw
                correct_score += 2
                correct_score += 3
            elif me == 'Z': # win
                correct_score += 3
                correct_score += 6

        elif opp == 'C': # scissors
            if me == 'X': # loss
                correct_score += 2
            elif me == 'Y': # draw
                correct_score += 3
                correct_score += 3
            elif me == 'Z': # win
                correct_score += 1
                correct_score += 6
print(correct_score)