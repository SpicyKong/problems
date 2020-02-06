# https://www.acmicpc.net/problem/1759 문제 제목 : 암호 만들기 , 언어 : Python, 날짜 : 2020-02-06, 결과 : 성공
# 조합.. 개념은 정말 간단한데 머리로만 함수를 그려내니 생각보다 햇갈렸다..
# 그리고 드디어 이 문제를 풀면서 vscode에서 디버깅툴을 사용해보았다.
# 예전에는 자꾸만 오류가 떴는데 설정을 이리저리 건들다보니 갑자기 오류가 사라졌다.

import sys

def picker(elements, start, end, n, result):
    res = []
    if not n:
        for j in range(start, end):
            res.append(result + [elements[j]])
        return res
    else:
        for i in range(start, end):
            i
            res += picker(elements, 1 + i, end, n-1, result + [elements[i]])
    return res

L, C = map(int, sys.stdin.readline().split())
list_inputs = list(sys.stdin.readline().split())

list_aeiou = []
list_else = []
for alphabet in list_inputs:
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
        list_aeiou.append(alphabet)
    else:
        list_else.append(alphabet)
L -= 3
MAX_AEIOU = len(list_aeiou)
MAX_ELSE = len(list_else)




result = []
for count in range(L+1):
    if MAX_AEIOU >= count and MAX_ELSE >= L-count:
        save_aeiou = picker(list_aeiou, 0, MAX_AEIOU, count, [])
        save_else = picker(list_else, 0, MAX_ELSE, L - count + 1, [])
        
        for aeiou in save_aeiou:
            for el in save_else:
                result.append(''.join(sorted(aeiou+el)))
[print(a) for a in sorted(result)]
