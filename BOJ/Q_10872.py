# https://www.acmicpc.net/problem/10872 문제 제목 : 팩토리얼 , 언어 : Python, 날짜 : 2019-10-17, 결과 : 성공
#한번 리스트를 써보고 싶었다ㅋㅋ

a = [1]
num = int(input())
for i in range(1,num+1):
    a.append(a[i-1] * i)
print(a[-1])
