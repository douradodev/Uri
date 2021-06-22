def main():
	times = input()
	times = int(times)
	initial_msg = []
	team1_msg = []
	team2_msg = []
	team1_pts, team2_pts = [], []
	
	for i in range(times):	

		initial_msg.append(raw_input())
		team1_msg.append(raw_input())
		team2_msg.append(raw_input())

	for instc in range(times):

		team1_pts += [len(initial_msg[instc])]
		team2_pts += [len(initial_msg[instc])]

		while len(initial_msg[instc]) != len(team1_msg[instc]) or len(initial_msg[instc]) != len(team2_msg[instc]):

			if len(initial_msg[instc]) > len(team1_msg[instc]):
				team1_msg[instc] = team1_msg[instc] + "?"
			elif len(initial_msg[instc]) > len(team2_msg[instc]):
				team2_msg[instc] = team2_msg[instc] + "?"
			elif len(initial_msg[instc]) < len(team1_msg[instc]) or len(initial_msg[instc]) < len(team2_msg[instc]):
				initial_msg[instc] = initial_msg[instc] + "?"


		for index in range(len(initial_msg[instc])):
			if initial_msg[instc][index] != team1_msg[instc][index]:
				team1_pts[instc] -= 1
			if initial_msg[instc][index] != team2_msg[instc][index]:
				team2_pts[instc] -= 1


		x= instc + 1
		print('Instancia %i' % x)

		if team1_pts[instc] == team2_pts[instc]:
			index = 0
			for char in initial_msg[instc]:				
				if team1_msg[instc][index] == char and team2_msg[instc][index] != char:
					print('time 1\n')					
					break
				elif team1_msg[instc][index] != char and team2_msg[instc][index] == char:
					print('time 2\n')					
					break

				index += 1

			else:
				print('empate\n')
				
		elif team1_pts[instc] > team2_pts[instc]:
			print('time 1\n')
			
		else:
			print('time 2\n')


main()