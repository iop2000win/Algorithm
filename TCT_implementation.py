# Q1. 상하좌우 문제

def solution_Q1(N, input_list):
	position = [1, 1]

	move_set = {'L': [0, -1],
				'R': [0, 1],
				'U': [-1, 0],
				'D': [1, 0]}

	for move in input_list:
		moving = [position[0] + move_set[move][0],
				  position[1] + move_set[move][1]]

		if (moving[0] > 0) & (moving[0] <= N) & (moving[1] > 0) & (moving[1] <= N):
			position[0] = moving[0]
			position[1] = moving[1]

	return position



# Q2. 시각 문제

def solution_Q2(N):
	result = 0

	for h in range(N+1):
		for m in range(60):
			for s in range(60):
				time = str(h) + str(m) + str(s)

				if '3' in time:
					result += 1

	return result