# https://www.acmicpc.net/problem/6986 문제 제목 : 절사평균 , 언어 : Python, 날짜 : 2019-08-07, 결과 : 실패

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    list_lesser, list_avr, list_greater=[], [], []
    key=arr[len(arr)//2]
    for num in arr:
        if num > key:
            list_greater.append(num)
        elif num < key:
            list_lesser.append(num)
        else:
            list_avr.append(num)
    return quick_sort(list_lesser) + list_avr + quick_sort(list_greater)

a,b = map(int, input().split())
list_a = [float(input()) for _ in range(a)]
list_a = quick_sort(list_a)
list_b = list_a[b:a-b]
sum_a = sum(list_b)+1e-9
num_ka = list_b[0]*b
num_kb = list_b[-1]*b
c = round(sum_a/(a-2*b),2)
d = round((sum_a+num_ka+num_kb)/a,2)
if len(str(c)) < 4:
    print(str(c)+'0'*(4-len(str(c))))
else:
    print(c)
if len(str(d)) < 4:
    print(str(d)+'0'*(4-len(str(d))))
else:
    print(d)
