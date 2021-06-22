x = []
for i in range(5):
	x.append(int(input()))

print('{} valor(es) par(es)'.format(len(list(filter(lambda y : y % 2 == 0, x)))))
print('{} valor(es) impar(es)'.format(len(list(filter(lambda y : y % 2 != 0, x)))))
print('{} valor(es) positivo(s)'.format(len(list(filter(lambda y : y > 0, x)))))
print('{} valor(es) negativo(s)'.format(len(list(filter(lambda y : y < 0, x)))))
