def main():
	begin_day = input().split()
	begin_time= input().split(' : ')
	end_day = input().split()
	end_time= input().split(' : ')

	begin_time = int(begin_time[0]), int(begin_time[1]), int(begin_time[2])
	end_time = int(end_time[0]), int(end_time[1]), int(end_time[2])

	total_day = 0
	total_time = [0,0,0]

	total_day = int(end_day[1]) - int(begin_day[1])

	

	if end_time[2] - begin_time[2] < 0:
		total_time[2] = end_time[2] + 60 - begin_time[2]
		dif_time = 1
	else:
		total_time[2] = end_time[2] - begin_time[2]
		dif_time = 0

	if (end_time[1] - dif_time) - begin_time[1] < 0:
		total_time[1] = (end_time[1] - dif_time + 60) - begin_time[1]
		dif_time = 1
	else:
		total_time[1] = (end_time[1] - dif_time) - begin_time[1]
		dif_time = 0

	if (end_time[0] - dif_time) - begin_time[0] < 0:
		total_time[0] = (end_time[0] - dif_time + 24) - begin_time[0]
		total_day -= 1
	else:
		total_time[0] = (end_time[0] - dif_time) - begin_time[0]

	print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(total_day, total_time[0], total_time[1], total_time[2]))

	

main()