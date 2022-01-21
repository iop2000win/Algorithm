# 최단 경로를 찾기 위한 다익스트라 알고리즘
'''
*** 바로바로 고민없이 작성할 수 있을정도로 익숙해지도록 하자.
기본적인 개념은 각 노드에 대한 최단거리를 기록한 리스트를
모든 경우에 대해 탐색하며 더 작은 값으로 갱신해나가는 것이다.

이를 위해, 각 노드에 대한 비용을 최초에 무한대로 설정해놓는다.
그 후 해당 값을 바꿔나가는 식으로 알고리즘이 진행된다.
'''

# 소스코드 입력 예시를 위한 그래프 작성

# INF = int(1e9)
# n, m = map(int, input().split()) # n = 노드의 수 / m = 간선의 수
# start = int(input())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
# # index 값을 node 번호에 대응시키기 위해 n+1로 처리 (0에 대한 처리)

# for _ in range(m):
# 	a, b, c = map(int, input().split())
# 	graph[a].append((b, c))

# 예시 그래프 값

INF = int(1e9)
n, m = 6, 11
start = 1
visited = [False] * (n+1)
distance = [INF] * (n+1)
graph =[[],
		[(2, 2), (3, 5), (4, 1)], # 1번 node에 연결된 node와 각 비용
		[(3, 3), (4, 2)], # 2번 node에 연결된 node와 각 비용
		[(2, 3), (6, 5)], # 3번 node에 연결된 node와 각 비용
		[(3, 3), (5, 1)], # 4번 node에 연결된 node와 각 비용
		[(3, 1), (6, 2)], # 5번 node에 연결된 node와 각 비용
		[]] # 6번 node에 연결된 node와 각 비용]



# 간단한 다익스트라 알고리즘 소스코드
def get_smallest_node():
	min_value = INF
	index = 0

	# 최단거리 리스트의 값과 방문여부를 확인하여 최소값을 가진 node를 찾는 작업
	for i in range(1, n+1):
		if (distance[i] < min_value) and (not visited[i]):
			# ex) 시작점(1)에서 1번 node까지의 거리 확인
			# 1번 node의 방문여부 확인
			min_value = distance[i]
			index = i

	return index


def dijkstra(start):
	distance[start] = 0
	visited[start] = True

	# 시작점에서 연결된 node들에 대해서 최단거리 리스트를 갱신
	for j in graph[start]:
		# j[0]은 연결된 node, j[1]은 해당 노드로의 비용
		distance[j[0]] = j[1]

	# 시작점(1)을 제외한 나머지 node들에 대해서 최단거리 리스트 갱신 시작
	for i in range(n-1):
		# 방문하지 않은 node들 중, 현재까지 최단거리 값을 가진 node를 찾아간다.
		now = get_smallest_node()
		visited[now] = True

		for j in graph[now]:
			cost = distance[now] + j[1]

			if cost < distance[j[0]]:
				distance[j[0]] = cost



# 우선순위 큐를 이용한 다익스트라 알고리즘 소스코드
import heapq

def dijkstra_heap(start):
	q = []
	heapq.heappush(q, (0, start)) # (거리, node 번호)
	distance[start] = 0

	# 각 node에 대한 비용이 적은 순으로 queue에 입력된 뒤,
	# 해당 연결에 대한 최단거리 계산이 끝나면 queue에서 제거된다.
	# 따라서 queue에 데이터가 모두 없어지게 되면 모든 연결에 대한 처리가 끝났다는 의미이다.
	while q:
		dist, now = heapq.heappop(q)

		if distance[now] < dist:
			continue

		for i in graph[now]:
			cost = dist + i[1]

			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))




# 플로이드 워셜 알고리즘
'''
다익스트라 알고리즘의 경우, 시작점에서 다른 모든 노드에 대한 최단거리를 찾는 알고리즘이었다.

플로이드 워셜 알고리즘은 모든 노드에 대해서 각각 모든 노드에 대한 최단거리를 찾는 알고리즘이다.
즉, 2차원의 형태 결과값을 도출한다.
'''

def floyd_warshall():
	for node in range(1, n+1):
		for a in range(1, n+1):
			for b in range(1, n+1):
				graph[a][b] = min(graph[a][b], graph[a][node] + graph[node][b])



# Q1. 미래도시

# graph info - floyd warshall 알고리즘을 사용하기 위해 그래프를 2차원으로 입력 받는다.
node_count, edge_count = map(int, input().split())
graph = [[INF] * (node_count+1) for _ in range(node_count+1)]

# 자기 자신으로의 이동 비용을 0으로 초기화
for i in range(1, len(graph)):
	graph[i][i] = 0

for _ in range(1, node_count+1):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

start = 1
destination, waypoint = map(int, input().split())

def solution_1_Q1(start, waypoint, destination, graph):
	for i in range(1, len(graph)):
		for j in range(1, len(graph)):
			for k in range(1, len(graph)):
				cost = min(graph[i][j], graph[i][k] + graph[k][j])
				graph[i][j] = cost

	result = graph[start][waypoint] + graph[waypoint][destination]
	if result >= INF:
		return -1
	else:
		return result


# 근데 위 문제의 경우 시작점, 경유점, 도착점이 모두 입력값으로 주어진다.
# 따라서 모든 경로에 대해서 최단거리를 갱신할 필요가 없지 않을까?
def solution_2_Q2(start, waypoint, destination, graph):
	for i in range(1, len(graph)):
		for j in range(1, len(graph)):
			cost = min(graph[start][i], graph[start][j] + graph[j][i])
			graph[start][i] = cost

	for i in range(1, len(graph)):
		for j in range(1, len(graph)):
			cost = min(graph[waypoint][i], graph[waypoint][j] + graph[j][i])
			graph[waypoint][i] = cost

	result = graph[start][waypoint] + graph[waypoint][destination]
	if result >= INF:
		return -1
	else:
		return result