# https://www.acmicpc.net/problem/2631 문제 제목 : 줄세우기 , 언어 : Python, 날짜 : 2020-04-24, 결과 : 성공 
"""
    회고:
    LIS의 길이를 구하는 O(Nlog(2,N))의 방법중 이분탐색이 아닌 세그먼트 트리로 구현이 가능하다는것을 알게되어서 한번 공부할겸 구현해 보았다.
    먼저 트리의 모든 값을 0으로 초기화 시키고, 우리가 구할 수열을 [num, i]순으로 정렬 시킨다. 그리고 앞에서부터 차례대로 
    [0, i]까지의 최대값을 업데이트 시켜주면 된다. 이때 최대값이 LIS의 길이다. 뭔가 말로 설명하기 어려우니깐 아이패드에 정리해봐야겠다.

    오늘새벽에 코포 637.div2 가 있었다. 드디어 div2에서 2솔을 하기는 했는데 먼저 A번에서 실수를해서 오답을 여러번 제출했고 B번은 지문이 어려워서
    이해하는데에 시간을 많이 쏟았다. 결과적으로 모두 푸니 한시간이 조금 넘게 흘러있었다. 그래서 대략 1시간20분 정도의 시간이 남아있었지만 다른 문제를 풀지는 못하였다.
    계속 덤벼보기는 했는데 에디토리얼을 자세히 보지는 않았지만 접근방법이 완전히 잘못되었었다.. 아쉽다..
"""

import sys
import math
def get_max(start, end, left, right, node):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return list_graph[node]
    mid = (start + end)//2
    return max(get_max(start, mid, left, right, node*2), get_max(mid+1, end, left, right, node*2+1))

def update(start, end, diff, index, node):
    if start == end:
        list_graph[node] = max(diff, list_graph[node])

        return
    if start <= index <= end:
        list_graph[node] = max(diff, list_graph[node])
    mid = (start + end)//2
    if start <= index <= mid:
        update(start, mid, diff, index, node*2)
    if mid+1 <= index < end:
        update(mid+1, end, diff, index, node*2+1)

    
N = int(sys.stdin.readline())
list_num = [[int(sys.stdin.readline()), i] for i in range(N)]
list_num.sort()
list_graph = [0]*(N*4+1)#(2**(int(math.log2(N))+1)*2+1)
now_max = 0
for num in list_num:
    num_v, num_i = num
    save = get_max(0,N-1, 0, num_i, 1)
    update(0, N-1, save+1, num_i, 1)
print(N-list_graph[1])
