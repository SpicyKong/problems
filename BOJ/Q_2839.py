# https://www.acmicpc.net/problem/2389 문제 제목 : 설탕 배달 , 언어 : Python, 날짜 : 20190804, 결과 : 성공

num = int(input())

a,b = divmod(num,3)
c,d = divmod(num,5)
#print(c,d)
if d==0:
    print(c)
elif d==1:#good
    print(c+1)
elif num>=12 and d==2:#good?
    print(int((num-12)/5)+4)
elif d==3:#good
    print(c+1)
elif d==4 and c>0:#good
    print(c+2)
    
else:
    print(-1)
