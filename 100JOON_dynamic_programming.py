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

