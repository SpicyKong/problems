# https://www.acmicpc.net/problem/15803 문제 제목 : PLAYERJINAH’S BOTTLEGROUNDS , 언어 : Python, 날짜 : 2019-10-06, 결과 : 성공

list_state = [list(map(int, input().split())) for _ in range(3)]
c = 0
if list_state[0][0]-list_state[1][0]==0:
    if list_state[0][0] == list_state[2][0]:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
else:
    a = (list_state[0][1]-list_state[1][1])/(list_state[0][0]-list_state[1][0])
    b = list_state[0][1]-a*list_state[0][0]
    if a*list_state[2][0] + b == list_state[2][1]:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
