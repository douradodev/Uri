not_fisrt_loop = False 
while True:
    try:        
        if not_fisrt_loop:
            print()
        string = input()

        new_string = ''

        for char in string[:len(string)-1]:
            new_string += char + ' '
        else:
            new_string += string[-1]

        for i in range(len(string)):           
            print(' '*i + new_string)
            new_string = new_string[:len(new_string)-2]
        
        not_fisrt_loop = True
    except EOFError:
        break
