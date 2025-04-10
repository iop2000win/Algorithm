'''
다이나믹 프로그래밍에서 가장 중요한 개념은
1. 점화식
2. 메모리를 이용한 연산 시간의 단축

이전 단계의 리턴 값을 다음 단계의 리턴 값에 활용하는 문제를 풀기 위해 사용하는 알고리즘이며,
일종의 재귀함수라고 볼 수 있다.
다만 결정적인 차이점은 메모이제이션이라고 불리는 메모리의 활용 부분에 있다.

일반 점화식을 활용할 경우,
한 번의 연산이 진행될 때마다 처음부터 해를 계속 계산하는 작업을 반복해야한다.
이미 계산했던 결과에 대해서도 반복적으로 계산을 계속하기 때문에 연산 시간에서 낭비가 매우 크다.
이를 해결하기 위해 한 번 계산한 결과값을 메모리에 저장해두고,
해당 값에 대해 다시 요청이 올 경우 계산을 다시하는 것이 아니라 메모리에 저장돼있는 값을
읽어오는 방식으로 문제를 해결한다.

예를 들어, 대표적인 재귀함수인 피보나치 수열의 경우를 보자.
피보나치 수열의 10번째 수는 9번째 수와 8번째 수를 합한 값이다.
- f(10) = f(9) + f(8)
이 때, 
- f(9) = f(8) + f(7) 이며
- f(9) = f(7) + f(6) + f(7)
- f(9) = f(6) + f(5) + f(6) + f(6) + f(5)
- ...
이런 식으로 동일한 값에 대해서도 매번 새로 다시 연산을 진행하게 된다.
매 단계에서 2개의 연산이 진행되므로 2의 제곱으로 연산량이 늘어난다.
즉, 시간 복잡도 2^n을 가지게 되며 이는 매우 큰 숫자다.

하지만 메모이제이션을 활용할 경우,
- f(10) = f(9) + f(8) 에서 f(9)를 계산하기 위해 이전 수열을 계속 찾아갈 경우,
한 번 계산한 값은 메모리에 저장해놓기 때문에, 다음 단계를 계산하기 위해서는 해당 값을 가져오기만 하면 된다.
따라서 시간 복잡도 n을 가지게 되며 매우 효율적인 계산이 가능해진다.
'''
from typing import List, Dict

# Pascal's Triangle
# class 형태로 솔루션을 만들기도 하는구나.
# 내부 선언 측면에서는 좀 편하려나?
class Solution___Pascal:
	# 재귀를 이용한 풀이
	def generate(self, numRows: int) -> (Dict[int, List], Dict[int, List]):
		memo_recur = {}
		memo_loop = {}

		_ = self.pascal_f_recur(numRows, memo_recur)
		_ = self.pascal_f_loop(numRows, memo_loop)

		return memo_recur, memo_loop


	def pascal_f_recur(self, numRows: int, memo: Dict) -> Dict[int, List]:
		# 함수 안에서 memo를 선언할 경우 초기화가 일어난다.
		# 외부에서 선언한 변수를 가지고와서 데이터를 업데이트 해주는 방식으로 활용해야한다.
		# 또한 재귀함수는 함수 내에서 자신을 호출해야한다는 사실을 늘 명심하자.
		# 리턴 값이 어떤 값, 어떤 형태로 나와야 재귀함수가 작동할 수 있는지에 대해서도 고려할 것!

		# 이 문제에서는 이전 단계의 결과값을 읽어와서 해당 값을 통해
		# 이번 단계의 결과값을 생성한 후, '그 결과값' 메모에 저장한 후 리턴해야한다.

		if numRows == 1: # 문제에서 첫번째 행을 1로 지정
			rows = [1]
			memo[numRows] = rows

		else:
			# 재귀를 통해 이전 단계의 결과 값을 가져온다.
			b_rows = self.pascal_f_recur(numRows-1, memo)

			rows = [1]
			for i in range(len(b_rows)-1):
				rows.append(b_rows[i] + b_rows[i+1])
			rows.append(1)

			memo[numRows] = rows

		return memo[numRows]


	def pascal_f_loop(self, numRows: int, memo: Dict) -> Dict[int, List]:
		# 반복문을 이용하여 메모이제이션을 활용하는 방법
		# 재귀방식을 하향식, 반복문 방식을 상향식이라고 부른다.
		# 재귀방식의 경우 요청한 값에서부터 시작해서 이전 단계로 한 단계씩 내려가며 해를 구하고,
		# 반복문 방식의 경우 처음부터 시작해서 요청 값까지 한 단계식 올라가며 해를 구하기 때문이다.
		for i in range(1, numRows+1):
			if i == 1:
				memo[i] = [1]
			else:
				b_rows = memo[i-1]

				rows = [1]
				for j in range(len(b_rows)-1):
					rows.append(b_rows[j] + b_rows[j+1])
				rows.append(1)

				memo[i] = rows

		return memo[numRows]


class Solution___BestTime:
	def max_profit(self, prices: List[int]) -> int:
		for i in range(len(prices)):
			if i == 0:
				min_val = prices[i]
				max_profit = 0
			else:
				max_profit = max(max_profit, prices[i]-min_val)
				min_val = min(min_val, prices[i])

		return max_profit


class Solution___CountBit:
	def count_bits(self, n: int) -> List[int]:
		result_list = [0]

		for i in range(1, n+1):
			if i%2 == 0:
				r = result_list[i//2]
				r += 0
				result_list.append(r)
			else:
				r = result_list[i//2]
				r += 1
				result_list.append(r)

		return result_list


class Solution___IsSubseq:
	'''
	while 문을 사용하는 방법도 생각해보기
	두 문제의 인덱스를 각각 for문으로 반복하지 않아도 된다.
	'''
	def is_subseq(self, s: str, t: str) -> bool:
		cnt = 0
		start_index = 0
		for i in range(len(s)):
			for j in range(start_index, len(t)):
				if s[i] == t[j]:
					cnt += 1
					start_index = j+1
					break

			if i+1 != cnt:
				return False

		return True

    def is_subseq_others(self, s: str, t: str) -> bool:
        i=0
        j=0
        while(i<len(s) and j<len(t)):
            if (s[i]==t[j]):
                i+=1
                j+=1
            else:
                j+=1
        if(i<len(s) and j==len(t)):
            return False
        return True
        

class Solution___MinCost:
	def min_climbing_cost()





class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        str_lst = [words[0]]
        group_num = groups[0]
        idx = 1
        
        while idx < len(words):
            if group_num != groups[idx]:
                str_lst.append(words[idx])
                group_num = groups[idx]
                
            idx += 1
            
        return str_lst




class Solution:
    def tribonacci(self, n: int) -> int:
        tribo_list = {}
        tribo_list[0] = 0
        tribo_list[1] = 1
        tribo_list[2] = 1
        
        for i in range(3, n+1):
            tribo_list[i] = tribo_list[i-1] + tribo_list[i-2] + tribo_list[i-3]
            
        return tribo_list[n]




class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:



