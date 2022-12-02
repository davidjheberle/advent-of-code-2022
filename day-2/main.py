def print_score(input_file):
    score = 0

    with open(input_file) as file:
        for line in file:
            chars = line.strip().split(' ')
            score += calc_score(chars[1], chars[0])

    print(score)


def calc_score(player, opponent):
    score = 0

    if player == 'X':
        score += 1
        if opponent == 'A':
            score += 3
        elif opponent == 'C':
            score += 6
    elif player == 'Y':
        score += 2
        if opponent == 'B':
            score += 3
        elif opponent == 'A':
            score += 6
    elif player == 'Z':
        score += 3
        if opponent == 'C':
            score += 3
        elif opponent == 'B':
            score += 6

    return score


def print_score_1(input_file):
    score = 0

    with open(input_file) as file:
        for line in file:
            chars = line.strip().split(' ')
            score += calc_score_1(chars[1], chars[0])

    print(score)


def calc_score_1(round_result, opponent):
    score = 0
    player = ''

    if round_result == 'X':
        if opponent == 'A':
            player = 'C'
        elif opponent == 'B':
            player = 'A'
        elif opponent == 'C':
            player = 'B'
    elif round_result == 'Y':
        score += 3
        player = opponent
    elif round_result == 'Z':
        score += 6
        if opponent == 'A':
            player = 'B'
        elif opponent == 'B':
            player = 'C'
        elif opponent == 'C':
            player = 'A'

    if player == 'A':
        score += 1
    elif player == 'B':
        score += 2
    elif player == 'C':
        score += 3

    return score


if __name__ == '__main__':
    print_score("./input.txt")
    print_score_1("./input.txt")
