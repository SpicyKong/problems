# https://www.acmicpc.net/problem/1614 문제 제목 : 영식이의 손가락 , 언어 : Python, 날짜 : 2019-09-26, 결과 : 실패

finger_num = int(input())
max_num = int(input())
result = 0
if finger_num%4==1:
    if finger_num == 1: # 1일때
        result = (max_num)*8
    else: # 5일때
        result = (max_num)*8 + 4
else:
    result = max_num*4 # 짝이면 + 홀이면 -
    if (max_num)%2 == 0:
        result+=finger_num-1
    else:
        result+=3
        if finger_num==4:
            finger_num-=2
print(result)
"""
1234
5432
1234
5432
1234
5432

"""
