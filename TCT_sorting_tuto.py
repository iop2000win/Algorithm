# 정렬 알고리즘의 여러가지 방법들을 배우고, 적절하게 사용할 수 있도록 연습하자.

# 선택 정렬 - 시간 복잡도 O(N^2)
'''
주어진 배열에서,
1. 가장 작은 데이터를 찾는다.
2. 해당 데이터를 가장 앞으로 보낸다.
위 방식의 반복으로 정렬이 이루어진다.
'''
def select_sort(input_list):
	for i in range(len(input_list)):
		min_index = i

		for j in range(i, len(input_list)):
			if input_list[min_index] > input_list[j]:
				min_index = j

		input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

	return input_list


# 삽입 정렬 - 시간 복잡도 O(N^2)
'''
주어진 배열에서, 각 원소가 위치해야할 장소를 찾아 해당 위치에 원소를 삽입하는 방식
거의 정렬이 이루어진 상태의 배열에 대해서 그 효율성이 매우 높다.
'''
def insert_sort(input_list):
	for i in range(1, len(input_list)):
		for j in range(i, 0, -1):
			if input_list[j] < input_list[j-1]:
				input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
			else:
				break

	return input_list


# 퀵 정렬 ***
'''
기준 데이터를 설정, 그 기준보다 큰 데이터와 작은 데이터의 위치를 변환
(이진 탐색과 그 형태가 매우 비슷하다)
'''
def quick_sort_1(input_list, start, end):
	if start >= end:
		return

	pivot = start
	left = start +1
	right = end

	while left <= right:
		while left <= end and input_list[left] <= input_list[pivot]:
			left += 1

		while right > start and input_list[right] >= input_list[pivot]:
			right -= 1

		if left > right:
			input_list[right], input_list[pivot] = input_list[pivot], input_list[right]
		else:
			input_list[left], input_list[right] = input_list[right], input_list[left]

	quick_sort_1(input_list, start, right -1)
	quick_sort_1(input_list, right+1, end)


def quick_sort_2(input_list):
	if len(input_list) <= 1:
		return input_list

	pivot = input_list[0]
	tail = input_list[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)


# 계수 정렬
def count_sort(input_list):
	count = [0] * (max(input_list) + 1)
	result = []

	for i in input_list:
		count[i] += 1

	for i in range(len(count)):
		for j in range(count[i]):
			result.append(i)

	return result


# 버블 정렬
def bubble_sort(input_list):
	for i in range(len(input_list)):
		idx = 0
		l = len(input_list) -1
		while idx +1 <= l:
			if input_list[idx] > input_list[idx+1]:
				input_list[idx], input_list[idx+1] = input_list[idx+1], input_list[idx]
			
			idx += 1

		l -= 1

	return input_list


# 쉘 정렬
def shell_sort(input_list):
	return


# 힙 정렬
def heap_sort():
	return


# 기수 정렬
def radix_sort():
	return


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# Q1. 두 배열의 원소 교체

def solution(N, K, list_A, list_B):
	list_A = sorted(list_A)
	list_B = sorted(list_B)

	for i in range(K):
		if list_A[i] < list_B[i]:
			list_A[i], list_B[i] = list_B[i], list_A[i]
		else:
			break

	return sum(list_A)