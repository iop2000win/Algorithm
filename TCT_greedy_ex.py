# Q1. 모험가 길드 문제

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