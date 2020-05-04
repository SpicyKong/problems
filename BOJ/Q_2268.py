# https://www.acmicpc.net/problem/2268 문제 제목 : 수들의 합 , 언어 : Python, 날짜 : 2020-05-04, 결과 : 성공
"""
    회고:
    사실 이 문제는 Lazy Propagation을 적용시켜 푸는 문제인것 같은데 pypy로 제출하니깐 맞았다.
    첫 실수는 i와 j가 당연히 i<j인줄 알아서 틀렸고, 두번째 실수는 오타였다. max(i+j)+1이라고 적었다. -1을 해야했는데.
    세그먼트 트리를 복습할 겸 풀어보았다. 아이패드에 다시 정리해봐야 겠다.
"""
import sys

def get_sum(start, end, left, right, node):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return list_tree[node]
    mid = (start + end)//2
    return get_sum(start, mid, left, right, node*2) + get_sum(mid+1, end, left, right, node*2+1)

def update(start, end, index, node, diff):
    list_tree[node] += diff
    if start == end:
        return
    mid = (start + end)//2
    if start <= index <= mid:
        update(start, mid, index, node*2, diff)
    if mid+1 <= index <= end:
        update(mid+1, end, index, node*2+1, diff)


N, M = map(int, sys.stdin.readline().split())
list_num = [0]*N
list_tree = [0]*(N*4+1)
for _ in range(M):
    a, i, j = map(int, sys.stdin.readline().split())
    if a:
        update(0, N-1, i-1, 1, j-list_num[i-1])
        list_num[i-1] = j
    else:
        print(get_sum(0, N-1, min(i,j)-1, max(i,j)-1, 1))
