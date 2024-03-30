# def solution(a, b):
#     ab = int(str(a) + str(b))
#     ba = int(str(b) + str(a))
    
#     if ab >= ba :
#         return ab
#     else :
#         return ba
# # 문자로 변환 후 합치고 숫자로 되돌려서 비교 후 출력

# def solution(route):
#     east = 0
#     north = 0
#     for i in route:
#         if i == "N":
#             north += 1
#         elif i == "S" :    
#             north -= 1
#         elif i == "E" :
#             east += 1

#         elif i == "W":
#             east -= 1

#     return [east, north]

# def solution(arr):
#     for i in range(len(arr)):
#         print(str(arr[i]), end="")
    # print(arr[0], end="") 
    # print(arr[1], end="")
    # print(arr[2], end="")
    
    # answer = 0
    # return answer
        
# a, b = map(int, input().strip().split(' '))
# print(a, '+' , b ,'=', a+b )