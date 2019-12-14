# https://www.acmicpc.net/problem/2096 문제 제목 : 내려가기 , 언어 : Python, 날짜 : 2019-12-14, 결과 : 실패
# 1차시도는 메모리 초과다..
# 다시 한번 짜봐야겠다.

import sys
N = int(sys.stdin.readline())
list_window = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_dp_max = [[0,0,0] for _ in range(N)]
list_dp_min = [[0,0,0] for _ in range(N)]
list_dp_max[0] = list_window[0]
list_dp_min[0] = list_window[0]
for i in range(1,N):
    for j in range(3):
        #list_dp_max[j] = maxlist_dp_max[]
        if j == 0:
            list_dp_max[i][j] = max(list_dp_max[i-1][j], list_dp_max[i-1][j+1]) + list_window[i][j]
            list_dp_min[i][j] = min(list_dp_min[i-1][j], list_dp_min[i-1][j+1]) + list_window[i][j]
        elif j == 1:
            list_dp_max[i][j] = max(list_dp_max[i-1][j], list_dp_max[i-1][j-1], list_dp_max[i-1][j+1]) + list_window[i][j]
            list_dp_min[i][j] = min(list_dp_min[i-1][j], list_dp_min[i-1][j-1], list_dp_min[i-1][j+1]) + list_window[i][j]
        else:
            list_dp_max[i][j] = max(list_dp_max[i-1][j], list_dp_max[i-1][j-1]) + list_window[i][j]
            list_dp_min[i][j] = min(list_dp_min[i-1][j], list_dp_min[i-1][j-1]) + list_window[i][j]
print(max(list_dp_max[-1]), min(list_dp_min[-1]))
