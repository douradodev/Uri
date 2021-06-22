for _ in range(int(input())):
    number_students = int(input())
    students = input().split()
    att = input().split()

    not_okay = []
    total = 0
    for idx in range(number_students):
        P, A = 0, 0
        for c in att[idx]:
            if c == 'A':
                A += 1
            elif c == 'P':
                P += 1
            total += 1
        else:
            if P*(total/4) < A*((3*total)/4):
                not_okay.append(students[idx])

    print(' '.join(not_okay))