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



'''

    #누적합 카테고리 문제
    
    합을 계산하는 과정에서 연산 수를 줄이기 위하여,
    리스트에 미리 누적합을 계산한 후, 누적합 간의 관계를 이용하여
    결과를 도출해내는 문제로, 연산 시간을 크게 줄일 수 있는 테크닉이다.
'''

# Q 11659. 구간 합 구하기 4
'''
    연산 속도 향상을 위해 누적합을 활용하는 문제
'''
n, t = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
for i in range(1, len(num_list)):
    num_list[i] = num_list[i] + num_list[i-1]

for _ in range(t):
    start_index, end_index = map(int, input().split())
    
    result = num_list[end_index] - num_list[start_index-1]
    print(result)


# Q 2559. 수열
n, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list = [0] + num_list
for i in range(1, len(num_list)):
    num_list[i] += num_list[i-1]

for i in range(k, n+1):
    if i == k:
        max_val = num_list[i]
    else:
        val = num_list[i] - num_list[i-k]
        max_val = max(max_val, val)
        
print(max_val)


# Q 11660. 구간 합 구하기 5
'''
    2차원 배열에 대한 구간합 구하기 문제
    연산 시간이 중요한 문제로, 제출시에는 입력값을 받는 방식을 sys를 활용한 방식으로 변경 필요
'''
n, m = map(int, input().split())

num_list = [[0] + list(map(int, input().split())) for _ in range(n)]
num_list = [[0] * (n+1)] + num_list

for i in range(1, n+1):
    for j in range(1, n+1):
        num_list[i][j] = num_list[i][j-1] + num_list[i-1][j] + num_list[i][j] - num_list[i-1][j-1]
        
for _ in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    
    result = num_list[x_2][y_2] - num_list[x_2][y_1-1] - num_list[x_1-1][y_2] + num_list[x_1-1][y_1-1]
    print(result)