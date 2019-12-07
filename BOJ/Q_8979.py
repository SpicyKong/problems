# https://www.acmicpc.net/problem/8979 문제 제목 : 올림픽 , 언어 : Python, 날짜 : 2019-11-24, 결과 : 실패
# https://www.acmicpc.net/problem/8979 문제 제목 : 올림픽 , 언어 : Python, 날짜 : 2019-12-07, 결과 : 성공
# 정답코드는 아래에있다.

# ============================= code ver.1 (틀린코드) ===========================================
# 이 문제는 간단해 보여서 시도했는데 내일은 다른방법으로 풀어봐야겠다..
import sys

def quick_sort(arr, len_arr):
    #print(arr)
    if len_arr <= 0:
        return arr
    pivot = arr[len_arr//2][1]
    lesser, equal, larger = [], [], []
    count_lesser, count_larger = 0, 0
    for num in arr:
        if num[1] > pivot:
            larger.append(num)
            count_larger+=1
        elif num[1] < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)
    return quick_sort(larger, count_larger) + equal + quick_sort(lesser, count_lesser) 

N, K = map(int, sys.stdin.readline().split())
list_country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i,a in enumerate(list_country):
    list_country[i] = [a[0],a[1]*1000000**2 + a[2]*1000000 + a[3]]

#print(list_country)
"""
4 3
1 1 2 0
2 1 2 0
3 1 2 0
4 1 2 0
 0 0 1
2 0 1 0
3 4 1 0"""

list_country = quick_sort(list_country,N)
count_rank = 1
save_num = list_country[0][1]
for country in list_country:
    #print(country)
    if not country[0] == K:
        if not save_num == country[1]:
            count_rank += 1
    else:
        print(count_rank)
        break
    save_num = country[1]
    
# ============================= code ver.2 (정답코드) ===========================================
# 사실 이 문제는 게시판에서 정렬이 필요없다는 힌트를 듣고서야 정답코드가 떠올랐다..

import sys

N, K = map(int, sys.stdin.readline().split())
list_medal = [[] for  _ in range(N+1)]
for _ in range(N):
    nation, gold, silver, bronze = map(int, sys.stdin.readline().split())
    list_medal[nation] = [gold, silver, bronze]
goal_g, goal_s, goal_b = list_medal[K]

#print(list_medal[K])
count = 1
for i in range(1,N+1):
    if list_medal[i][0] > goal_g:
        count+=1
    elif list_medal[i][0] == goal_g:
        if list_medal[i][1] > goal_s:
            count+=1
        elif list_medal[i][1] == goal_s:
            if list_medal[i][2] > goal_b:
                count+=1
print(count)


