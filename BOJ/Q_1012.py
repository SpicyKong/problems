# https://www.acmicpc.net/problem/1012 문제 제목 : 유기농 배추 , 언어 : Python, 날짜 : 2019-08-25, 결과 : 실패

import sys

N = int(sys.stdin.readline())



for _ in range(N):
    M, N, K = map(int, sys.stdin.readline().split())
    list_bechu = []
    count = 0
    for a in range(K):
        bechu = list(map(int, sys.stdin.readline().split()))
        if [bechu[0] -1, bechu[1]] in list_bechu or [bechu[0] +1, bechu[1]] in list_bechu or [bechu[0], bechu[1] -1] in list_bechu or [bechu[0], bechu[1] +1] in list_bechu:
            list_bechu.append(bechu)
        else:
          list_bechu.append(bechu)
          count+=1
    print(list_bechu)
    print("N :",count)
    """
    
    import sys

N = int(sys.stdin.readline())



for _ in range(N):
    M, N, K = map(int, sys.stdin.readline().split())
    list_bechu = []
    count = 1
    for _ in range(K):
        list_bechu.append(list(map(int, sys.stdin.readline().split())))
    for bechu in list_bechu:
        if [bechu[0] -1, bechu[1]] in list_bechu or [bechu[0] +1, bechu[1]] in list_bechu or [bechu[0], bechu[1] -1] in list_bechu or [bechu[0], bechu[1] +1] in list_bechu:
            pass
        else:
            count+=1
    #print(list_bechu)
    print("N :",count)1
2 2 3
1 0
0 1
1 1
    푸는 중인데, 자소서쓰느냐고 일단 보류
    """
