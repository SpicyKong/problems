# https://www.acmicpc.net/problem/1107 문제 제목 : 리모컨 , 언어 : Python, 날짜 : 2019-12-05, 결과 : 실패
# ㄴ아ㅣ롼ㄹ오ㅓㅏㅣㄴㅇ로ㅓㅏㅣ넝라ㅣㅓㄴㅇ라ㅣㅓㄴㅇ리ㅏㅏㅣㄴㄹ어ㅏㅣㄴㅇ러ㅏㄴㄹ어ㅣㅏ
# 난 웰케 코딩을 못하는건지

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_broken = sys.stdin.readline().split()
result = 1000000
now = 100
for i in range(500000):
    #save = abs(abs(i - 100) - N)
    b = 0
    for num in str(i):
        if num in list_broken:
            b = 1
            break
    if not b:
        re =  abs(i - N) + len(str(i))
    else:
        re = abs(100 - i)
    if re < result:
        result = re
#print(re)
    
print(result)
"""

100 105
1 2 3 4 5

95 100
6 7 8 9 10
"""
