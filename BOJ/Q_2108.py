# https://www.acmicpc.net/problem/2108 문제 제목 : 통계학 , 언어 : Python, 날짜 : 2019-09-01, 결과 : 성공
#이 문제는 어이없게도 최빈값을 구하는 과정에서 많은 시행착오를 겪었다..


import sys
N = int(sys.stdin.readline())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    key = arr[len(arr)//2]
    lesser, aver, greater = [], [], []
    for a in arr:
        if a < key:
            lesser.append(a)
        elif a > key:
            greater.append(a)
        else:
            aver.append(a)
    return quick_sort(lesser) + aver + quick_sort(greater)
list_a = quick_sort(list_a)
count=1
count_max = 1
index_list = []
start_num=0
while True:
    if N == count:
        if count+1 - start_num > count_max:
            index_list = []
            index_list.append(start_num)
            count_max = count+1 - start_num
        elif count+1 - start_num == count_max:
            index_list.append(start_num)
        break
    elif not list_a[count]==list_a[start_num]:
        if count+1 - start_num > count_max:
            index_list = []
            index_list.append(start_num)
            count_max = count+1 - start_num
        elif count+1 - start_num == count_max:
            index_list.append(start_num)
        start_num = int(count)
    count+=1
print(round(sum(list_a)/N))
print(list_a[N//2])
if len(index_list) > 1:
    print(list_a[index_list[1]])
else:
    print(list_a[index_list[0]])
if N==1:
    print(0)
else:
    print(list_a[-1]-list_a[0])
