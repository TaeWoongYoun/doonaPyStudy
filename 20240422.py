# def solution(names):
#     answer = []
#     list_size = 5
#     for i in range(0, len(names), list_size):
#         answer.append(names[i])

#     return answer

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer
