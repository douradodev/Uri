line = ''
while True:
    try:
        for word in input().split():
            if word not in ['<br>', '<hr>']:
                if len(line + word.strip()) <= 80:
                    line += word + ' '
                else:
                    print(line.strip())
                    line = word + ' '                    
            elif word == '<br>':
                print(line.strip())
                line = ''
            elif word == '<hr>':
                if len(line):
                    print(line.strip())
                    line = ''
                print('-'*80)            

    except EOFError:
        if len(line):        
            print(line.strip(), end='')
        break
    