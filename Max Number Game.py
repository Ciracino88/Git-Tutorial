import time

n, m, k = map(int, input("공백 단위로 데이터를 입력하세요").split()) # 공백 단위로 데이터를 입력받는다.
data = list(map(int, input("공백 단위로 데이터를 입력하세요").split())) # 공백 단위로 데이터를 입력 받아 이를 리스트에 저장한다.

sttm = time.time()

data.sort() # 입력 받은 데이터 정렬
st = data[n-1] # 제일 큰 숫자
nd = data[n-2] # 두 번째로 큰 숫자

result = 0 # 결과값 초기화
while True: # 반복문 시작
    for i in range(k): # k번만큼 반복 실행
        if m == 0: # 더하는 횟수 m이 0이 되면
            break # 종료
        result += st # 결과값에 제일 큰 값을 더해 갱신
        m = m-1 # 더하는 횟수 1 감소
    if m == 0:
        break
    result += nd # 결과값에 두 번째로 큰 값을 더해 갱신
    m -= 1
print(result) # 결과값 출력

edtm = time.time()
print("time:", edtm-sttm)
