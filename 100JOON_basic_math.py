# Q 1712. 손익분기점
def solution_Q1712(fixed_cost, variable_cost, price):
    if price - variable_cost > 0:
        profit = price - variable_cost
        result = fixed_cost // profit + 1
    else:
        result = -1

    return result

fixed_cost, variable_cost, price = map(int, input().split())

result = solution_Q1712(fixed_cost, variable_cost, price)
print(result)



# Q 2869. 달팽이는 올라가고 싶다 ***
def solution_Q2869(up, down, target):
    h = target - up
    if h % (up - down) == 0:
        result = h // (up - down) + 1
    else:
        result = h // (up - down) + 2
    
    return result

up, down, target = map(int, input().split())

result = solution_Q2869(up, down, target)
print(result)



# Q 10250. ACM 호텔
def solution_Q10250(floor, room, n):
    room_no = (n // floor) + 1 if (n % floor) != 0 else (n // floor)
    floor_no = (n % floor) if (n % floor) != 0 else floor
    
    if room_no // 10 == 0:
        room_no = '0' + str(room_no)
    else:
        room_no = str(room_no)
        
    result = str(floor_no) + room_no
    return result

T = int(input()):
for _ in range(T):
    floor, room, n = map(int, input().split())
    result = solution_Q10250(floor, room, n)
    print(result)



# Q 2775. 부녀회장이 될테야
def solution_Q2775(floor, room):
    d = [[0] * (n+1) for _ in range(floor+1)]
    
    for i in range(1, room+1):
        d[0][i] = i
        
    for i in range(1, floor+1):
        for j in range(1, room+1):
            for l in range(1, j+1):
                d[i][j] += d[i-1][l]
                
    return d[floor][room]

floor = int(input())
room = int(input())
result = solution_Q2775(floor, room)
print(result)



# Q 2839. 설탕배달
def solution_Q2839(input_num):
    sh = input_num // 5
    rem = input_num % 5

    result = 0

    while sh >= 0:
        if rem % 3 == 0:
            result += sh
            result += rem // 3
            break

        else:
            sh -= 1
            rem += 5

    if result == 0:
        result = -1

    return result

input_num = int(input())
result = solution_Q2839(input_num)
print(result)



# Q 2745. 진법 변환, Q 11005 진법 변환 2 (역으로 진행하는 것으로 개념 자체는 동일하다)
def solution_Q2745(input_num, arith_num):
    arith_dic = {}
    for i in range(36): # 문제에서 최대 36진법까지로 정하고 있다.
        if i <= 9:
            arith_dic[str(i)] = i
        else:
            key = chr(i + 55)
            arith_dic[key] = i

    result = 0

    for i, spell in enumerate(input_num):
        val = arith_dic[spell] * (arith_num ** (len(input_num) - (i+1)))
        result += val

    return result

input_num, arith_num = input().split()
arith_num = int(arith_num)
result = solution_Q2745(input_num, arith_num)
print(result)


def solution_Q11005(input_num, arith_num):
    arith_dic = {}
    for i in range(36): # 문제에서 최대 36진법까지로 정하고 있다.
        if i <= 9:
            arith_dic[i] = str(i)
        else:
            val = chr(i + 55)
            arith_dic[i] = val

    result = ''

    while True:
        remainder = n % b
        n = n // b

        result = s_dic[remainder] + result

        if n == 0:
            break

    return result

input_num, arith_num = map(int, input().split())
result = solution_Q11005(input_num, arith_num)
print(result)



# Q 1193. 분수찾기
def solution_Q1193(input_num):
    S = 0
    num = 0

    while True:
        num += 1
        S += num

        if S > input_num:
            S -= num
            num -= 1
            break

    if input_num-S == 0:
        num1 = num
        num2 = 1

    else:
        num += 1
        num1 = input_num-S
        num2 = num - (input_num-S-1)

    if num % 2 == 0:
        result = f'{num1}/{num2}'
    else:
        result = f'{num2}/{num1}'

    return result

input_num = int(input())
result = solution_Q1193(input_num)
print(result)



# Q 2292. 벌집
def solution_Q2292(input_num):
    n = 1
    s = 0

    while True:
        if n == 1:
            a = 1
        else:
            a = 6*(n-1)

        s += a
        if input_num <= s:
            return n

        n += 1

input_num = int(input())
result = solution(input_num)
print(result)



# Q 5086. 배수와 약수
def solution_Q5086(num1, num2):
    if num1 % num2 == 0:
        result = 'multiple'
    elif num2 % num1 == 0:
        result = 'factor'
    else:
        result = 'neither'

    return result

while True:
    num1, num2 = map(int, intpu().split())
    if (num1 == 0) & (num2 == 0):
        break

    else:
        result = solution(num1, num2)
        print(result)



# Q 2501. 약수 구하기
def solution_Q2501(input_num, k):
    count = 0

    for i in range(1, input_num+1):
        if input_num % i == 0:
            count += 1
            if count == k:
                return i

    return 0

input_num, k = map(int, input().split())
result = solution_Q2501(input_num, k)
print(result)