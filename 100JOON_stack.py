# Q 10828. 스택

import sys

def stack(input_txt):
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

n = int(input())
for i in range(n):
	input_txt = sys.stdin.readline()
	_ = stack(input_txt)



# Q 10773. 제로

import sys
n = int(sys.stdin.readline())

lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()
        
print(sum(lst))



