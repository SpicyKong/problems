# https://www.acmicpc.net/problem/1987 문제 제목 : 알파벳 , 언어 : Python, 날짜 : 2019-10-23, 결과 : 실패
# BFS만 풀다보니 DFS문제인데 자꾸 BFS로 짜진다..



import sys
R, C = map(int, sys.stdin.readline().split())
list_visit = [[0]*C for _ in range(R)]
list_map = [list(sys.stdin.readline()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
list_stack = [[0, 0]]
list_alphabet = [list_map[0][0]]
check_is_there = 0
max_num = 0
now_num = 0
while list_stack:
    x, y = list_stack[-1]
    list_alphabet.append(list_map[y][x])
    count_i = 0
    asdf = 0
    while not count_i == 3 and not asdf:
        ax = x + dx[count_i]
        ay = y + dy[count_i]
        if 0 <= ax < C and 0 <= ay < R:
            if list_visit[ay][ax] == 0 and not list_map[ay][ax] in list_alphabet:
                list_visit[ay][ax] = 1
                list_stack.append([ax, ay])
                asdf = True
                check_is_there = 1
                now_num +=1
        count_i += 1
    if max_num < now_num:
        max_num = now_num
    if not check_is_there:
        tx, ty = list_stack.pop()
        list_visit[ty][tx] = 0
        list_alphabet.pop()
        now_num -= 1
    else:
        check_is_there = 0
    print(list_stack)
    print("=====================")
print(max_num)
    


"""
while list_stack:
    x, y = list_stack.pop()
    list_alphabet.append(list_map[y][x])
    for i in range(2):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < C and 0 <= ay < R:
            if list_visit[ay][ax] == 0 and not list_map[ay][ax] in list_alphabet:
                list_visit[ay][ax] = 1
                list_stack.append([ax, ay])
    [print(a) for a in list_visit]
    print("=====================")
"""
