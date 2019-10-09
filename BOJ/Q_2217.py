# https://www.acmicpc.net/problem/2217 문제 제목 : 로프 , 언어 : Python, 날짜 : 2019-10-09, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
def sorting(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    lesser, ave, larger = [], [], []
    for i in arr:
        if i > pivot:
            larger.append(i)
        elif i < pivot:
            lesser.append(i)
        else:
            ave.append(i)
    return sorting(lesser) + ave + sorting(larger)
list_a = sorting(list_a)
weight = 0
best = 0
count = 1
for i in range(N):
    lope_w = list_a[-1-i]
    weight = lope_w*count
    count+=1
    if best < weight:
        best = weight
print(best)
