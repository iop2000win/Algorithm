def solution(n,lost_list, reserve_list):
	uniform_list = [0] * n

	for i in range(n):
		if (i+1) in lost_list:
			uniform_list[i] -= 1

		if (i+1) in reserve_list:
			uniform_list[i] += 1

	for lost in lost_list:
		f_lost = lost - 1
		b_lost = lost + 1

		if f_lost in reserve_list:
			uniform_list[lost-1] += 1
			uniform_list[lost-1-1] -= 1

		elif b_lost in reserve_list:
			uniform_list[lost-1] += 1
			uniform_list[lost-1+1] -= 1

	result = len([x for x in uniform_list if x >= 0])

	return result