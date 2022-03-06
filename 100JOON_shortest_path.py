# Q 1753. 최단 경로

import sys
import heapq

node, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(node+1)]
for _ in range(edge):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node].append((cost, to_node))

INF = 1e9
cost_list = [INF] * (node+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost_list[start] = 0
    
    while q:
        cost, now = heapq.heappop(q)
        if cost > cost_list[now]:
            continue
            
        for c, n in graph[now]:
            n_cost = cost + c
            if n_cost < cost_list[n]:
                heapq.heappush(q, (n_cost, n))
                cost_list[n] = n_cost

dijkstra(start)
for i in range(1, node+1):
    if cost_list[i] < INF:
        print(cost_list[i])
    else:
        print('INF')



# Q 1504. 특정한 최단 경로
import sys
import heapq

def dijkstra(node, start, dest):
    INF = 1e9
    cost_list = [INF] * (node+1)
    
    q = []
    heapq.heappush(q, (0, start))
    cost_list[start] = 0
    
    while q:
        cost, now = heapq.heappop(q)
        if cost > cost_list[now]:
            continue
            
        for c, n in graph[now]:
            n_cost = cost + c
            if n_cost < cost_list[n]:
                heapq.heappush(q, (n_cost, n))
                cost_list[n] = n_cost

    return cost_list[dest]


node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(edge):
    node_1, node_2, cost = map(int, input().split())
    graph[node_1].append((cost, node_2))
    graph[node_2].append((cost, node_1))
    
way_1, way_2 = map(int, input().split())

result_1 = dijkstra(node, 1, way_1) + dijkstra(node, way_1, way_2) + dijkstra(node, way_2, node)
result_2 = dijkstra(node, 1, way_2) + dijkstra(node, way_2, way_1) + dijkstra(node, way_1, node)
result = min(result_1, result_2)

if result < INF:
    print(result)
else:
    print(-1)



# Q 9370. 미확인 도착지
'''
dijkstra 알고리즘 사용, 최대한 연산 시간이 짧아지도록 코드 구성을 해야한다!
'''
def dijkstra(graph, start):
    import heapq

    INF = 1e9
    cost_list = [INF] * (len(graph))

    q = []
    heapq.heappush(q, (0, start))
    cost_list[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if cost > cost_list[now]:
            continue

        for c, n in graph[now]:
            new_c = cost + c
            if new_c < cost_list[n]:
                heapq.heappush(q, (new_c, n))
                cost_list[n] = new_c

    return cost_list

T = int(input())
for _ in range(T):
    node, edge, cand = map(int, input().split())
    start, g, h = map(int, input().split())
    graph = [[] for _ in range(node+1)]
    for _ in range(edge):
        node_1, node_2, cost = map(int, input().split())
        graph[node_1].append((cost, node_2))
        graph[node_2].append((cost, node_1))

    t_list = sorted([int(input()) for _ in range(cand)])

    for i in graph[g]:
        if i[1] == h:
            c = i[0]

    dijk_start = dijkstra(graph, start)
    dijk_g = dijkstra(graph, g)
    dijk_h = dijkstra(graph, h)

    for t in t_list:
        min_cost = min(dijk_start[g] + dijk_h[t] + c,
                       dijk_start[h] + dijk_g[t] + c)
        if dijk_start[t] == min_cost:
            print(t, end = ' ')



# Q 11404. 플로이드

INF = 1e9
node = int(input())
edge = int(input())
graph = [[INF] * (node+1) for _ in range(node+1)]
for i in range(node+1):
    graph[i][i] = 0

for _ in range(edge):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node][to_node] = min(graph[from_node][to_node], cost)

for k in range(1, node+1):
    for i in range(1, node+1):
        for j in range(1, node+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, node+1):
    for j in graph[i][1:]:
        print(j, end = ' ')
    print()



# Q 1956. 운동
'''
파이썬 코드 제출로는 시간초과가 계속 뜬다.
풀이에서 시간을 줄일 방법이 있을까??

마지막에 result의 최솟값을 구하는 부분에서 줄일 수도 있을 것 같은데...
'''

def floyd(input_graph):
    graph = input_graph.copy()
    for k in range(1, len(graph)):
        for a in range(1, len(graph)):
            for b in range(1, len(graph)):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

    return graph

node, edge = map(int, input().split())
INF = 1e9
graph = [[INF] * (node+1) for _ in range(node+1)]

for i in range(node+1):
    graph[i][i] = 0
    
for _ in range(edge):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node][to_node] = cost

graph = floyd(graph)

result = INF

for i in range(1, node+1):
    for j in range(1, node+1):
        if i == j:
            continue

        result = min(result, graph[i][j] + graph[j][i])

print(result)