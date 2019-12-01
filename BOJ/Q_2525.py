# https://www.acmicpc.net/problem/2525 문제 제목 : 오븐 시계 , 언어 : Python, 날짜 : 2019-12-01, 결과 : 성공
# 최근 어떤 글을 읽었는데, 먼저 정올 초등부 기출을 풀어보는것도 좋다고한다.
# 이제부터 그 핑계로 초등부 문제들을 도전해봐야 겠다.

import sys

now_h, now_m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline()) + now_m + now_h*60

print((time//60)%24, time%60)
