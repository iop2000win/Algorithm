# 거스름 돈 문제

def solution(input_value):
    remains = input_value
    coin_count = 0

    for coin in [500, 100, 50, 10]:
        coin_count += remains // coin
        remains %= coin

    return coin_count



# 가장 큰 수 만들기 문제

def solution_1(N, M, K, input_list):
    input_list.sort()
    count = 0
    result = 0
    
    while M!= 0:
        count += 1
        print(f'count: {count}')
        
        if count % (K+1) != 0:
            result += input_list[-1]
            print(f'This time (count: {count}) we add the biggest number.')
        else:
            result += input_list[-2]
            print(f'This time (count: {count}) we add the second biggest number.')

        M -= 1
        if count == K+1:
            count = 0
        print(result)
        
    return result


def solution_2(N, M, K, input_list):
    input_list.sort()
    
    count = M // (K+1)
    remains = M % (K+1)
    
    value = input_list[-1] * K + input_list[-2]
    
    return value * count + input_list[-1] * remains



# 숫자 카드 게임 문제

def solution(N, M, input_matrix):
    result = 0
    
    for i in range(N):
        min_val = min(input_matrix[i])
        
        if min_val > result:
            result = min_val

        # result = max(result, min_val)
        # max 함수를 활용하여 if문 없이 위 조건을 해결할 수 있다.

    return result



# 1이 될 때까지 문제

'''
남은 숫자가 K의 값보다 작아졌을 때를 고려하지 못한 실수가 나올 수 있다.
N 값이 0이 될 때까지가 아닌 1이 될 때까지이기 때문에,
마지막 연산이 나누기가 아니고 -1 처리일 때 연산 횟수 카운트에서 실수가 발생할 수 있으니
유의가 필요하다.
'''

def solution(N, K):
    result = 0
    
    while N >= K:
        if N % K == 0:
            N = N//K
            result += 1
#             print(N)
            
        else:
            remains = N % K
            N -= remains
            result += remains
#             print(N)
            
    while N > 1:
        N -= 1
        result += 1
            
    return result