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