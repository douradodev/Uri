more_loop = False
instance = 1
while True:    
    signature = input()
    if int(signature) == 0:
        break
    
    seq = input()
    
    if more_loop:
        print()
    print('Instancia {}'.format(instance))
    print('verdadeira' if signature in seq else 'falsa')

    instance += 1
    more_loop = True