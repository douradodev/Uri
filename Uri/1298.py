check_cpf = True
add_decimal = False
dec_count = 0
decimals = '0123456789'
cpf = ''
value01 = '0'
value02 = '0'

line_01 = raw_input()
line_02 = raw_input()

for char in line_01:
    if len(cpf) == 11:
        check_cpf = False
    
    if check_cpf:
        if char in decimals:
            cpf += char
    else:        

        if char in decimals:
            value01 += char
            if add_decimal:
                dec_count += 1
                if dec_count == 2:
                    break

        elif char == '.' and '.' not in value01:
            value01 += char
            add_decimal = True

        elif char == '.' and '.' in value01:
            break

add_decimal = False
dec_count = 0

for char in line_02:
    if char in decimals:
        value02 += char
        if add_decimal:
                dec_count += 1
                if dec_count == 2:
                    break

    elif char == '.' and '.' not in value02:
        value02 += char
        add_decimal = True

    elif char == '.' and '.' in value02:
        break

print 'cpf', cpf
print('{:.2f}'.format(float(value01)+float(value02)))
