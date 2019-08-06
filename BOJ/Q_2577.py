# https://www.acmicpc.net/problem/2577 문제 제목 : 숫자의 개수 , 언어 : Python, 날짜 : 2019-08-06, 결과 : 성공

a=int(input())
b=int(input())
c=int(input())
d=str(a*b*c)
print_list = [0,0,0,0,0,0,0,0,0,0]
for f in range(10):
    for e in d:
        if e==str(f):
            print_list[f]+=1
[print(h) for h in print_list]
