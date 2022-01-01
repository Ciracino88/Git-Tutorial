# 01
n, m = map(int, input("행과 열을 입력하세요.").split())
result =0

for i in range(n):
    data = list(map(int, input('숫자 {}개를 입력하세요'.format(m)).split()))
    mv = min(data)
    result = max(mv,result)
print(result)

# 02
n, m = map(int, input("행과 열을 입력하세요.").split())
result = 0

for i in range(n):
    data = list(map(int, input('숫자 {}개를 입력하세요').split()))
    mv = 10001
    for a in data:
        mv = min(mv, a)
    result = max(result, mv)
print(result)