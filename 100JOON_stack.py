# -----------------------------------------------------------------------------------------------
# Q 10828. 스택

import sys

def solution_Q10828(input_txt):
	global size
	x = input_txt.split()

	if x[0] == 'push':
		lst.append(int(x[1]))
		size += 1

	elif x[0] == 'pop':
		if size == 0:
			print(-1)
		else:
			pop_num = lst.pop()
			print(pop_num)
			size -= 1

	elif x[0] == 'size':
		print(size)

	elif x[0] == 'empty':
		if size == 0:
			print(1)
		else:
			print(0)
	
	elif x[0] == 'top':
		if size == 0:
			print(-1)
		else:
			print(lst[-1])

	else:
		pass

lst = []
size = 0

T = int(input())
for t in range(T):
	input_txt = sys.stdin.readline()
	_ = solution_Q10828(input_txt)


# -----------------------------------------------------------------------------------------------
# Q 28278. 스택2

import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    x = sys.stdin.readline().split()
    
    if x[0] == '1':
        stack.append(int(x[1]))
    elif x[0] == '2':
        if len(stack) <= 0:
            print(-1)
        else:
            pop = stack.pop()
            print(pop)
    elif x[0] == '3':
        print(len(stack))
    elif x[0] == '4':
        if len(stack) <= 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[-1])


# -----------------------------------------------------------------------------------------------
# Q 10773. 제로

import sys
T = int(sys.stdin.readline())

lst = []
for t in range(T):
    num = int(sys.stdin.readline())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()
        
print(sum(lst))


# -----------------------------------------------------------------------------------------------
# Q 9012. 괄호 검사

import sys

def solution_Q9012(input_txt):
	lst = []

	for i in ragne(len(input_txt)):
		if input_txt[i] == '(':
			lst.append(input_txt[i])
		else:
			if len(lst) == 0:
				print('NO')
				return

			else:
				lst.pop()

	if len(lst) == 0:
		print('YES')
	else:
		print('NO')

T = int(input())

for t in range(T):
	input_txt = sys.stdin.readline()
	_ = solution_Q9012(input_txt)


# -----------------------------------------------------------------------------------------------
# Q 4949. 균형잡힌 세상

import sys

def solution_Q4949(input_txt):
	stack = []

	for i in range(len(input_txt)):
		if (input_txt[i] == '(') or (input_txt[i] == '['):
			stack.append(input_txt[i])

		elif (input_txt[i] == ')') or (input_txt[i] == ']'):
			if len(stack) == 0:
				return 'no'

			else:
				pop = stack.pop()

				if (input_txt[i] == ')') & (pop == '['):
					return 'no'
				elif (input_txt[i] == ']') & (pop == '('):
					return 'no'
				else:
					pass

		else:
			continue

	if len(stack) == 0:
		return 'yes'
	else:
		return 'no'


while True:
	input_txt = sys.stdin.readline()
	
	if (input_txt == '.') or (input_txt == '.\n'):
		break
	else:
		result = solution_Q4949(input_txt)

		print(result)


# -----------------------------------------------------------------------------------------------
# Q 1874. 스택 수열 - 더 간단한 풀이 구해보기! 개념적으로 접근!
import sys

def solution_Q1874(n, target_num_list):
	stack = []
	result = []

	input_num = 1
	target_index = 0

	while True:
		if len(stack) == 0:
			stack.append(input_num)
			result.append('+')

			input_num += 1

		elif stack[-1] == target_num_list[target_index]:
			stack.pop()
			target_index += 1
			result.append('-')

		elif input_num <= n:
			stack.append(input_num)
			result.append('+')

			input_num += 1

		elif input_num > n:
			return ['NO']

		else:
			pass

		if (input_num > n) & (len(stack) == 0):
			return result

N = int(input())
target_num_list = [int(sys.stdin.readline()) for _ in range(N)]

result = solution_Q1874(N, target_num_list)
print(*result, sep = '\n')


# -----------------------------------------------------------------------------------------------
# Q 28279. 덱2

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    x = sys.stdin.readline().split()
    
    if x[0] == '1':
        deq.appendleft(int(x[1]))
    elif x[0] == '2':
        deq.append(int(x[1]))
    elif x[0] == '3':
        if len(deq) != 0:
            pop = deq.popleft()
            print(pop)
        else:
            print(-1)
    elif x[0] == '4':
        if len(deq) != 0:
            pop = deq.pop()
            print(pop)
        else:
            print(-1)
    elif x[0] == '5':
        print(len(deq))
    elif x[0] == '6':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == '7':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    else:
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)


# -----------------------------------------------------------------------------------------------
# Q 2346. 풍선 터트리기