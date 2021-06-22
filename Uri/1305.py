while True:
    try:
        num = input()
        cutoff = input()

        if num[0] == '.':
            num = '0' + num
        if num[-1] == '.':
            num += '0'
        if '.' not in num:
            num += '.0'
        
        num, dec = num.split('.')[0], num.split('.')[1]
        
        while len(dec) < len(cutoff.split('.')[1]):
            dec += '0'
        while len(dec) > len(cutoff.split('.')[1]):
            cutoff += '0'
        

        if int(dec) >= int(cutoff.split('.')[1]):           
            print(int(num) + 1)
        else:
            print(num)

    except EOFError:
        break