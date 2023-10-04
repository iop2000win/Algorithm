'''
백준 온라인 저지 사이트에서 제공하는 단계별 문제풀이 카테고리의
재귀함수/동적 계획법1 & 재귀함수 카테고리의 문제 풀이 코드
'''

# Q 1003. 피보나치 함수
'''
피보나치 함수가 작동했을 때, 0과 1이 호출되는 횟수를 리턴하는 함수
'''
def fibo(input_num):
    d = [0] * 41
    count_0 = [0] * 41
    count_1 = [0] * 41
    
    for i in range(input_num+1):
        if i == 0:
            count_0[i] = 1
            d[i] = 0
        elif i == 1:
            count_1[i] = 1
            d[i] = 1
        else:
            d[i] = d[i-1] + d[i-2]
            count_0[i] = count_0[i-1] + count_0[i-2]
            count_1[i] = count_1[i-1] + count_1[i-2]
            
    print(count_0[input_num], count_1[input_num])


# Q 1149. RGB 거리 ***
'''
주어진 비용을 단계에 따라 업데이트 해나가는 방식!!!
이전에도 이런 방식의 문제가 있었는데... 
이런 식의 접근법을 떠올릴 수 있도록, 이런 유형의 문제에 익숙해지도록 하자!!
'''

n = int(input())
cost_list = [list(map(int, input().split())) for _ in range(n)]

def solution_Q1149(input_list):
	# R, G, B 를 0, 1, 2로 대응
	for i in range(1, len(input_list)):
		input_list[i][0] = min(input_list[i-1][1], input_list[i-1][2]) + input_list[i][0]
		input_list[i][1] = min(input_list[i-1][0], input_list[i-1][2]) + input_list[i][1]
		input_list[i][2] = min(input_list[i-1][0], input_list[i-1][1]) + input_list[i][2]

	return min(input_list[-1])

result = solution_Q1149(cost_list)
print(result)


# Q 1932. 정수 삼각형
'''
위 RGB 문제와 똑같은 문제!
'''

n = int(input())
tri_list = [list(map(int, input().split())) for _ in range(n)]

def solution_Q1932(input_list):
    for i in range(1, len(input_list)):
        for j in range(len(input_list[i])):
            if j == 0:
                input_list[i][j] += input_list[i-1][j]
            elif j == len(input_list[i])-1:
                input_list[i][j] += input_list[i-1][j-1]
            else:
                input_list[i][j] = input_list[i][j] + max(input_list[i-1][j], input_list[i-1][j-1])

    return max(input_list[-1])

result = solution_Q1932(tri_list)
print(result)


# Q 2579. 계단 오르기

n = int(input())
stair_list = [0] + [int(input()) for _ in range(n)]

def solution_Q2579(input_list):
    d = [0] * (len(input_list))
    if len(input_list) <= 2:
        return sum(input_list)
    
    d[1] = input_list[1]
    d[2] = input_list[1] + input_list[2]
    
    for i in range(3, len(input_list)):
        val_1 = d[i-2] + input_list[i]
        val_2 = d[i-3] + input_list[i-1] + input_list[i]
        
        d[i] = max(val_1, val_2)
        
    return d[len(input_list)-1]

result = solution_Q2579(stair_list)
print(result)



# Q 1463. 1로 만들기

input_num = int(input())

