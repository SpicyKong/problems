# https://www.acmicpc.net/problem/10835 문제 제목 : 카드게임 , 언어 : Python, 날짜 : 2020-02-17, 결과 : 성공
"""
  회고:
  맨 처음에는 그저 간단해 보였다. 경우에 따라 나누기만 하면 될줄알았는데 계속 런타임 에러가 떳다.
  곰곰히 생각해보다 어렴풋이 재귀함수 깊이를 조절할수있음이 기억났고 sys.setrecursionlimit(10**6)를 코드에 추가해 주었더니
  시간초과가 났다. 그래서 마지막 시도라는 생각으로 PYPY3로 제출을 했더니 맞았다!
  시간초과를 해결하기위해 한번 더 생각해봐야겠다.
"""
import sys
sys.setrecursionlimit(10**6)
def cardgame(index_Left, index_Right):
    global N, list_left, list_right, list_memo
    if index_Left >= N or index_Right >= N:
        return 0
    
    if not list_memo[index_Left][index_Right] == -1:
        return list_memo[index_Left][index_Right]
    #result = 0
    list_memo[index_Left][index_Right] = 0
    
    if list_left[index_Left] > list_right[index_Right]:
        list_memo[index_Left][index_Right] += max(cardgame(index_Left, index_Right+1) + list_right[index_Right], cardgame(index_Left+1, index_Right+1), cardgame(index_Left+1, index_Right))
    else:
        list_memo[index_Left][index_Right] += max(cardgame(index_Left+1, index_Right+1), cardgame(index_Left+1, index_Right))

    return list_memo[index_Left][index_Right]

N = int(sys.stdin.readline())
list_memo = [[-1]*(N+1) for _ in range(N+1)]
list_left = list(map(int, sys.stdin.readline().split()))
list_right = list(map(int, sys.stdin.readline().split()))
