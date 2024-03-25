# 조건문자열
def solution(ineq, eq, n, m):

    a = ineq == "<" and eq == "=" and n <= m and True
    b = ineq == ">" and eq == "=" and n >= m and True
    c = ineq == "<" and eq == "!" and n < m and True
    d = ineq == ">" and eq == "!" and n > m and True

    if a or b or c or d:
        return 1
    else :
        return 0

# 카운트업
def solution(start_num, end_num):
    answer = []

    for i in range(start_num, end_num+1):
        
        answer.append(i)
    return answer

# 콜라츠 수열 만들기
def solution(n):
    answer = [n,]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = 3 * n + 1
        answer.append(n)

    return answer