# 피보나치 수열을 통한 동적 프로그래밍의 필요성 이해
'''
기본적으로 피보나치 수열처럼 점화식으로 쉽게 표현되는 연산의 경우
재귀함수를 이용하여 쉽게 구현할 수 있다.

다만 재귀함수를 사용할 경우, 입력 값이 커질수록 연산량이 기하급수적으로 늘어나는 단점이 있다.
피보나치 수열을 통해 이를 살펴보고, 동적프로그래밍의 필요성을 느껴보자
'''

def fibo_recursive(x):
	if x <= 2:
		return 1

	else:
		return fibo_recursive(x-1) + fibo_recursive(x-2)

'''
fibo_recursive(5)의 경우를 살펴보면,

fibo_recursive(5) = fibo_recursive(4) + fibo_recursive(3)
				  = (fibo_recursive(3) + fibo_recursive(2)) + (fibo_recursive(2) + fibo_recursive(1))
				  = ((fibo_recursive(2) + fibo_recursive(1)) + fibo_recursive(2)) + (fibo_recursive(2) + fibo_recursive(1))
위와 같이 풀어지는데,
해당 연산 과정에서 똑같은 연산이 반복적으로 나타난다는 것을 확인할 수 있다.
이렇듯 동일한 연산의 결과를 메모리 공간에 저장하여, 연산 수를 기하급수적으로 줄이는 방식이
동적 프로그래밍의 개념이다.
'''

# 메모이제이션(Memoization)을 이용한 피보나치 수열 구현
d = [0] * 100

# top-down 방식
def fibo_memo_td(x):
	if x <= 2:
		return 1

	if d[x] != 0:
		return d[x]

	d[x] = fibo_memo(x-1) + fibo_memo(x-2)

	return d[x]

# bottom-up 방식
def fibo_memo_bu(x):
	d = [0] * 100
	d[1] = 1
	d[2] = 1

	for i in range(3, 100):
		d[i] = d[i-1] + d[i-2]

	return d[x]



# Q1. 1로 만들기
'''
정수 X가 주어졌을 때, 주어진 연산을 통해서 해당 정수를 1로 만드는 가장 최연소 연산수를 구하는 문제
점화식으로 표현이 되는 문제인지를 항상 생각하자
'''
def solution_Q1_bottomup(input_num):
	d_list = [0] * 30001

	for i in range(2, 30001):
		result = 1 + d[i-1]

		if i%5 == 0:
			a_result = d[i//5] + 1
			
		if i%3 == 0:
			b_result = d[i//3] + 1

		if i%2 == 0:
			c_result = d[i//2] + 1

		d[i] = min(result, a_result, b_result, c_result)

	return d_list[input_num]


def solution_Q1_topdown(input_num):
	d_list = [0] * len(input_num)

	def solution(input_num):
		if input_num == 1:
			return 0
		d_list[input_num] = solution(input_num-1) + 1

		if input_num % 2 == 0:
			d_list[input_num] = min(d_list[input_num], solution(input_num//2) + 1)
		elif input_num % 3 == 0:
			d_list[input_num] = min(d_list[input_num], solution(input_num//3) + 1)
		elif input_num % 5 == 0:
			d_list[input_num] = min(d_list[input_num], solution(input_num//5) + 1)
		else:
			pass

		return d_list[input_num]

	result = solution(input_num)
	return result


# Q2. 개미 전사 ***



# Q3. 바닥 공사
def solution_Q3(input_num):
	d_list = [0] * 1001
	d_list[1] = 1
	d_list[2] = 3

	for i in range(3, 1001):
		d_list[i] = d_list[i-1] + d_list[i-2] * 2

	return d_list[input_num]



# Q4. 효율적인 화폐구성 ***
'''
책에서 제공해주는 풀이가 훨씬 간결하다.
책에서 나온 풀이도 복습하여 해당 방식의 풀이법도 익히도록 하자.
'''

def solution_Q4(input_list, target):
	d = [0] * 10001
	coin_list = sorted(coin_list, reverse = True)

	for coin in coin_list:
		d[coin] = 1

	for i in range(1, target+1):
		for coin in coin_list:
			if (i - coin >= 0) & (d[i - coin] != -1):
				d[i] = d[i - coin] + 1
				break
			else:
				d[i] = -1

	return d[target]