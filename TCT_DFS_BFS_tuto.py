# 재귀함수의 이해
'''
간단한 팩토리얼 문제를 통해 재귀함수에 대해서 이해하고,
재귀함수와 단순 반복문의 연산량 차이를 이해한다.

재귀함수에 대해서는 간단하게 수학의 점화식을 생각하며 이해하면 좋다.
*** 재귀함수를 사용할 때에는 항상 종료 조건에 대해서 생각해야한다.

재귀함수의 처리는 컴퓨터 내부에서 '스택 자료구조'를 이용하여 이루어진다.
'''

# 재귀함수의 매커니즘 이해

recursive_stack = []

def recursive_test(i):
	if i == 10:
		print('종료 조건이 충족되어, 후입선출 구조에 따라 뒤에서 부터 함수 결과값 반환')
		return

	print(f'{i}번째 함수가 실행되었으므로, recursive_stack에 해당 함수가 입력')
	recursive_stack.append(f'recursive_test({i})')
	print(f'{i}번째 함수에서 {i+1}번째 함수 호출')
	recursive_test(0)


# 반복문을 사용한 factorial

def factorial_iterative(input_num):
	result = 1

	if input_num <= 1:
		return 1

	for i in range(1, input_num+1):
		result *= i

	return result


# 재귀함수를 사용한 factorial

def factorial_recursive(input_num):
	if input_num <= 1:
		return 1

	return input_num * factorial_recursive(input_num - 1)


# 재귀함수를 이용한 fibonazzi 수열 구현
'''
fibonazzi 수열의 경우 재귀함수를 사용하여도 연산 시간이 매우매우 길어지므로,
후에 배울 다이나믹 프로그래밍을 통해서 메모리까지 적극 활용해야하는 수열이다.

여기서는 재귀함수만을 이용하여 간략하게 구현해보자.
'''

def fibonazzi_sequence(input_num):
	# fibonazzi sequence의 첫 번째, 두 번째 항은 1임을 조건에 명시
	if input_num <= 2:
		return 1

	return fibonazzi_sequence(input_num-2) + fibonazzi_sequence(input_num-1)



# DFS(깊이 우선 탐색)의 이해
'''
주어진 그래프에 대해서 깊이 우선 탐색의 방법으로 탐색을 진행할 경우,
어떤 순서로 탐색이 이루어지는지 확인함으로서 DFS 탐색에 대해 이해한다.
'''

# 인접 리스트 형식의 그래프
graph = [[],
		 [2, 3, 8],
		 [1, 7],
		 [1, 4, 5],
		 [3, 5],
		 [3, 4],
		 [7],
		 [2, 6, 8],
		 [1, 7]]

visited = [False] * 9

# dfs 함수의 경우, 재귀 함수를 사용하여 구현한다!
# stack 자료 구조의 활용!

def DFS(graph, start, visited):
	visited[start] = True
	print(start, end = ' ')

	for i in graph[start]:
		if not visited[i]:
			DFS(graph, i, visited)

def DFS_list(graph, start, visited):
	visit_sequence = []
	
	def dfs_(graph, start, visited):
		# 재귀 함수의 종료조건 제시
		# 방문한 노드가 이미 방문처리 된 노드일 경우 해당 방문에서 처리할 작업이 없으므로,
		# 재귀 함수가 종료되도록 한다.
		if visited[start] == True:
			return

		visited[start] = True # 방문 처리
		visit_sequence.append(start)

		for node in graph[start]:
		dfs_(graph, node, visited)

	dfs_(graph, start, visited)

	return visit_sequence


# BFS(너비 우선 탐색)의 이해
'''
위와 같은 방식으로 이번에는 BFS방식을 통해 그래프 방문 순서를 시각화,
해당 방식을 이해한다.
'''

def BFS(graph, start, visited):
	queue = deque([start])
	visited[start] = True

	while queue:
		node = queue.popleft()
		print(node, end = ' ')

		for i in graph[node]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True


def BFS_list(graph, start, visited):
	q = deque([start])
	visited[start] = True
	visit_sequence = []

	while q:
		node = queue.popleft()

		for c_node in graph[node]: # c_node : connected node
			if visited[c_node] == False:
				q.append(c_node)
				visited[c_node] = True
				visit_sequence.append(c_node)

	return visit_sequence



# Q1. 음료수 얼려 먹기
'''
책에서 제시해준 풀이법은 DFS를 이용한 풀이법지만,
혼자 풀이하는 과정에서 BFS를 사용하여 풀었다.

복습 과정에서 DFS를 활용하는 방법으로도 풀어보도록 하자.
(아직은 재귀함수를 자연스럽게 사용하는게 어려운 듯 하다.)
'''
def solution_Q1(n, m, input_list):
	# n = row, m = col, input_list = graph
	from collections import deque
	result = 0

	for row in range(n):
		for col in range(m):
			if input_list[row][col] == 0: # 방문한 노드인지 확인
				q = deque([(row, col)]) # 좌표로 노드 표시
				input_list[row][col] = 1 # 방문 처리

				while q:
					r, c = q.popleft()

					# 인접 노드의 1)범위에 대한 조건, 2)방문 여부에 대한 조건 확인 후 방문처리
					if (r-1 >= 0):
						if (input_list[r-1][c] != 1):
							q.append((r-1, c))
							input_list[r-1][c] = 1

					if (r+1 <= n-1):
						if (input_list[r+1][c] != 1):
							q.append((r+1, c))
							input_list[r+1][c] = 1

					if (c-1 >= 0):
						if (input_list[r][c-1] != 1):
							q.append((r, c-1))
							input_list[r][c-1] = 1

					if (c+1 <= m-1):
						if (input_list[r][c+1] != 1):
							q.append((r, c+1))
							input_list[r][c+1] = 1

				result += 1

	return result


# Q2. 미로 탈출
'''
전형적인 BFS 문제이면서, 풀이에 대한 아이디어를 떠올리면 훨씬 쉽게 접근할 수 있는 문제
최단거리 문제라고도 볼 수 있다.

노드와 노드 사이의 이동에 대해서 비용을 계산하는 것!

* 조건 처리에 대해서도 유의하자.
'''

def solution_Q2(n, m, input_list):
	# n = row, m = col, input_list = graph
	from collections import deque

	# 범위에 대한 부분을 다뤄주기 위해 상하좌우로 [0] 값 추가
	# 이렇게 하지 않아도 됨! 한 번 시험해본 방식임
	graph = [[0] * (m+2)]
	for lst in input_list:
		graph.append([0] + lst + [0])
	graph.append([0] * (m+2))

	move_pattern = [(-1, 0),
					(1, 0),
					(0, -1),
					(0, 1)]

	q = deque([(1, 1)])
	graph[1][1] = 1

	while q:
		r, c = q.popleft()

		for pattern in move_pattern:
			if graph[r + pattern[0]][c + pattern[1]] == 1:
				q.append((r + pattern[0], c + pattern[1]))
				graph[r + pattern[0]][c + pattern[1]] = graph[r][c] + 1

	return graph[n][m]