def solution_1463(input_num):
    d = [0] * (input_num + 1)
    
    for i in range(2, input_num + 1):
        min_val = d[i-1] + 1
        if i%3 == 0:
            min_val = min(min_val, d[i//3] + 1)
        if i%2 == 0:
            min_val = min(min_val, d[i//2] + 1)
        
        d[i] = min_val
        
    return d[input_num]

result = solution_1463(input_num)
print(result)



# Q 10844. 쉬운 계단 수
'''
더 간결한 풀이가 있을 것이다. 복습 단계에서 생각해보자!
'''
input_num = int(input())

def solution_Q10844(input_num):
    d = [0] + [1] * 9

    for i in range(1, input_num):
        num_0 = d[1]
        num_1 = d[0] + d[2]
        num_2 = d[1] + d[3]
        num_3 = d[2] + d[4]
        num_4 = d[3] + d[5]
        num_5 = d[4] + d[6]
        num_6 = d[5] + d[7]
        num_7 = d[6] + d[8]
        num_8 = d[7] + d[9]
        num_9 = d[8]

        d[0] = num_0
        d[1] = num_1
        d[2] = num_2
        d[3] = num_3
        d[4] = num_4
        d[5] = num_5
        d[6] = num_6
        d[7] = num_7
        d[8] = num_8
        d[9] = num_9

    return sum(d) % 1000000000

result = solution_Q10844(input_num)
print(result)



# Q 9184. 신나는 함수 실행
'''
재귀함수에 대한 이해!!!
dp table의 값을 반환하는 부분을 잘 생각하자!!
'''
def solution_Q9184(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return 1
    elif (a > 20) or (b > 20) or (c > 20):
        return solution_Q9184(20, 20, 20)
    elif (a < b < c):
        if d[a][b][c]:
            return d[a][b][c]
        else:
            d[a][b][c] = solution_Q9184(a, b, c-1) + solution_Q9184(a, b-1, c-1) - solution_Q9184(a, b-1, c)
            return d[a][b][c]
    else:
        if d[a][b][c]:
            return d[a][b][c]
        else:
            d[a][b][c] = solution_Q9184(a-1, b, c) + solution_Q9184(a-1, b-1, c) + solution_Q9184(a-1, b, c-1) - solution_Q9184(a-1, b-1, c-1)
            return d[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if (a == -1) and (b == -1) and (c == -1):
        break
    
    result = solution_Q9184(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')



# Q 1904. 01타일
'''
문제를 보고 적합한 점화식을 세울 수 있는지 묻는 문제
점화식을 사용해야하는 문제라고 판단이 되면, 이전 항과 다음 항 간의 관계식을 잘 생각해보자!
'''
def solution_Q1904(input_num):
    d = [0] * 1000001
    d[1] = 1
    d[2] = 2

    for i in range(3, input_num+1):
        d[i] = d[i-2] + d[i-1]

    return d[input_num]

input_num = int(input())
result = solution_Q1904(input_num)
print(result)


# Q 9461. 파도반 수열
def solution_Q9461(input_num):
    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2

    for i in range(6, input_num + 1):
        d[i] = d[i-1] + d[i-5]

    return d[input_num]

input_num = int(input())
result = solution_Q9461(input_num)
print(result)


# Q 11053. 가장 긴 증가하는 부분 수열
def solution_Q11053(input_list):
    d = [1] * 1001

    for i in range(1, len(input_list)):
        for j in range(i):
            if input_list[i] > input_list[j]:
                d[i] = max(d[i], d[j] + 1)

    return max(d)

n = int(input())
input_list = list(map(int, input().split()))

result = solution_Q11053(input_list)
print(result)



# Q 11054. 가장 긴 바이토닉 부분 수열
def solution_Q11054(input_list):
    d_inc = [1] * 1001
    d_dec = [1] * 1001

    for i in range(len(input_list)):
        for j in range(i):
            if input_list[i] > input_list[j]:
                d_inc[i] = max(d_inc[i], d_inc[j] + 1)

    for i in range(len(input_list)-1, -1, -1):
        for j in range(len(input_list)-1, i, -1):
            if input_list[i] > input_list[j]:
                d_dec[i] = max(d_dec[i], d_dec[j] + 1)

    for i in range(n):
        d_inc[i] = d_inc[i] + d_dec[i]

    return max(d_inc) - 1

n = int(input())
input_list = list(map(int, input().split()))

result = solution_Q11054(input_list)
print(result)


# Q 1912. 연속합
def solution_Q1912(input_list):
    d = [0] * n
    d[0] = input_list[0]

    for i in range(1, n):
        d[i] = max(input_list[i], d[i-1] + input_list[i])

    return max(d)

n = int(input())
input_list = list(map(int, input().split()))

result =solution_Q1912(input_list)
print(result)


# Q 2565. 전깃줄
def solution_Q2565(input_list):
    d = [1] * n
    for i in range(len(input_list)):
        for j in range(i):
            if input_list[i][1] > input_list[j][1]:
                d[i] = max(d[i], d[j] + 1)

    result = n-max(d)
    return result

n = int(input())
input_list = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: x[0])

result = solution_Q2565(input_list)
print(result)


# Q 27433. 팩토리얼
def solution_Q27433(input_num):
    if (input_num == 0) or (input_num == 1):
        return 1
    
    else:
        return input_num * solution(input_num-1)

n = int(input())

result = solution_Q27433(n)
print(result)


# Q 10870. 피보나치 수열
def solution_Q10870(input_num):
    if input_num == 0:
        return 0
    elif input_num == 1:
        return 1
    else:
        return solution_Q10870(input_num-1) + solution_Q10870(input_num-2)

n = int(input())

result = solution_Q10870(n)
print(result)


# Q 25501. 재귀의 귀재
# what is Palindrome? 회문, 거꾸로 읽어도 제대로 읽은 것과 동일한 배열
def palin(input_str, l, r):
    global cnt
    cnt += 1
    
    if l >= r:
        return 1
    elif input_str[r] != input_str[l]:
        return 0
    else:
        return palin(input_str, l+1, r-1)
    
T = int(input())
for t in range(T):
    txt = input()
    cnt = 0
    
    result = palin(txt, 0, len(txt)-1)
    print(result, cnt)


# Q 2447. 별찍기
'''
이전 스텝의 패턴에 대해서,
p p p
p 0 p
p p p 형태로 출력하는 것을 재귀적으로 구현하는 문제
'''
def solution_Q2447(input_num):
    if input_num == 1:
        return '*'

    x_pat = solution_Q2447(input_num/3)
    x_len = len(x_pat.split('\n')[0])

    new_pat = ''
    for x in x_pat.split('\n'):
        new_pat += x*3
        new_pat += '\n'

        new_pat += f"{x}{' '*x_len}{x}"
        new_pat += '\n'

        new_apt += x*3
        new_pat += '\n'

    new_pat = new_pat.rstrip('\n')

    return new_pat

input_num = int(input())
result = solution_Q2447(input_num)
print(result)


# Q 11729. 하노이탑 이동순서
'''
단순히 하노이탑의 이동 횟수만 카운트하는 것은 점화식을 이용하면 매우 간단하다.
move_cnt = move_cnt_before + 1 + move_cnt_before
- 이전 단계를 통해 마지막 한칸을 제외한 모든 탑을 옮기는 횟수(move_cnt_before)
- 마지막 칸을 세번째 칸으로 옮기는 횟수(1)
- 1번 단계에서 옮긴 탑을 다시 마지막 칸으로 옮기는 횟수, 이전 단계의 이동 횟수와 동일(move_cnt_before)

but, 이 문제에서는 단순히 횟수만 구하는게 아니라 각 탑의 이동 루트를 모두 계산해야 하는 문제이다.
개념은 똑같다. 탑의 출발지점과 도착지점만 변경해주면 되는 문제
* python에서 문자열에 대해서 제공하는 maketrans, translate 메서드를 활용하면 문제를 쉽게 해결할 수 있다.
'''
def solution_Q11729(input_num):
    # 재귀 함수에서 가장 중요한 것은, 재귀함수가 종료되는 시점을 설정해주는 것!
    if input_num == 1:
        route = '1 3'

        return route

    else:
        x_route = solution_Q11729(input_num-1)

        tbl_1 = str.maketrans('23', '32')
        tbl_2 = str.maketrans('12', '21')

        route = x_route.translate(tbl_1) + '\n1 3\n' + x_route.translate(tbl_2)

        return route

input_num = int(input())
result = solution_Q11729(input_num)
print(len(result.split('\n')))
print(result)


# Q 4779. 칸토어 집합
def solution_Q4779(input_num):
    if input_num == 1:
        return '-'
    else:
        l = input_num // 3

        result = solution_Q4779(l) + ' '*l + solution_Q4779(l)
        return result

lines = sys.stdin.readlines()
for line in lines:
    input_num = int(line.strip())
    input_num = 3 ** input_num

    result = solution_Q4779(input_num)
    print(result)


# Q 24416. 피보나치 수열 2
def solution_Q24416(input_num):
    recur_list = [0] * input_num+1
    dynamic_cnt = 0

    for i in range(1, input_num+1):
        if i in (1, 2):
            recur_list[i] = 1
        else:
            dynamic_cnt += 1
            recur_list[i] = recur_list[i-1] + recur_list[i-2]

    return recur_list[input_num], dynamic_cnt

input_num = int(input())
recur_cnt, dynamic_cnt = solution_Q24416(input_num)
print(recur_cnt, dynamic_cnt)


# Q 12865. 평범한 배낭
'''
동적계획법의 가장 대표적인 문제로,
그리디로는 풀리지 않고, 모든 경우의 수를 계산하기에는 연산양이 너무 많은 문제로
동적계획법을 통해서 풀 수 있다.

동적계획법의 가장 큰 개념은 메모이제이션!
이전의 연산 값을 저장하고, 이를 바탕으로 이후의 연산을 진행한다!
'''
import sys

def solution_Q12865(n, W, goods_list:list): # [(weight, value)]
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i, (w, v) in enumerate(goods_list):
        i += 1
        for j in range(1, W+1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = d[i-1][j]

    return dp[-1][-1]

n, W = map(int, sys.stdin.readline().split())
goods_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = solution_Q12865(n, W, goods_list)
print(result)


# Q 9251. 수열문제
# 점화식의 개념으로 접근하는 문제가 맞는 것 같긴한데... 풀이 방법이 떠오르지가 않는다.
def solution_Q9251(x_str, y_str):
    dp = [[0] * (len(x_str) + 1) for _ in range(len(y_str) + 1)]
    for i in range(1, len(y_str) + 1):
        for j in range(1, len(x_str) + 1):
            if x_str[j-1] == y_str[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(y_str)][len(x_str)]

x_str = input()
y_str = input()

result = solution_Q9251(x_str, y_str)
print(result)


# Q 2156. 포도주 시식
'''
동적계획법을 사용하는 방식으로 접근은 했지만, 결국 개념적으로 문제를 완벽하게 이해하지 못해서
계속된 오답을 작성했다. 수학 문제와 같다. 문제에 대해서 개념적으로 이해를 하는 것이 선행되어야 한다!
* 꼭 다시 풀어보기
'''
def solution_Q2156(input_list):
    dp = [0] * 10000 # 문제에서 최대 입력값의 범위를 10000으로 제한해두었다.
    
    for i in range(len(input_list)):
        if i == 0:
            dp[i] = input_list[i]
        elif i == 1:
            dp[i] = dp[i-1] + input_list[i]
        else:
            val1 = dp[i-3] + input_list[i] + input_list[i-1] # 연속된 두 값을 포함하는 경우
            val2 = dp[i-2] + input_list[i] # 지금 값을 연속하지 않게 포함하는 경우
            val3 = dp[i-1] # 지금 값을 포함하지 않는 경우
            dp[i] = max(val1, val2, val3)

    return dp[len(input_list)-1]

n = int(input())
input_list = [int(input()) for _ in range(n)]

result = solution_Q2156(input_list)
print(result)