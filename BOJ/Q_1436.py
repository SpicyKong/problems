# https://www.acmicpc.net/problem/1436 문제 제목 : 영화감독 숌 , 언어 : Python, 날짜 : 2019-09-04, 결과 : 성공
# 이 문제는 만약에 시간제한이 촉박했다면 틀렸을거 같다. 다른 분들 코드를 보면서 공부해야겠다.


import sys
N = int(sys.stdin.readline())
a=666
count = 0
while True:
    if '666' in str(a):
        count+=1
    if count==N:
        print(a)
        break
    a+=1
    
