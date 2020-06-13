# https://www.acmicpc.net/problem/2002 문제 제목 : 추월 , 언어 : Python, 날짜 : 2020-06-13, 결과 : 성공
"""
    회고:
    처음에는 어떻게 풀지 고민하다가 원래 내 순서보다 빨리 터널에서 나왔을떄를 생각했는데,
    그렇게 하면 (1, 2, 3) > (3, 2, 1) 인 케이스만 보더라도 이상한 답이 나오게 된다.
    그래서 고민을 하다가 뒤에서부터 살펴보게 되었다. 이 아이디어는 저번에 학교 알고리즘 스터디시간에 다룬
    누적합을 구하는 방법에서 생각났다. 그래서 뒤 부터 탐색하며 가장 빨리 나와야 할 차를 저장하고
    이보다 빨리 나온 차를 모두 카운트를 해 주었다.

    옛날에는 코포를 한 날도 따로 백준을 풀었는데 요즘에는 안하게 된다. 뭔가 많이 나태해졌다.
    그래서 오늘 부터 롤을 삭제하고 게임을 잠시 멀리하기로 했다.(게임으로 스트레스만 풀면 좋을텐데 자꾸 할 일을 미룬다..)
"""

import sys
N = int(sys.stdin.readline())
dict_car = {sys.stdin.readline().strip():i for i in range(N)}
result = 0
list_car = [sys.stdin.readline().strip() for _ in range(N)]
now_min = N
count = 0
for i in range(N-1,-1,-1):
    if now_min < dict_car[list_car[i]]:
        count += 1
    else:
        now_min = dict_car[list_car[i]]

print(count)
