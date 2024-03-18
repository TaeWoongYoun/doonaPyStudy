def solution(my_string, overwrite_string, s):

    a = my_string[:s]
    b = overwrite_string
    c = my_string[s + len(overwrite_string):]
    answer = a + b + c
    return answer



# 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.