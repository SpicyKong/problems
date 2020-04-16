# https://www.acmicpc.net/problem/14267 문제 제목 : 내리 갈굼 , 언어 : Python, 날짜 : 2020-04-16, 결과 : 성공
"""
    회고:
    가장 높은 직급인 사장의 인덱스가 정해져 있어서 그냥 사장부터 차례로 내려가면된다.

"""
import sys
n, m = map(int, sys.stdin.readline().split())
list_child = [[] for _ in range(n)]
index = 0
for boss in list(map(int, sys.stdin.readline().split())):
    if boss-1 >= 0:
        list_child[boss-1].append(index)
    index += 1
    
list_stress = [0]*n
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    list_stress[a-1] += b

list_stack = [0]
while list_stack:
    now_index = list_stack.pop()
    for next_index in list_child[now_index]:
        list_stress[next_index] +=list_stress[now_index]
        list_stack.append(next_index)
#print(list_child)
print(*list_stress)

