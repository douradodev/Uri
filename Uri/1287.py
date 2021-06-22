while True:
    try:
        number_str = input()
        number_str = ''.join(number_str.split(','))
        number_str = ''.join(number_str.split(',')

        is_number = True
        out_num = ''
        for num in number_str:
            if num in ['O', 'o']:
                out_num += '0'
            elif num == 'l':
                out_num += '1'
            elif num.isalpha():
                is_number = False
                break           
            else:
                out_num += num
    
        try:
            if  0 <= int(out_num) <= 2147483647 and is_number:
                print(int(out_num))
            else:
                print('error')

        except ValueError:
            print('error')

    except EOFError:
        break