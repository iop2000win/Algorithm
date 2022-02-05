'''
백준 사이트에서 제공해주는 문제 중, 단계별 문제풀기 카테고리의
정렬 카테고리에 대한 풀이
'''

# Q 2750. 수 정렬하기

def solution_Q2750(input_list):
	input_list = sorted(input_list)

	for num in input_list:
		print(num)

	return


### 선택 정렬을 이용한 정렬
def solution_Q2750_1(input_list):
	input_list = input_list.copy()

	for i in range(len(input_list)):
		min_index = i

		for j in range(i+1, len(input_list)):
			if input_list[min_index] > input_list[j]:
				min_index = j

		input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

	for num in input_list:
		print(num)

	return


### 삽입 정렬을 이용한 정렬

### 퀵 정렬을 이용한 정렬

### 계수 정렬을 이용한 정렬 (*** 음수에 대해서는 정렬을 할 수 없다.)
# 계수 정렬을 이용한 수 정렬

def count_sorting(input_list):
	input_list = input_list.copy()
	count_list = [0] * max(input_list)

	for num in input_list:
		count_list[num] += 1

	sort_list = []
	for i in range(len(count_list)):
		for j in range(count_list[i]):
			sort_list.append(i)

	for num in sort_list:
		print(num)
    
	return