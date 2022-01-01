n = int(input('공간의 크기를 입력하세요'))
m = list(map(str, input('이동 경로를 입력하세요.').split()))
result = list(map(int, [1, 1]))

for a in m:
    if a == "r" and result[1] < n:
        result[1] += 1
    elif a == "l" and result[1] > 1:
        result[1] -= 1
    elif a == "u" and result[0] > 1:
        result[0] -= 1
    elif a == "d" and result[0] < n:
        result[0] += 1

print(result)
