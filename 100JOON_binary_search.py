'''
백준 온라인 저지 사이트에서 제공하는 단계별 문제풀이 카테고리의
이분 탐색 카테로리의 문제 풀이 코드
'''

# Q 1920. 수 찾기
'''
이진 탐색 알고리즘을 작성할 수 있는지 물어보는 기초적인 문제
'''

import sys

n = int(input())
# num_list = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, input().split()))
num_list = sorted(num_list)

m = int(input())
# target_list = list(map(int, sys.stdin.readline().split()))
target_list = list(map(int, input().split()))

def binary_search(input_list, start, end, target):
	if start > end:
		return 0

	mid_index = (start + end) // 2
	if input_list[mid_index] == target:
		return 1
	elif input_list[mid_index] < target:
		return binary_search(input_list, mid_index+1, end, target)
	else:
		return binary_search(input_list, start, mid_index-1, target)

start = 0
end = len(num_list)-1
for target in target_list:
	print(binary_search(num_list, start, end, target))



# Q 10816. 숫자카드2
'''
이진탐색 카테고리의 문제이므로, 이진탐색을 이용하여 푸는 풀이법이 있을텐데,
현재 풀이법을 찾지못해, 우선 계수 정렬의 개념을 활용하여 풀었다.
'''

import sys

n = int(input())
# n = int(sys.stdin.readline())
num_list = list(map(int, input().split()))
# num_list = list(map(int, sys.stdin.readline().split()))
num_list = sorted(num_list)

m = int(input())
# m = int(sys.stdin.readline())
target_list = list(map(int, input().split()))
# target_list = list(map(int, sys.stdin.readline().split()))

def solution_Q10816(num_list, target_list):
	count_list = [0] * 20000001
	for num in num_list:
		count_list[num] += 1

	for target in target_list:
		print(count_list[target], end = ' ')

	return


# Q 1654. 랜선 자르기
'''
이진탐색의 개념을 이용하여 최댓값, 최솟값을 찾는 문제로,
이코테 연습문제의 떡 자르기와 같은 문제이다.
이와같은 응용을 묻는 질문이 많으니 해당 개념에 익숙해지도록 하자.
* 문제의 조건을 잘 확인하자. 입력되는 값이 '자연수'라는 부분을 놓쳐서,
 이진탐색의 시작점을 0으로 설정하는 바람에 에러가 발생하였다.
'''

n, target = map(int, input().split())
len_list = [int(input()) for _ in range(n)]

def solution_Q1654(len_list, target):
	start, end = 1, max(len_list)
	max_len = 0

	while start <= end:
		mid = (start + end) // 2
		total_count = 0

		for l in len_list:
			total_count += l//mid

		if total_count >= n:
			max_len = mid
			start = mid+1
		else:
			end = mid-1

	return max_len

result = solution_Q1654(len_list, target)
print(result)