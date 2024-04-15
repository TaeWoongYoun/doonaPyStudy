# def solution(a, b, c):
#     answer = a+b+c
#     if a==b==c:
#         answer = answer*(a**2+b**2+c**2)*(a**3+b**3+c**3)
#     elif a==b or b==c or c==a:
#         answer = answer*(a**2+b**2+c**2)
#     return answer

def solution(my_string, queries):
    answer = list(my_string)
    
    for start, end in queries:
        answer[start: end + 1] = answer[start: end + 1][::-1]

    return ''.join(answer)