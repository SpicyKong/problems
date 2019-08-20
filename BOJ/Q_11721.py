# https://www.acmicpc.net/problem/11721 문제 제목 : 열 개씩 끊어 출력하기 , 언어 : Python, 날짜 : 2019-08-20, 결과 : 성공

str_word = input()
list_a = ''
for a in range(1,len(str_word)+1):
    list_a+=str_word[a-1]
    if a%10 == 0 or a == len(str_word):
        print(list_a)
        list_a = ''
