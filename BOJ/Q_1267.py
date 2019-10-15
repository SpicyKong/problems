# https://www.acmicpc.net/problem/1267 문제 제목 : 핸드폰 요금 , 언어 : Python, 날짜 : 2019-10-15, 결과 : 성공

import sys

N = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
#sum_a = sum(list_a)
Y_fee = 0
M_fee = 0
for fee in list_a:
    Y_fee += (fee//30+1)*10
    M_fee += (fee//60+1)*15
if M_fee == Y_fee:
    print("Y","M",M_fee)
elif M_fee > Y_fee:
    print("Y", Y_fee)
else:
    print("M",M_fee)
