# https://www.acmicpc.net/problem/9020 문제 제목 : 골드바흐의 추측 , 언어 : Python, 날짜 : 2019-12-30, 결과 : 성공

import sys
T = int(sys.stdin.readline())
list_sosu = [0]*2 + [1]*(10001-2)
for i in range(2,10000 + 1):
    n = 2
    while i * n <= 10000:
        if list_sosu[i * n]:
            list_sosu[i * n] = 0
        n += 1
list_sosu = [i for i in range(10000 + 1) if list_sosu[i]]

def find(N_input):
    global list_sosu
    list_pair = []
    list_gap  = []
    for i in list_sosu:
        for j in list_sosu:
            if i + j > N_input:
                break
            if i + j == N_input:
                list_pair.append([i,j])
                list_gap.append(abs(j-i))
    min_num = 10001
    save_index = 0
    for i, num in enumerate(list_gap):
        if num < min_num:
            min_num = num
            save_index = i
    return list_pair[save_index]

for _ in range(T):
    N = int(sys.stdin.readline())
    num1, num2 = find(N)
    print(num1, num2)
