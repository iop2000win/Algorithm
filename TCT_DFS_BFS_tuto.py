# 재귀함수의 이해
'''
간단한 팩토리얼 문제를 통해 재귀함수에 대해서 이해하고,
재귀함수와 단순 반복문의 연산량 차이를 이해한다.

재귀함수에 대해서는 간단하게 수학의 점화식을 생각하며 이해하면 좋다.
'''

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



# DFS(깊이 우선 탐색)의 이해
'''
주어진 그래프에 대해서 깊이 우선 탐색의 방법으로 탐색을 진행할 경우,
어떤 순서로 탐색이 이루어지는지 확인함으로서 DFS 탐색에 대해 이해한다.
'''

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

def DFS(graph, start, visited):
	visited[start] = True
	print(start, end = ' ')

	for i in graph[start]:
		if not visited[i]:
			DFS(graph, i, visited)


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


def BFS(graph, start, visited):
	queue = deque()
	queue.append(start)
	visited[start] = True

	while len(queue) != 0:
		node = queue.popleft()
		print(node, end = ' ')

		for i in graph[node]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True



# Q1. 음료수 얼려 먹기

def solution()