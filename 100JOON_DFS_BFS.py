'''
백준 저지의 단계별 문제풀이 카테고리의 DFS/BFS 알고리즘 문제 풀이
'''



# Q 1260. DFS와 BFS
'''
주어진 그래프에 대해서 DFS 결과와 BFS 결과를 각각 출력하는 것으로,
각 알고리즘에 대한 기본적인 이해도 및 사용법을 물어보는 문제
'''

n, m, start = map(int, input().split())
input_list = [list(map(int, input().split())) for x in range(m)]

graph = [[] for x in range(n+1)]

for edge in input_list:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    
# dfs / bfs

def dfs_result(graph, start):
    visit_sequence = []
    visited = [False] * len(graph)
    
    def dfs(graph, start, visited):
        if visited[start] == False:
            visited[start] = True
            visit_sequence.append(start)
            print(start, end = ' ')
            
            for node in graph[start]:
                dfs(graph, node, visited)
    
    dfs(graph, start, visited)
    
    return(visit_sequence)


def bfs_result(graph, start):
    visit_sequence = []
    visited = [False] * len(graph)
    
    def bfs(graph, start, visited):
        from collections import deque
        q = deque([start])
        visited[start] = True
        visit_sequence.append(start)
        print(start, end = ' ')
        
        while q:
            node = q.popleft()
            
            for c_node in graph[node]:
                if visited[c_node] == False:
                    q.append(c_node)
                    visited[c_node] = True
                    visit_sequence.append(c_node)
                    print(c_node, end = ' ')
                    
    bfs(graph, start, visited)
    
    return visit_sequence

dfs_result(graph, start)
print()
bfs_result(graph, start)



# Q 2606. 바이러스
import sys

node_cnt = int(sys.stdin.readline())
edge_cnt = int(sys.stdin.readline())
edge_list = [list(map(int, sys.stdin.readline().split())) for x in range(edge_cnt)]

# 상호 연결
graph = [[] for x in range(node_cnt+1)]
for edge in edge_list:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


# 1번 컴퓨터를 시작점으로 연결된 모든 노드 방문. 총 방문한 노드의 수는?
def get_virus(graph, start):
    visited = [False] * len(graph)
    
    def dfs(graph, start, visited):
        if visited[start] == False:
            visited[start] = True
            
            for node in graph[start]:
                dfs(graph, node, visited)
                
    dfs(graph, start, visited)
         
    return visited

result = get_virus(graph, 1)
print(sum(result)-1)



# Q 2667. 단지 번호 붙이기
import sys

n = int(input())
# n = int(sys.stdin.readline())

graph = [[int(y) for y in input()] for x in range(n)]
# graph = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

def building_search(graph):
    from collections import deque
    
    n = len(graph)
    building_dic = {}
    move_pattern = [(1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)]

    building_num = 1
    for row in range(len(graph)):
        for col in range(len(graph)):
            if graph[row][col] == 1:
                building_dic[building_num] = 1
                q = deque([(row, col)])
                graph[row][col] = -1 # -1 값으로 방문처리
                
                while q:
                    r, c = q.popleft()
                    for move in move_pattern:
                        r_ = r + move[0]
                        c_ = c + move[1]
                        
                        if (r_ < 0) | (r_ > n-1) | (c_ < 0) | (c_ > n-1):
                            continue
                            
                        if graph[r_][c_] == 1:
                            q.append((r_, c_))
                            graph[r_][c_] = -1
                            building_dic[building_num] = building_dic[building_num] + 1
                building_num += 1
                
    print(len(building_dic))
    value_list = sorted(building_dic.values())
    for value in value_list:
        print(value)

    return

building_search(graph)



# Q 1012. 유기농 배추
import sys

T = int(sys.stdin.readline())

def solution(graph):
    from collections import deque
    count = 0
    n, m = len(graph), len(graph[0])
    move_pattern = [(1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)]

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1:
                count += 1
                q = deque([(row, col)])
                graph[row][col] = -1

                while q:
                    r, c = q.popleft()

                    for move in move_pattern:
                        r_ = r + move[0]
                        c_ = c + move[1]

                        if (r_ < 0) | (r_ > n-1) | (c_ < 0) | (c_ > m-1):
                            continue

                        if graph[r_][c_] == 1:
                            q.append((r_, c_))
                            graph[r_][c_] = -1
    
    return count


for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for x in range(n)]
    
    for i in range(k):
        col, row = map(int, sys.stdin.readline().split())
        graph[row][col] = 1
        
    result = solution(graph)
    print(result)