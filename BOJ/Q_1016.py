# https://www.acmicpc.net/problem/1016 문제 제목 : 제곱 ㄴㄴ 수 , 언어 : Python, 날짜 : 2020-02-02, 결과 : 성공
# 포문 돌릴때 범위 잘못 정해서 삽질했다.
# 심지어 반례 찾을때도 다른분의 코드로 돌려보면서 찾아보았는데
# 알고보니 그분의 블로그에 게시된 코드도 틀린것이여서 계속 삽질했다ㅋㅋ

import sys

#while(1):
num_min, num_max = map(int, sys.stdin.readline().split())
list_test = [0]*(num_max - num_min + 2)
result = 0
for i in range(2,int(num_max**0.5)+1):
    i_square = i*i
    count = num_min//i_square
    while count * i_square <= num_max:
        
        if num_min <= count * i_square <= num_max and not list_test[count * i_square - num_min]:
            list_test[count * i_square - num_min] = 1
            result += 1
        count+=1
print(num_max - num_min + 1 - result)
