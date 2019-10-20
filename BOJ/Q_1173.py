# https://www.acmicpc.net/problem/1173 문제 제목 : 운동 , 언어 : Python, 날짜 : 2019-10-20, 결과 : 성공
# 첫번째 면접은 나쁘지않게 한것같다
# 우선 이 문제는 생각보다 시간이 오래걸렸다..
# 간단한 문제임에도 불구하고, 문제에 있는 조건인 'X-R이 m보다 작으면 맥박은 m이 된다.'를 보지 못하고
# 계속해서 삽질했따,..,


import sys

N, m, M, T, R = map(int,sys.stdin.readline().split())
# 운동 시간, 처음 맥박 , 최대 맥박 < M 
# 운동하면 T만큼 증가 , 쉬면 R만큼 감소

if M < T+m:
    print(-1)
else:
    exercise = 0
    now = m
    count = 0
    while not exercise == N:
        if now + T <= M:
            now+=T
            exercise+=1
        elif now - R >= m:
            now-=R
        else:
            now = m
        count+=1
        #print(now)
    print(count)
