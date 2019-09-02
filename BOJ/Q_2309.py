# https://www.acmicpc.net/problem/2309 문제 제목 : 일곱 난쟁이 , 언어 : Python, 날짜 : 2019-09-02, 결과 : 성공

import sys

list_a = [int(sys.stdin.readline()) for _ in range(9)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]

    lesser, aver, greater = [], [], []
    for a in arr:
        if a > pivot:
            greater.append(a)
        elif a < pivot:
            lesser.append(a)
        else:
            aver.append(a)

    return quick_sort(lesser) + aver + quick_sort(greater)

list_a = quick_sort(list_a)
obj = sum(list_a) - 100
count_a = 0
count_b = 0
asdf = True
while asdf:
    count_b=count_a+1
    while True:
        if list_a[count_a] + list_a[count_b] == obj:
            del list_a[count_b]
            del list_a[count_a]
            asdf =False
            break
        if count_b == 8:
            break
        count_b+=1
    if count_a == 7:
        break
    count_a+=1
[print(a) for a in list_a]
