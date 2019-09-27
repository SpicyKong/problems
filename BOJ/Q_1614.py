# https://www.acmicpc.net/problem/1614 문제 제목 : 영식이의 손가락 , 언어 : Python, 날짜 : 2019-09-26, 결과 : 실패
# https://www.acmicpc.net/problem/1614 문제 제목 : 영식이의 손가락 , 언어 : Python, 날짜 : 2019-09-27, 결과 : 성공

finger_num = int(input())
count_max = int(input())
if finger_num == 1:
    result = 8*count_max
elif finger_num == 5:
    result = 4+8*count_max
else:
    if count_max%2==0:
        result = 4*count_max + finger_num - 1
    else:
        result = 4*count_max + 5-finger_num
print(result)
