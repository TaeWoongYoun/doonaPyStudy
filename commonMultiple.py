def solution(number, n, m):

    if number % n == 0 and number % m == 0:
        answer = 1
        return answer
    else:
        answer = 0
        return answer

# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
# number을 n과 m으로 나눴을 때 둘 다 0으로 나누어 떨어진다면 answer = 1?