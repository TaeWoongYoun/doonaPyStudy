def solution(babbling):
    a = ["aya","ye","woo","ma"]
    answer = 0
    for i in babbling:
        result = 0
        for j in range(4):
            if i.find(a[j]) != -1:
                result += len(a[j])
        if len(i) == result:
            answer += 1
        
    return answer

def solution(x):
    answer = False
    x_sum = 0
    
    for i in str(x):
        x_sum += int(i)
    
    if x % x_sum == 0:
        answer = True
    
    return answer

# def solution(dots):
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]= dots
# answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
# answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
# answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
# return 1 if answer1 or answer2 or answer3 else 0

# from itertools import combinations

# def solution(dots):
#     new_dots = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
#     com = list(combinations(new_dots, 2))

# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]

def solution(wallpaper):
    x, y = set(), set()

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x.add(i)
                y.add(j)
                
    return [min(x), min(y), max(x) + 1, max(y) + 1]