
2
3
4
5
6
7
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer

print(solution("banana"))
