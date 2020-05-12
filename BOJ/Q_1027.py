# https://www.acmicpc.net/problem/1027 문제 제목 : 고층 건물 , 언어 : Python, 날짜 : 2020-05-12, 결과 : 성공 
"""
    회고:
    어제 익힌 CCW알고리즘을 사용했다. 나는 이 문제의 입력을 모두 완전탐색을 해가면서 풀이를 진행했다.
    우선 시작 빌딩-중간빌딩-목표빌딩 이런식으로 생각했다. 그리고 문제에서 볼 수 있으려면 3개의 빌딩이 /이거나 ^이런 모양만 아니면된다.
    그래서 나는 목표 빌딩이 생기면 그 빌딩을 중간빌딩으로 업데이트하고 차근차근 진행해 나갔다. 빌딩의 반대편으로도 봐야하므로
    서로 다른 방향으로 두 번 탐색 해 주었다. N이 50이라 다행이다.

    미적 중간고사가 끝나면 본격적으로 공부를 해야 겠다.
"""
import sys
def canIsee(s, m, e, d):
    if ((m - s)*(list_num[e]-list_num[s]) - (list_num[m]-list_num[s])*(e-s))*d > 0:
        return True
    return False
def update(d):
    global list_result, N
    if d>0:
        sp = 0
        ep = N-1
    else:
        sp = N-1
        ep = 0

    for s in range(sp,ep,d):
        mid = s+d
        for e in range(mid+d, ep+d, d):
            if canIsee(s, mid, e, d):
                mid = e
                list_result[s] += 1
def solve():
    global N, list_num, list_result
    N = int(sys.stdin.readline())
    list_num = list(map(int, sys.stdin.readline().split()))
    if N==1:
        print(0)
        return
    result = 0
    list_result = [1 if (i==0 or i==N-1) else 2 for i in range(N)]#[]*N#[[0,0] for _ in range(N)]
    update(1)
    update(-1)


    print(max(list_result))
solve()
"""
0 1 2 3 4
0 1 2
0 1   3
0 1     4
  1 2 3
  1 2   4
    2 3 4
"""
