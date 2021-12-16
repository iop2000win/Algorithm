# Q1. 모험가 길드 문제 ***

def solution_1_Q1(N, input_list):
    result = 0
    
    while len(input_list) >= input_list[-1]:
        group = []
        for i in range(len(input_list)):
            group.append(input_list[i])
            
            if len(group) == group[-1]:
                result += 1
                input_list = input_list[i+1:]
                
                break
    
    return result


def solution_2_Q2(N, input_list):
    result = 0
    
    member_count = 0
    for i in range(len(input_list)):
        member_count += 1
        if input_list[i] <= member_count:
            result += 1
            member_count = 0
            
    return result



# Q2. 곱하기 혹은 더하기 문제

def solution_Q2(input_str):
    result = int(input_str[0])

    for i in range(1, len(input_str)):
        if (result > 1) & (int(input_str[i]) > 1):
            result *= int(input_str[i])
        else:
            result += int(input_str[i])

    return result



# Q3. 문자열 뒤집기 문제 ***

def solution_1_Q3(input_str):
    first_num = input_str[0]
    start_index = 1
    result = 0

    while start_index != len(input_str) -1:
        check_num = input_str[start_index]

        if check_num == first_num:
            start_index += 1

        else:
            while True:
                start_index += 1
                if input_str[strat_index] == first_num:
                    break

            result += 1

    return result


def solution_2_Q3(input_str):
    count0 = 0
    count1 = 0

    if input_str[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(input_str) -1):
        if input_str[i] != input_str[i+1]:
            if input_str[i+1] == '1':
                count0 += 1

            else:
                count1 += 1

    return min(count0, count1)



# 번외. 부분집합을 구하는 방법 3가지
# 1. 반복문을 통한 구현
def get_subsets_1(input_list):
    subsets = [[]]

    for element in input_list:
        size = len(subsets):

        for i in range(size):
            subsets.append(subsets[i] + [element])

    return subsets


# # 2. 비트연산자를 통한 구현
# def get_subsets_2(input_list):

# 3. itertools를 이용한 구현
def get_subsets_3(input_list):
    import itertools

    subsets = []

    # 공집합부터 전체 원소를 포함한 집합까지 부분집합으로 포함하기 위한 range 설정
    for i in range(len(input_list)+1):
        [subsets.append(list(x)) for x in list(itertools.combinations(input_list, i))]

    return subsets



# Q4. 볼링공 고르기 문제

def solution_1_Q4(N, M, input_list):
    result = 0

    for i in range(len(input_list) -1):
        ball_1 = input_list[i]

        for j in range(len(input_list[i:])):
            ball_2 = input_list[i:][j]

            if ball_1 != ball_2:
                result += 1

    return result


# 위 방식으로 문제를 풀 경우, 시간복잡도가 O(N^2)이 된다.
# 반복문이 이중으로 사용되어서 하나의 원소에 대해서 남은 원소를 전체 순회 하여야하기 때문이다.
# 코드를 좀 더 효율적으로 구성하기 위해선 문제에서 문제를 간소화할 방법을 찾아내야 한다.

def solution_2_Q4(N, M, input_list):
    # M은 볼링공 무게의 범위
    # 즉, 주어지는 모든 볼링공은 1~M까지의 배열에 대응할 수 있다.
    result = 0
    weight_list = [0] * (M+1)
    ball_list = sorted(input_list)

    for ball in ball_list:
        weight_list[ball] += 1

    '''
    조합의 개수를 구하는 방식에 대해서 생각해보자.
    공의 조합은 순서는 고려하지 않는다. 즉 (1번공, 3번공) == (3번공, 1번공)이다.
    무게 1인 1번 공에서 발생할 수 있는 조합은, 무게가 1인 공을 제외한 전체공의 개수만큼이다.
    (공의 무게가 같더라도 공의 번호가 다르면 다른 공으로 취급하기 때문에)

    각 무게별로 몇 개의 공이 주어졌는지를 기록한 후, 확인하는 공에 대해서 해당 공의 무게를 제외한 무게의 공의 총 개수를 곱해주면
    해당 공을 통해 만들 수 있는 조합의 개수가 나온다.
    '''

    for weight, count in enumerate(weight_list):
        N = N - weight # 해당 무게의 공의 개수
        result += count * N

    return result