# 01
n = int(input('숫자를 입력하세요.'))
k = int(input("숫자를 입력하세요"))
count = 0

while True:
    if n == 1:
        break

    elif n%k == 0:
        n = n/k
        count +=1

    else:
        n -= 1
        count += 1

print(count)

# 02
n, k = map(int, input("숫자를 입력하세요").split())
count = 0

while n >= k:
    while n%k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1

    while n> 1:
        n -= 1
        count += 1

print(count)