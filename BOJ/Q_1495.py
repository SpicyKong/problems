# https://www.acmicpc.net/problem/1495 문제 제목 : 기타리스트 , 언어 : Python, 날짜 : 2020-02-19, 결과 : 실패
# https://www.acmicpc.net/problem/1495 문제 제목 : 기타리스트 , 언어 : Python, 날짜 : 2020-02-20, 결과 : 성공
"""
  회고:
  약 3시간 가량동안 풀었는데 못풀었다. 이 문제는 실버1 문제인데 이렇게 허덕이는 걸 보면 공부를 정말 열심히 해야할것 같다.
  솔직히 말하자면 AC를 받은 몇몇 코드를 살펴 보았지만 이 문제에서 메모이제이션이 어떻게 작동하는지 잘 모르겠다.
  완전 기초 DP문제부터 공부해야겠다.
  
  AC를 받은 후의 의문점은 두개의 코드의 내용이 별반 다른게 없어보이는데다 심지어 여기에 게시된 코드말고도 오늘 푼 방법과
  동일한 아이디어로 접근한 코드가 어제는 틀렸었다.. 아마도 다른 부분이 있었나 본데 그렇다면 내 구현력에 문제가 있었던거니
  프로그래밍에 좀더 자주 노출되어야 겠다.

"""
##### 성공코드.1
import sys

N, S, M = map(int, sys.stdin.readline().split())
list_volume = list(map(int ,sys.stdin.readline().split()))
list_dp = [[0]*(M+1) for _ in range(N+1)]
list_dp[0][S] = 1
#[print(a) for a in list_dp]
#print("============")
for i in range(1,N+1):
    for j in range(M+1):
        if list_dp[i-1][j]:
            if 0 <= j + list_volume[i-1] <= M:
                list_dp[i][j + list_volume[i-1]] = 1
            if 0 <= j - list_volume[i-1] <= M:
                list_dp[i][j - list_volume[i-1]] = 1
#[print(a) for a in list_dp]
token = 0
for i in range(M+1):
    if list_dp[-1][-1-i]:
        token = 1
        print(M - i)
        break
if not token:
    print(-1)

    
########## 실패코드.1
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
