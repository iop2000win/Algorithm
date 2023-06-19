'''
다양한 정렬 알고리즘에 대한 이론

1. 버블 정렬
2. 선택 정렬
3. 삽입 정렬
4. 힙 정렬
5. 병합 정렬
6. 퀵 정렬
7. 쉘 정렬
8. 기수 정렬 *자리수가 정해진 양의 정수에 대해서만 가능
9. 계수 정렬(카운팅 정렬) *양의 정수에 대해서만 가능
'''

'''
=======================================================================================================================
<<<버블 정렬>>>

A B C D E F G
위와 같은 배열이 있을 때,
앞에서부터 두 개의 원소를 선택하여 크기를 비교, 더 작은 수를 앞으로 보내는 방식으로 반복한다.
이럴 경우,

	1. A - B 비교 > 더 작은 수를 앞으로, 더 큰 수를 뒤로 (ex A > B, A와 B의 자리 교환)
	2. [B A C D E F G] > A - C 비교

이렇게 정렬 되는 과정을 보면 작은 숫자가 점점 앞으로 나오는 방식인데, 이 모습이
거품이 위로 올라오는 것과 같다고 해서 붙여진 알고리즘의 이름이다.

이 알고리즘의 경우, 한 번의 순회가 끝났을 때 가장 큰 원소가 배열의 가장 마지막으로 이동하게 된다.
즉, (원소의 갯수 - 1번)만큼 순회를 반복하게 되면 모든 배열이 정렬되는 알고리즘이다.
'''

def bubble_sort(input_list):
	# 반복횟수
	for _ in range(len(input_list)-1):
		# 한 번의 순회동안 확인해야 하는 원소의 갯수(정렬되지 않은 배열의 길이-1)
		l = len(input_list)-1

		for i in range(l):
			if input_list[i] > input_list[i+1]:
				input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

		l -= 1

	return


'''
=======================================================================================================================
<<<선택 정렬>>>

'''

def selection_sort(input_list):
	for i in range(len(input_list)):
		min_index = i

		for j in range(i+1, len(input_list)):
			if input_list[min_index] > input_list[j]:
				min_index = j

		input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

	return


'''
=======================================================================================================================
<<<삽입 정렬>>>

위까지의 정렬 알고리즘 보다는 약간 더 헷갈린다.
'''

def insertion_sort(input_list):
	for i in range(1, len(input_list)):
		for j in range(i-1, -1, -1):
			if input_list[j+1] < input_list[j]:
				input_list[j+1], input_list[j] = input_list[j], input_list[j+1]
			else:
				break

	return


def insertion_sort2(input_list):
	for i in range(1, len(input_list)):
		key = input_list[i]
		j = i-1

		while (j >= 0) and (input_list[j] > key):
			input_list[j+1] = input_list[j]
			j -= 1

		input_list[j+1] = key

	return


'''
=======================================================================================================================
<<<힙 정렬>>>

두 단계로 작업이 구분된다.
1. 주어진 배열을 힙 자료구조 형태로 재배열하는 작업
2. 힙 자료구조의 루트 값을 꺼내어 정렬하는 작업

* 힙 자료구조의 구현에 대한 이해가 기본적으로 선행 되어야 한다.
'''

# 입력된 배열을 힙 자료구조로 재배열하는 함수 - 반복문을 통한 구현 / 재귀함수를 통한 구현 모두 가능하다.
def heapify_loop(input_list):


	return


def heapify_recur(input_list):

	return