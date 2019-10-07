# https://www.acmicpc.net/problem/5014 문제 제목 : 스타트링크 , 언어 : Python, 날짜 : 2019-10-07, 결과 : 성공

from collections import deque
F, S, G, U, D = map(int, input().split())
list_visit = [0 for _ in range(F+1)]
end = False
list_button = [U, D*-1]
list_queue = deque()
list_queue.append(S)
count = 0
asdf = 0
count_stack = [1]
while list_queue:
    #print(list_queue)
    now_floor = list_queue.popleft()
    if count_stack[count] > 0:
        count_stack[count]-=1 
    if now_floor == G:
        asdf = 1
        break
    for i in range(2):
        imsi_floor =now_floor + list_button[i]
        if 1 <= imsi_floor <= F:
            if not list_visit[imsi_floor]:
                list_visit[imsi_floor] = 1
                list_queue.append(imsi_floor)
                try:
                    count_stack[count+1]+=1
                except:
                    count_stack.append(1)
    if count_stack[count] == 0:
        count += 1
if asdf:
    print(count)
else:
    print("use the stairs")
