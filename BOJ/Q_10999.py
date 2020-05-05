# https://www.acmicpc.net/problem/10999 문제 제목 : 구간 합 구하기 2 , 언어 : Python, 날짜 : 2020-05-05, 결과 : 성공
"""
    회고:
    Lazy Propagation을 공부하고 풀어보았다. 솔직히 내가 제대로 한 건지는 잘 모르겠다.
    일단 내가 이해한 바로는 구간에 대한 업데이트가 주어졌을때 지금 하나하나 모두 업데이트를 하는것이 아니라 나중에 그 정보를 사용할때 업데이트를 하라고 이해했다.
    그리고 나중에 적용시킬 값들에 대한 내용을 저장하기위해 lazy라는 배열을 하나 더 만들어주는데, 이 lazy의 모양은 세그먼트 트리와 동일하다.
    그래서 만약 값을 조회하다가 lazy값이 0이아니면 갱신을 해 주는 방식이다.
    솔직히 말하면 아직 혼자서는 못짜겠다. 이 코드를 작성하는 것도 굉장히 오래걸렸다..ㅠㅠ
    그냥 열심히 해봐야겠다.

    오늘 오랜만에 크림파스타를 만들어 먹었는데 역대급으로 맛이 있었다. 저번에 만든 감바스보다 더 맛있었다.
"""
import sys
def segInit(start, end, node):
    global N
    if start >= N:
        return 0
    if start == end:
        list_tree[node] = list_num[start]
        return list_tree[node]
    mid = (start+end)//2
    list_tree[node] = segInit(start, mid, node*2) + segInit(mid+1, end, node*2+1)
    return list_tree[node]

def segUpdate(start, end, left, right, node, diff):
    lazyUpdate(start, end, node)
    
    if end < left or start > right:
        return
    if start == left and end == right:
        list_lazy[node] += diff
        return
    elif start <= left and end >= right:
        list_tree[node] += (right - left + 1)*diff
    mid = (start + end)//2
    right1 = min(right, mid)
    left1 = max(mid+1, left)
    if start <= left and right1 <= mid:
        segUpdate(start, mid, left, right1, node*2, diff)
    if mid+1 <= left1 and right <= end:
        segUpdate(mid+1, end, left1, right, node*2+1, diff)

def lazyUpdate(start, end, node):
    if not list_lazy[node]:
        return
    list_tree[node] += list_lazy[node] * (end - start + 1)
    if not start == end:
        list_lazy[node*2] += list_lazy[node]
        list_lazy[node*2+1] += list_lazy[node]
    list_lazy[node] = 0

def getSum(start, end, left, right, node):
    lazyUpdate(start, end, node)
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return list_tree[node] + list_lazy[node]*(end - start + 1)
    mid = (start + end)//2
    return getSum(start, mid, left, right, node*2) + getSum(mid+1, end, left, right, node*2+1)


#def segUpdate(start, end, left, right, node, diff):
#    if start == left and end == right:
#        list_lazy[node]+=diff

N, M, K = map(int, sys.stdin.readline().split())
list_num = [int(sys.stdin.readline()) for _ in range(N)]
list_tree = [0]*(N*4+1)
list_lazy = [0]*(N*4+1)
segInit(0, N-1, 1)
for _ in range(M + K):
    #print('---------------------------')
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        segUpdate(0, N-1, command[1]-1, command[2]-1, 1, command[3])
    else:
        print(getSum(0, N-1, command[1] -1, command[2]-1, 1))
    
    #print(list_lazy)
    #print(list_tree)
#while True:
#    a, b = map(int, sys.stdin.readline().split())
#    print(getSum(0, N-1, a, b, 1))
#    print(list_lazy)
#    print(list_tree)
