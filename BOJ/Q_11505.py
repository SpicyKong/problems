# https://www.acmicpc.net/problem/11505 문제 제목 : 구간 곱 구하기 , 언어 : Python, 날짜 : 2019-10-02, 결과 : 실패

import sys
from math import log2,ceil
def Segment(node, start, end):
    global list_a, tree
    if start == end:
        tree[node] = list_a[start]
        return tree[node]
    else:
        tree[node] = Segment(node*2, start, (start+end)//2) * Segment(node*2 + 1, (start + end)//2 + 1, end)
        return tree[node]

def Segment_multiply(node, start, end, left, right):
    global tree
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    return Segment_multiply(node*2, start, (start + end)//2, left, right) * Segment_multiply(node*2 + 1, (start + end)//2 + 1, end, left, right)

def Segment_update(node, start, end, index, diff):
    global tree
    if index < start or index > end:
        return
    if tree[node] == 0: # 탐색중인 노드가 이미 0 이였을 경우
        if tree[node*2] + tree[node*2+1] == -2: # 리프노드 인 경우
            tree[node] = diff # 해당노드를 입력받은 값으로 바꾸어 줍니다
        else:
            tree[node] = tree[node*2] * tree[node*2+1] # 해당 노드의 값을 구해주고 바꾸어 줍니다
        
        
    else:
        tree[node] *= diff
    if not start == end:
        Segment_update(node*2, start, (start + end)//2, index, diff)
        Segment_update(node*2 + 1, (start + end)//2 + 1, end, index, diff)


N, M, K = map(int, sys.stdin.readline().split())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
tree = [-1]*(1<<ceil(log2(N))+1)
Segment(1,0,N-1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        if list_a[b-1] == 0: # 0일경우 따로 처리
            d = c
        else:
            d = c/list_a[b-1]
        Segment_update(1, 0, N-1, b-1, d)
        list_a[b-1] = c
    else:
        print(int(Segment_multiply(1, 0, N-1, b-1, c-1))%1000000007)
"""
4%에서 런타임 오류가 뜬다..ㅂㄷㅂㄷ
"""
