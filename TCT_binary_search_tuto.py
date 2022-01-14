# 이진 탐색의 기본적인 구현
'''
재귀함수를 이용한 방법과 반복문을 이용한 방법으로 이진 탐색을 구현할 수 있다.
가장 기본적인 형태의 이진 탐색 코드를 제대로 이해하고 숙달하여 언제든지 쉽게 구현할 수 있도록 암기하도록 하자.
'''

# 재귀함수를 이용한 이진 탐색 구현
def binary_search_recursive(array, target, start, end):
	# 탐색하고자 하는 target이 주어진 배열에 없을 경우에 대한 대비
	if start > end:
		return None

	mid = (start + end) // 2

	if array[mid] == target:
		return mid

	elif array[mid] > target:
		return binary_search_recursive(array, target, start, mid-1)

	else:
		return binary_search_recursive(array, target, mid+1, end)


# 반복문을 이용한 이진 탐색 구현
def binary_search_iterative(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2

		if array[mid] == target:
			return mid

		elif array[mid] > target:
			end = mid - 1

		else:
			start = mid + 1

	return None


'''
* 위의 코드에서 target이 없을 때 None이 리턴되도록 하기위한 조건에 대한 이해

array = [1, 3, 5, 6, 9, 11, 13]
target = 7

이 경우에 대해서, start = 0, end = 6, mid = 3
가운데 원소인 6과 타겟인 7을 비교 >>> 타겟 값이 더 크므로 뒷 쪽만 확인한다. (start = 4가 된다.)
>>> [1, 3, 5, 6, [9, 11, 13]] >>> 가운데 원소인 11과 타겟인 7을 비교 >>> 타겟 값이 더 작으므로 앞쪽만 확인한다. (end = 4가 된다.)
>>> [1, 3, 5, 6, [[9], 11, 13]] >>> start와 end의 값이 같아지고, 따라서 mid의 값도 같아진다.
>>> 하나 남은 원소는 타겟 값이 아니므로, 만약 해당 원소 값이 타겟보다 큰 경우 end의 값이 -1, 해당 원소 값이 타겟보다 작은 경우 start의 값이 +1이 되며
어떤 경우든 start와 end값의 크기에서 역전이 발생하며, 이 시점에서는 모든 원소를 이미 탐색한 경우이기 때문에 더 이상의 탐색이 이루어져선 안된다.

따라서 이진 탐색의 종료 조건은 start와 end의 값에 역전이 일어나는 순간으로 설정하여야 한다.
'''


# Q2. 떡볶이 떡 만들기
'''
전형적인 이진탐색을 통한 파라메트릭 서치 문제
문제의 풀이를 아는 것도 중요하지만, 가장 중요한 것은 이런 유형의 문제에서 이진 탐색 풀이를
떠올리는 것!!

단순히 greedy 형식으로 접근해서 문제를 풀이할 수도 있지만, 그럴 경우 연산 시간이 매우 오래 걸리게 된다.
문제를 받았을 때, 주어진 파라미터의 범위를 보고 대략적인 풀이 방향을 잡는 것도 중요!
'''

def solution(rq, input_list):
	start = 0
	end = max(input_list)

	result = 0

	while start <= end:
		mid = (start + end) // 2

		left = sum([x-mid if x-mid > 0 else 0 for x in input_list])

		if left < rq:
			end = mid-1
		else:
			result = mid
			start = mid+1

	return result