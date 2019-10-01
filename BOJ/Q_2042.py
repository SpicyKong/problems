# https://www.acmicpc.net/problem/2042 문제 제목 : 구간 합 구하기 , 언어 : Python, 날짜 : 2019-08-21, 결과 : 실패(트리 공부하기)
# https://www.acmicpc.net/problem/2042 문제 제목 : 구간 합 구하기 , 언어 : Python, 날짜 : 2019-10-01, 결과 : 성공
# 세그먼트 트리가 무엇인지는 알겠는데, 이를 코드로 활용하는게 어렵다..
# 당분간 세그먼트 트리 문제를 풀어 보도록 해야겠다.

import sys
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start + end)//2 + 1, end)
        return tree[node]
def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right :
        return tree[node]
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start + end)//2+1, end, left, right)
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if not start == end:
        update(node*2, start, (start + end)//2, index, diff)
        update(node*2 + 1, (start + end)//2 + 1, end, index, diff)
l = []
tree = [0] * 3000000
N, M, K = map(int, sys.stdin.readline().split())
for _ in range(N):
    l.append(int(input()))
init(1, 0, N-1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:# b번째 수를 c로 바꿔라
        update(1, 0, N-1, b-1, c-l[b-1])
        l[b-1] = c
    else:# b부터 c까지의 합을 구하여라
        print(subSum(1,0,N-1, b-1, c-1))
