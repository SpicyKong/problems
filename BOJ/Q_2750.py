# https://www.acmicpc.net/problem/2750 문제 제목 : 수 정렬하기 , 언어 : Python, 날짜 : 2019-08-05, 결과 : 성공

num = int(input())
list_a = []
list_a.append(int(input()))
avr = list_a[0]
for i in range(num-1):
    n = int(input())
    if avr/(i+1) < n:
        for a in reversed(range(i+1)):
            if list_a[a] < n:
                list_a.insert(a+1,n)
                break
    else:
        for a in range(i+1):
            if list_a[a] > n:
                list_a.insert(a,n)
                break
    avr+=n
[print(a) for a in list_a]
