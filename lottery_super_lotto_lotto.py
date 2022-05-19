import random


def lottery_card():
    first_area = list(range(1, 38))
    first = random.sample(first_area, 6)
    second_area = list(range(1, 8))
    second = random.sample(second_area, 1)

    first.sort()
    second.sort()

    for first_six in first:
        print('%02d' % first_six, end=' ')

    print(end='      ')

    for second_one in second:
        print('%02d' % second_one, end=' ')

    print('')


bet_number = input('Please enter a number want to bet:\n')
for bets in bet_number:
    lottery_card()
