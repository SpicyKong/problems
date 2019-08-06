# https://www.acmicpc.net/problem/13458 문제 제목 : 시험 감독 , 언어 : Python, 날짜 : 2019-08-06, 결과 : 성공

n = int(input())
room_list = list(map(int, input().split()))
B,C = map(int,input().split())
room_list_n = []
for d in room_list:
    if d-B<=0:
        room_list_n.append(1)
    else:
        d-=B
        mod_a, mod_b = divmod(d,C)
        if mod_a==0:
            room_list_n.append(2)
        elif mod_b == 0:
            room_list_n.append(1+mod_a)
        else:
            room_list_n.append(1+mod_a+1)
print(sum(room_list_n))
