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



# Q3. 게임 개발 문제

def solution_Q3(N, M, position, input_list):
	result = 1

	row_position = int(position[0])
	col_position = int(position[1])
	direction = int(position[2])
	visited = [(row_position, col_position)]

	dir_map = {0: (-1, 0),
			   1: (0, 1),
			   2: (1, 0),
			   3: (0, -1)}

	while True:
		for i in range(4):
			move = False
			direction = (direction + 1) % 4
			d_row = row_position + dir_map[direction][0]
			d_col = col_position + dir_map[direction][1]

			if (input_list[d_row][d_col] == 0) and ((d_row, d_col) not in visited):
				row_position = d_row
				col_position = d_col
				visited.append((d_row, d_col))
				move = True
				break

		if move:
			result += 1
		else:
			row_position -= dir_map[direction][0]
			col_position -= dir_map[direction][1]

			if (input_list[row_position][col_position] == 1):
				return result