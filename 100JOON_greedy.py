# Q 1541. 잃어버린 괄호
'''
뭔가 더 좋은 풀이법이 분명 있는데... 아우우우...
'''

def solution(input_str):
	if '-' in input_str:
		x = input_str.index('-')
		plus_part = input_str[:x]
		minus_part = input_str[x+1:]
		minus_part = minus_part.replace('+', '-')

		plus_part = sum(list(map(int, plus_part.split('+'))))
		minus_part = sum(list(map(int, minus_part.split('-'))))

		result = plus_part - minus_part

	else:
		result = sum(list(map(int, input_str.split('+'))))

	return 


# Q 11047. 동전 0

def solution(coin_list, target):
	coin_list = sorted(coin_list, reverse = True)
	result = 0

	for coin in coin_list:
		result = result + (k // coin)
		k = k % coin

	return result


# Q 11399. ATM

def solution(time_list):
	time_list = sorted(time_list)
	result = 0

	for i in range(len(time_list)):
		result += (time_list[i] * (len(time_list) - i))

	return result


# Q 13305. 주유소

def solution(roads_list, cities_list):
	total_cost = cities_list[0] * roads_list[0]

	for i in range(1, len(cities)-1):
		cities[i] = min(cities[i], cities[i-1])
		total_cost += (cities[i] * roads[i])

	return total_cost


# Q 1931. 회의실 배정

def solution(meet_info):
	meet_info = sorted(meet_info)
	schedule = [meet_info[0]]

	for i in range(1, len(meet_info)):
		b_meet = schedule[-1]
		f_meet = meet_info[i]

		if b_meet[1] > f_meet[1]:
			schedule.pop()
			schedule.append(f_meet)

		else:
			b_finish = b_meet[1]
			f_start = f_meet[0]

			if f_start >= b_finish:
				schedule.append(f_meet)

	return len(schedule)