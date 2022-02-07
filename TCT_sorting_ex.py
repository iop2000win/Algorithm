# Q23. 국영수

def solution_Q23(input_list):
	student_list = input_list.copy()
	student_list = sorted(student_list, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3])))

	for student in student_list:
		print(student[0])

	return

n = int(input())
input_list = [tuple(input().split()) for x in range(n)]