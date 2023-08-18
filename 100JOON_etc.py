# Q 10988. 팰린드롬 확인하기
'''
파이썬의 기초적인 반복문 사용법을 묻는 질문
'''
import math

def solution_Q10988(input_txt):
	i = math.ceil(len(input_txt)//2)

	for i in range(i):
		if input_txt[i] == input_txt[-(i+1)]:
			pass
		else:
			return 0

	return 1

input_txt = input()
result = solution_Q10988(input_txt)

print(result)



def solution(input_txt_list):
    score_board = {
                    'A+': 4.5,
                    'A0': 4.0,
                    'B+': 3.5,
                    'B0': 3.0,
                    'C+': 2.5,
                    'C0': 2.0,
                    'D+': 1.5,
                    'D0': 1.0,
                    'F' : 0
    }
    
    grade_sum = 0
    credit_sum = 0
    subject_count = 0
    
    for txt in input_txt_list:
        _, credit, grade = txt.split()
        if grade != 'P':
            grade_sum += int(credit[0]) * score_board[grade]
            credit_sum += int(credit[0])
            subject_count += 1
            
    result = grade_sum / credit_sum
    
    return result