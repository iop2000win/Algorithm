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


# Q 25305. 커트라인
def solution_Q25305(input_list, k):
	input_list = sorted(input_list, reverse = True)

	result = input_list[k-1]
	print(result)

	return

# n, k = map(int, input().split())
# scores = list(map(int, input().split()))

# _ = solution_Q25305(scores, k)


# Q 2108. 통계학
'''
패키지를 활용하지 않고 mode 값을 구하고 싶은데,
시간 부분에서 계속 비효율적인 코드가 작성된다...
'''

# Q 11650. 좌표 정렬하기
'''
다중 조건을 이용한 정렬 방법을 익히는 예제
'''

def solution_Q11650(input_list):
	input_list = input_list.copy()
	input_list = sorted(input_list, key = lambda x: (x[0], x[1]))

	for point in input_list:
		print(point[0], point[1])

	return

# n = int(input())
# input_list = [tuple(map(int, input().split())) for x in range(n)]


# Q 1181. 단어 정렬
'''
중복 원소에 대한 처리를 익히는 예제 >>> set을 이용
'''

def solution_Q1181(input_list):
	words_list = input_list.copy()
	words_list = sorted(set(words_list), key = lambda x: (len(x), x))

	for word in words_list:
		print(word)

	return

# n = int(input())
# input_list = [input() for x in range(n)]


# Q 10814. 나이순 정렬

def solution_Q10814(input_list):
	member_list = sorted(member_list, key = lambda x: int(x[0]))

	for member in member_list:
		print(member[0], member[1])

	return

# n = int(input())
# input_list = [tuple(input().split()) for x in range(n)]


# Q 18870. 좌표 압축
'''
시간복잡도를 고려해야하는 문제
list.index() <<< 메서드의 경우 시간복잡도 O(N)의 연산으로
반복문 아래에서 사용할 경우 연산량을 급격하게 늘릴 수 있으므로
사용에 유의해야한다.
'''

def solution_Q18870(input_list):
	loc_list = input_list.copy()
	num_list = sorted(set(loc_list))
	num_dic = {}

	for i in range(len(num_list)):
		num_dic[num_list[i]] = i

	for num in loc_list:
		print(num_dic[num], end = ' ')

	return

# n = int(input())
# input_list = list(map(int, input().split()))