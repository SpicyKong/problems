# https://www.acmicpc.net/problem/2193 문제 제목 : 이친수 , 언어 : Python, 날짜 : 2019-10-08, 결과 : 성공
# 아직 점화식 찾는 습관이 안배겨 있어 고생했다
N = int(input())
list_a = [0]*(N+1)
list_a[1] = 1
for i in range(2,N+1):
    list_a[i] = list_a[i-2] + list_a[i-1]
print(list_a[N])
