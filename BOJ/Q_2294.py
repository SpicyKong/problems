# https://www.acmicpc.net/problem/2294 문제 제목 : 동전 2 , 언어 : Python, 날짜 : 2019-12-20, 결과 : 실패
# https://www.acmicpc.net/problem/2294 문제 제목 : 동전 2 , 언어 : Python, 날짜 : 2019-12-21, 결과 : 성공
# 런타임에러가 어디서 나는걸까?
import sys
n, k = map(int, sys.stdin.readline().split())
list_a = sorted(set([int(sys.stdin.readline()) for _ in range(n)]))
list_dp = [0] * (k + 1)
count_index = 0
for i in range(list_a[0], k + 1):
    if i == list_a[count_index]:
        list_dp[i] = 1
        if n > count_index+1:
            count_index += 1
    else:
        min_list = []
        for j in list_a:
            if i-j>0 and list_dp[i - j]:
                min_list.append(list_dp[i - j])
        if min_list:
            list_dp[i] = 1 + min(min_list)

if list_dp[-1]:
    print(list_dp[-1])
else:
    print(-1)

#----------------------------------------------------------------------------
#
# 기존코드에서 문제점은 겹치는 숫자의 갯수를 n > count_index 여기에서 반영을 하지
# 않았었다. 우연히 테케 막 입력하다가 발견했다.
----------------------------------------------------------------------------#
import sys
n, k = map(int, sys.stdin.readline().split())
list_a = sorted(set([int(sys.stdin.readline()) for _ in range(n)]))
size_list_a = len(list_a)
list_dp = [0] * (k + 1)
count_index = 0
for i in range(list_a[0], k + 1):
    if i == list_a[count_index]:
        list_dp[i] = 1
        if size_list_a > count_index + 1:
            count_index += 1
    else:
        min_list = []
        for j in list_a:
            if k>=i-j>0 and list_dp[i - j]:
                min_list.append(list_dp[i - j])
        if min_list:
            list_dp[i] = 1 + min(min_list)

if list_dp[-1]:
    print(list_dp[-1])
else:
    print(-1)
