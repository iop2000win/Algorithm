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