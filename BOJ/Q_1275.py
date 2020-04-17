# https://www.acmicpc.net/problem/1275 문제 제목 : 커피숍2 , 언어 : Python, 날짜 : 2020-04-17, 결과 : 성공
"""
    회고:
    세그먼트 트리에 대해서 처음으로 공부를 해 본것 같다. 그동안 구간합에 대한 문제를 보고 관련 해설을 찾아보면 항상 언급되는 알고리즘? 자료구조? 인데
    그때는 일단 트리에 대한 거부감이 있었고, 그냥 세그먼트 트리가 너무 어려워 보여서 공부할 마음조차 먹지 않았던것 같다. 하지만 최근 코드포스를 풀어보고 가리면서 공부할 처지는 못된다는것을 깨닫게 되고
    모르는건 찾아보고 배우기로 마음먹었다.
    
    세그먼트 트리를 이해하면서 들었던 의문들 :
    1. 트리를 어떻게 초기화를 하는지?
        init 함수를 보면 알 수 있듯이 start, end, node 3개의 파라미터를 가지고 있다. 앞서 두개의 변수는 구간을 표현하고 마지막 node라는 변수는 배열에서 현재 노드의 인덱스를 표현한다.
        그리고 이 함수가 반복실행 되면서 start == end인 경우를 만나게 되면 기존에 가지고 있던 배열에서 start번째 혹은 end번째 값을 반환시켜주면 된다.
    2. 업데이트는 어떻게 이루어 지는지:
        나는 맨처음 만약 3번째 인덱스를 5로 바꾼다고 하면 트리의 하단부부터 최상단까지 거슬러 올라가며 업데이트를 할 줄 알았다.
        하지만 우리가 구간의 합을 구할 배열을 통해 diff값을 먼저 구한뒤 루트노드 부터 탐색해 나가며 만약 현재 노드의 구간범위가 업데이트 시킬 인덱스를
        포함하고 있는 경우에 diff를 더해준다.
    3. 합은 어떻게 구하는지:
        이 의문은 업데이트를 구현하는 과정에서 사라졌다.

"""

import sys

def init(start, end, node):
    global N
    #print(list_graph)#start, end, node)
    if start == end:
        if start < N:
            list_graph[node] = list_num[start]
        return list_graph[node]
    mid = (start + end)//2
    list_graph[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)#list_num[node*2] + list_num[node*2]
    return list_graph[node]

def update(start, end, node, diff, index):
    list_graph[node] += diff
    if start == end:
        return
    mid = (start + end)//2
    if start <= index <= mid:
        update(start, mid, node*2, diff, index)
    if mid+1 <= index <= end:
        update(mid+1, end, node*2+1, diff, index)
    
def getSum(start, end, left, right, node):
    if end < left or start > right:
        return 0
    if left <= start and end <= right:
        return list_graph[node]
    mid = (start + end)//2
    return getSum(start, mid, left, right, node*2) + getSum(mid+1, end, left, right, node*2+1)



N, Q = map(int, sys.stdin.readline().split())
list_num = list(map(int, sys.stdin.readline().split()))
save_N = N-1#int(sys.stdin.readline())
count = 0

while save_N:
    save_N>>=1
    count += 1

list_graph = [0]*(2**(count+1))
init(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x > y:
        swap = x
        x = y
        y = swap
    print(getSum(0, N-1, x-1, y-1, 1))
    update(0, N-1, 1, b - list_num[a-1], a-1)
    list_num[a-1] = b
