# https://www.acmicpc.net/problem/2606 문제 제목 : 바이러스 , 언어 : Python, 날짜 : 2019-09-10, 결과 : 실패(메모리 초과)
# https://www.acmicpc.net/problem/2606 문제 제목 : 바이러스 , 언어 : Python, 날짜 : 2019-11-09, 결과 : 성공

# 실패 코드(정답코드는 이 코드 밑에 코드입니다.)
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_network = [list(map(int, sys.stdin.readline().split()))] # 처음받은 입력은 그냥 넣어줍니다.
for _ in range(M-1):
    input_a, input_b = map(int, sys.stdin.readline().split())
    for n,a in enumerate(list_network):
        is_there_a = input_a in a\
        is_there_b = input_b in a
        if is_there_a and not is_there_b: # 현재 네트워크에 첫번째 입력은 있고 두번째 입력은 없다면 
            list_network[n].append(input_b)# 두번째 입력을 현재 네트워크에 추가해 줍니다
        elif not is_there_a and is_there_b:
            list_network[n].append(input_a)
        elif not is_there_a and not is_there_b:# 둘다 없다면 새로운 네트워크를 구성합니다.
            list_network.append([input_a,input_b])
for a in list_network: # 1번이 있는 네트워크를 찾고 감염된 PC수를 구합니다.
    if 1 in a:
        print(len(a)-1)
        break
        

# 정답 코드
# 이 문제는 DFS와 BFS문제를 풀때 배웠던 그래프를 표현하는 방법인 인접리스트로 구현했다.
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

list_network = [[] for _ in range(N+1)]
list_visit = [0]*(N+1)
list_visit[1] = 1
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    list_network[a].append(b)
    list_network[b].append(a)
result = 0
def find_virus(num):
    global result,list_network, list_visit
    for i in list_network[num]:
        if not list_visit[i]:
            result+=1
            list_visit[i] = 1
            find_virus(i)
find_virus(1)
print(result)
