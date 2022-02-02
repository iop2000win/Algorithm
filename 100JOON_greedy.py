# Q. 잃어버린 괄호
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

	return result