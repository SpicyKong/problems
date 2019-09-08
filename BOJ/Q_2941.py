# https://www.acmicpc.net/problem/2941 문제 제목 : 크로아티아 알파벳 , 언어 : Python, 날짜 : 2019-09-08, 결과 : 성공

import sys
str_a = sys.stdin.readline()[:-1]
asdf =True
count=0
num = 0
len_str = len(str_a)
#  asc-dz
#  012345 len = 6
while asdf:
    if num+1 < len_str:
        if str_a[num]=='c' and str_a[num+1] == '=' or str_a[num]=='c' and str_a[num+1] == '-':
            count+=1
            num+=1
        elif str_a[num]=='d' and str_a[num+1] == '-':
            count+=1
            num+=1
        elif str_a[num]=='l' and str_a[num+1] == 'j':
            count+=1
            num+=1
        elif str_a[num]=='n' and str_a[num+1] == 'j':
            count+=1
            num+=1
        elif str_a[num]=='s' and str_a[num+1] == '=':
            count+=1
            num+=1
        elif str_a[num]=='z' and str_a[num+1] == '=':
            count+=1
            num+=1
        elif len_str-num >=3 and str_a[num]=='d' and str_a[num+1] == 'z' and str_a[num+2] == '=':
            count+=1
            num+=2
        else:
            count+=1
        num+=1
    else:
        count+=1
        num+=1
    if num+1 > len_str:
        break
print(count)
