# -----------------------------------------------------------------------------------------------
# Q 18258. 큐2

import sys
from collections import deque

def solution_Q18258(input_str):
	input_val = input_str.split()
    global size
    
    if input_val[0] == 'push':
        q.append(int(input_val[1]))
        size += 1
        
    elif input_val[0] == 'pop':
        if size != 0:
            output = q.popleft()
            size -= 1
            print(output)
        else:
            print(-1)
            
    elif input_val[0] == 'size':
        print(size)
        
    elif input_val[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
            
    elif input_val[0] == 'front':
        if size != 0:
            output = q[0]
            print(output)
        else:
            print(-1)
    
    elif input_val[0] == 'back':
        if size != 0:
            output = q[-1]
            print(output)
        else:
            print(-1)
            
    else:
        pass


T = int(input())
q = deque()
size = len(q)

for t in range(T):
	input_str = sys.stdin.readline()
	solution_Q18258(input_str)



# -----------------------------------------------------------------------------------------------
# Q 2164. 카드2

import sys
from collections import deque

def solution(input_num):
    q = deque(range(1, input_num+1))
    size = input_num
    
    while size > 1:
        q.popleft()
        size -= 1
        
        top = q.popleft()
        q.append(top)
        
    return q[0]

input_num = int(sys.stdin.readline())
result = solution(input_num)

print(result)


# -----------------------------------------------------------------------------------------------
# Q 11866. 요세푸스 문제

import sys
from collections import deque

def solution(input_num, r):
    q = deque(range(1, input_num+1))
    jose = []
    
    while q:
        for i in range(r-1):
            q.append(q.popleft())
            
        top = q.popleft()
        jose.append(top)
        
        continue
        
    return jose

input_num, r = map(int, sys.stdin.readline().split())
result = solution(input_num, r)

print('<', end = '')
print(*result, sep = ', ', end = '')
print('>', end = '')


# -----------------------------------------------------------------------------------------------
# Q 1966. 프린터 큐

import sys
from collections import deque

def solution(input_list, target_index):
    input_list = deque(input_list)
    cnt = 0
    
    while True:
        max_val = max(input_list)
        
        if input_list[0] == max_val:
            input_list.popleft()
            cnt += 1
            
            if target_index == 0:
                return cnt
            
        else:
            input_list.append(input_list.popleft())
            
        target_index -= 1
        if target_index < 0:
            target_index += len(input_list)
            

T = int(input())

for t in range(T):
    n, t = map(int, sys.stdin.readline().split())
    input_list = list(map(int, sys.stdin.readline().split()))
    
    result = solution(input_list, t)
    print(result)


# -----------------------------------------------------------------------------------------------
# Q 10866. 덱

import sys
from collections import deque

def solution(input_str):
    input_str = input_str.split()
    global size

    a = input_str[0]
    
    if a == 'push_front':
        deq.appendleft(int(input_str[1]))
        size += 1
    elif a == 'push_back':
        deq.append(int(input_str[1]))
        size += 1
    elif a == 'pop_front':
        if not size == 0:
            pop = deq.popleft()
            size -= 1
            print(pop)
        else:
            print(-1)
    elif a == 'pop_back':
        if not size == 0:
            pop = deq.pop()
            size -= 1
            print(pop)
        else:
            print(-1)
    elif a == 'size':
        print(size)
    elif a == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif a == 'front':
        if not size == 0:
            print(deq[0])
        else:
            print(-1)
    elif a == 'back':
        if not size == 0:
            print(deq[-1])
        else:
            print(-1)
    else:
        print('올바른 키워드를 입력하세요')
        
    return


T = int(input())

deq = deque()
size = 0

for t in range(T):
    input_str = sys.stdin.readline()
    solution(input_str)