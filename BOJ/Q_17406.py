# https://www.acmicpc.net/problem/17406 문제 제목 : 배열 돌리기 4 , 언어 : Python, 날짜 : 2020-03-11, 결과 : 성공
"""
    회고:
    permutations함수의 존재를 알게 되었다. 간혹 문제를 풀다가 순열, 조합을 구현해야하지만
    생각보다 구현이 까다로워 문제풀기를 포기했던적이 몇번 있다. 이제부터라도 이 함수를 적극 이용해야겠다.
    아 그리고 이 문제는 주어진 명령대로 배열을 돌리는것이 아니라 주어진 명령의 순서를 적절히 조절해 최소값을 찾아야하는 문제이다.
    P.S.
    이제부터 커밋 몰아서 안할거다
    어제도 몰아서 하려다가 까먹고 잔디밭에 빵꾸냈다ㅠㅠ
"""
import sys
from itertools import permutations
def spin(command): #c,s
    r, c, s = command[0]-1, command[1]-1, command[2]
    global imsi_map
    for i in range(1,s+1):
        save = imsi_map[r-i][c-i]
        length = 2*i
        for j in range(length):
            imsi_map[r-i+j][c-i] = imsi_map[r-i+j+1][c-i]
        for j in range(length):
            imsi_map[r+i][c-i+j] = imsi_map[r+i][c-i+j+1]
        for j in range(length):
            imsi_map[r+i-j][c+i] = imsi_map[r+i-j-1][c+i]
        for j in range(length):
            if j == length-1:
                imsi_map[r-i][c+i-j] = save
            else:    
                imsi_map[r-i][c+i-j] = imsi_map[r-i][c+i-j-1]
N, M, K = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_command = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
list_commands = list(permutations(list_command))
result = 50*50*100 + 1
for commands in list_commands:
    imsi_map = [list_a[:] for list_a in list_map]
    for command in commands:
        spin(command)
    for list_a in imsi_map:
        sum_a = sum(list_a)
        if result > sum_a:
            result = sum_a
print(result)
