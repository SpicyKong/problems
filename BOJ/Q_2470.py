# https://www.acmicpc.net/problem/2470 문제 제목 : 두 용액 , 언어 : Python, 날짜 : 2020-06-01, 결과 : 성공
"""
    회고:
    투 포인터 알고리즘을 이요해 해결하면 된다. 우선 나는 l과 r을 각각 0과 N-1로 설정했다. 그리고 각각의 포인터를
    이동시켜 최적값을 탐색해나가게 되는데, 어느 포인터를 움직일지 결정하는 부분은 두개의 포인터중 이동했을때 더욱
    값이 작아지는 쪽의 포인터를 이동시켰다. (현재값이랑 비교하는게 아니라 단순히 두개의 포인터를 각각 이동시켜보고 결정한다.)
    그리고 움직였을때의 값이 result에 저장된 값보다 작다면 업데이트를 해주면된다.

    오늘 스터디를 진행 도중 투 포인터 알고리즘을 사용하는 문제를 풀어보았는데, 회장님께서 이 문제를 추천해 주셨다.
    투 포인터라는 알고리즘을 자세히는 몰랐지만 여러번 비슷한 방식으로 풀어본 기억은 있었다. 아 그리고 오늘 스터디 진행 도중에
    콩이가 책장에서 내 얼굴로 떨어졌다. 그래서 피가 꽤 많이 났다..
    그리고 이제 백준외에 다른 알고리즘 문제를 푼 경우에는 내가 따로 기록을 하기로 했다.
"""

import sys
N = int(sys.stdin.readline())
list_liquid = list(map(int, sys.stdin.readline().split()))
list_liquid.sort()
l, r = 0, N-1
result = [2000000000, 0, 0] # min, l, r
while l<r:
    now = abs(list_liquid[l]+list_liquid[r])
    if result[0] > now:
        result=[now, l, r]
    if abs(list_liquid[l+1]+list_liquid[r]) < abs(list_liquid[l]+list_liquid[r-1]):
        l+=1
    else:
        r-=1
print(list_liquid[result[1]], list_liquid[result[2]])
