# https://www.acmicpc.net/problem/1350 문제 제목 : 진짜 공간 , 언어 : Python, 날짜 : 2020-01-06, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_files = list(map(int, sys.stdin.readline().split()))
size_of_cluster = int(sys.stdin.readline())
result = 0
for size_of_file in list_files:
    result += size_of_file//size_of_cluster
    if size_of_file%size_of_cluster > 0:
        result+=1
print(result*size_of_cluster)
