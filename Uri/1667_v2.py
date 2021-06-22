line = ''
text_file = []
while True:
    try:
         text_file += input().split()
    except EOFError:        
        break

for word in text_file:
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
else:
    if len(line):        
        print(line.strip())