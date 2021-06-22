for _ in range(int(input())):
    msg = ''
    check_first = True

    for char in input():
        if len(msg):
            if char.isalpha() and check_first:
                msg += char
                check_first = False
            elif not char.isalpha():
                check_first = True
        else:
            if char.isalpha():
                msg += char
                check_first = False
    
    print(msg)