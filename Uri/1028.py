def simple_mdc(num_max, num_min):
	if num_max % num_min == 0:
		print(num_min)
	else:
		simple_mdc(num_min, (num_max % num_min))

for _ in range(int(input())):
	deck1, deck2 = map(int, (input().split()))

	deck_min, deck_max = sorted([deck1, deck2])

	simple_mdc(deck_max, deck_min)
	