# https://www.acmicpc.net/problem/6581 문제 제목 : HTML , 언어 : Python, 날짜 : 2020-02-01, 결과 : 성공

import sys
input_code = sys.stdin.read()
check=1
count = 0
for word in input_code.split():
    if word == '<br>':
        print()
        count = 0
    elif word == '<hr>':
        if count:
            print()
        print('-'*80)
        count = 0
    else:
        if not count:
            print(word, end='')
            count += len(word)
        else:
            if count + len(word) + 1 < 80:
                print(' ',end='')
                print(word, end='')
                count += len(word) + 1
            elif count + len(word) + 1 == 80:
                print(' ',end='')
                print(word, end='')
                print()
                count = 0
            else:
                count = 0
                print()
                print(word, end='')
                count += len(word)

        
        
#print(input_code.split())
