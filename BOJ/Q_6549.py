# https://www.acmicpc.net/problem/6549 문제 제목 : 히스토그램에서 가장 큰 직사각형 , 언어 : Python, 날짜 : 2020-04-23, 결과 : 실패
"""
    회고:
    맨 처음 세그먼트 트리로만 간단히 풀릴거 같아서 풀어봤는데 생각보다 생각할게 많았다. 그래서 고민을하다 도저히 못풀겠어서 해설을 참고했다.
    분할 정복을 하는 방법이였는데 최솟값을 기준으로 왼쪽과 오른쪽을 나누고 또 그 범위에서 최솟값을 기준으로 왼쪽 오른쪽을 나누고.. 한마디로 재귀를 돌려준다.
    그리고 이렇게 하기 위해서 세그먼트 트리에는 높이가 아닌 최소값의 인덱스를 넣어준다. 굉장히 참신한 방법인것 같다.
    하지만 풀지못하였다.. 자꾸만 메모리 초과가 뜬다. 얼핏 해설을 보니 스택으로도 푸는 방법이 있다는데 더 고민을 해봐야겠다.
"""

import sys
import math
sys.setrecursionlimit(10**6)

def init(start, end, node):
    global list_segment, list_graph
    if start == end:
        list_segment[node] = start
        return list_segment[node]
    mid = (start + end)//2
    list_segment[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1), key = lambda x:list_graph[x])
    return list_segment[node]

def get_size(start, end, left, right, node):
    global list_segment
    if start > right or end < left:
        return -1
    if start >= left and end <= right:
        return list_segment[node]
    mid = (start + end)//2
    return min(get_size(start, mid, left, right, node*2), get_size(mid+1, end, left, right, node*2+1), key=lambda x:list_graph[x])
    

def get_max(start, end):
    global list_graph
    save_index = get_size(1, list_graph[0], start, end, 1)
    now_size = list_graph[save_index] * (end - start + 1)
    if start <= save_index-1:
        now_size = max(now_size, get_max(start, save_index-1))
    if end >= save_index+1:
        now_size = max(now_size, get_max(save_index+1, end))
    
    return now_size


while True:
    list_graph = list(map(int, sys.stdin.readline().split()))
    if list_graph[0] == 0:
        break
    list_graph.append(1000000000)
    list_segment = [0]*(2**(int(math.log2(list_graph[0]))+1)*2+1)
    init(1, list_graph[0], 1)
    print(get_max(1, list_graph[0]))
