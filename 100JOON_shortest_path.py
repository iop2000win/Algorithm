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