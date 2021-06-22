seq, qtd = map(int, input().split())

all_num = list(range(1,qtd+1))
begin_slice, end_slice = 0, seq

while len(all_num[begin_slice:end_slice]) > 0:

	nums = map(str, all_num[begin_slice:end_slice])

	if len(all_num[begin_slice:end_slice]) % seq != 0:
		print(" ".join(nums), end=" ")
	else:
		print(" ".join(nums))

	begin_slice = end_slice
	end_slice = end_slice + seq

