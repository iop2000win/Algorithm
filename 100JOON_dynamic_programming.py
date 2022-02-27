'''
백준 온라인 저지 사이트에서 제공하는 단계별 문제풀이 카테고리의
동적 계획법1 카테로리의 문제 풀이 코드
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



######
def solution():
    return