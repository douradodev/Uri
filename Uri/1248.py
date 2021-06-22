for _ in range(int(input())):
    diet = set(input())
    break_lunch = set(input() + input())
    dinner = ''
    cheater = False

    for char in break_lunch:
        if char not in diet:
            cheater = True
            break
    else:
        dinner = sorted(set(diet) - set(break_lunch))

    if cheater:
        print('CHEATER')
    else:
        print("".join(dinner))
