for _ in range(int(input())):
    line = input().split()
    result = []

    biggest = 0
    for word in line:
        if len(word) > biggest:
            biggest = len(word)
    
    idx = 0
    while len(result) < len(line):
        for word in line:
            if len(word) == biggest:
                result.append(word)
        else:
            biggest -= 1
    
    print(" ".join(result))


