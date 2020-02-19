# https://www.acmicpc.net/problem/1495 문제 제목 : 기타리스트 , 언어 : Python, 날짜 : 2020-02-19, 결과 : 실패
"""
  회고:
  약 3시간 가량동안 풀었는데 못풀었다. 이 문제는 실버1 문제인데 이렇게 허덕이는 걸 보면 공부를 정말 열심히 해야할것 같다.
  솔직히 말하자면 AC를 받은 몇몇 코드를 살펴 보았지만 이 문제에서 메모이제이션이 어떻게 작동하는지 잘 모르겠다.
  완전 기초 DP문제부터 공부해야겠다.
"""

import sys

def control(volume_now, volume_max, volumes, i):
    global N
    if i == N:
        return volume_now
    list_result = []
    token = 0
    if 0 <= volume_now + volumes[i] <= volume_max and 0 <= volume_now - volumes[i] <= volume_max:
        return max(control(volume_now+volumes[i],volume_max,volumes,i+1),control(volume_now-volumes[i],volume_max,volumes,i+1))
    elif 0 <= volume_now + volumes[i] <= volume_max:
        return control(volume_now+volumes[i],volume_max,volumes,i+1)
    elif 0 <= volume_now - volumes[i] <= volume_max:
        return control(volume_now-volumes[i],volume_max,volumes,i+1)
    else:
        return -1


N, S, M = map(int, sys.stdin.readline().split())
list_volume = list(map(int ,sys.stdin.readline().split()))
print(control(S, M, list_volume, 0))
