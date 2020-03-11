# https://www.acmicpc.net/problem/14503 문제 제목 : 로봇 청소기 , 언어 : Python, 날짜 : 2020-03-10, 결과 : 성공
"""
    회고:
    이 문제는 그냥 메뉴얼대로 구현하면 되는 문제라 어렵게 생각하진 않았다.
    다만 문제의 설명에서 '왼쪽 방향' 이라는 말이 왼쪽칸을 말하는건지, 왼쪽으로 벽이 나올때까지
    탐색을 해야하는건지 햇갈렸지만 풀다보니 전자라는것을 알수있었다.
    문제는 문제에서 초기에 주어지는 로봇의 위치인 (r,c)였다. 이번에도 문제를 제대로 잘못읽어서
    r,c를 우리가 아는 좌표평면인 x,y에 대입해 풀어서 계속 잘못된 값이 나왔다.
    문제의 설명에서는 r이 북쪽으로 부터 떨어진 칸의 개수라고 정확히 명시되어 있었는데 말이다.
    이 문제에 시간을 많이쓴게 아쉽다..
"""
import sys

def check_left_side():
    global list_map, robot, dx, dy
    imsi_d = (robot[2]-1)%4
    test = list_map[robot[1]+dy[imsi_d]][robot[0]+dx[imsi_d]]
    if test:
        return False
    else:
        return True

N, M = map(int,sys.stdin.readline().split())
robot = list(map(int, sys.stdin.readline().split()))
swap = robot[0]
robot[0] = robot[1]
robot[1] = swap
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

end = False
clean_token = 1
result=0
leftside_count = 0

while not end:
    
    if clean_token:
        list_map[robot[1]][robot[0]]=2
        clean_token=False
        result+=1
    if check_left_side():
        robot[2]-=1
        robot[2]%=4
        robot[0]+=dx[robot[2]]
        robot[1]+=dy[robot[2]]
        clean_token=True
        leftside_count = 0
    else:
        robot[2]-=1
        robot[2]%=4
        leftside_count+=1
        if leftside_count >= 4:
            if list_map[robot[1]-dy[robot[2]]][robot[0]-dx[robot[2]]]==1:
                end = True
            else:
                robot[1]-=dy[robot[2]]
                robot[0]-=dx[robot[2]]
            leftside_count = 0

print(result)
