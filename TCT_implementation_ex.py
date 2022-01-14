# Q1. 럭키 스트레이트 문제

def solution(input_num):
	score = str(input_num)
	score_len = len(score)
	half_len = int(score_len/2)

	f_score = score[:half_len]
	b_score = score[half_len:]

	f = 0
	b = 0

	for i in range(len(f_score)):
		f += int(f_score[i])
		b += int(b_score[i])

	if f == b:
		return 'LUCKY'
	else:
		return 'READY'