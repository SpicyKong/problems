# https://www.acmicpc.net/problem/1701 문제 제목 : Cubeditor , 언어 : Python, 날짜 : 2020-04-07, 결과 : 성공
"""
    회고:
    내가 생각한 방법은 간단하다. 문자열을 탐색해가면서 a면 a끼리 모아두고 b면 b끼리 모아두고를 반복해 알파벳 리스트를 만든다.
    이제 이 사실을 이용하면 된다. '같은 부분 문자열은 같은 알파벳으로 시작한다.'
    그러면 기존에 같은 알파벳들끼리 모아 인덱스를 저장해둔 리스트를 사용해 비교를 하면 된다.
    지금 회고를 작성하면서 생각해 보니 본코드에서처럼 문자열의 길이만큼 반복문을 할게 아니라
    그냥 알파벳 수만큼 반복문을 돌리면 된다.

    오늘 어제 기타를 열심히 연습한 탓인지 손목이 완전 나갔다..
    내일은 다른분들의 코드를 참고하며 풀어봐야겠다. 특히 이분탐색을 하거나 KMP알고리즘에 대해 찾아봐야겠다.
    이 문제에 이분 탐색을 어떻게 사용할지 감이 안잡힌다..
"""
import sys
input_string = sys.stdin.readline().strip()
dict_alpha = {chr(97+i):i for i in range(26)}
N=len(input_string)

list_alpha = [[] for _ in range(26)]
list_alpha_count = [0]*26
for i, alpha in enumerate(input_string):
    list_alpha[dict_alpha[alpha]].append(i)
    list_alpha_count[dict_alpha[alpha]]+=1
now_max = 0

for now_index in range(N-1):
    for i in range(list_alpha_count[dict_alpha[input_string[now_index]]]):
        for j in range(i+1, list_alpha_count[dict_alpha[input_string[now_index]]]):
            if list_alpha[dict_alpha[input_string[now_index]]][i] >= N-1 or list_alpha[dict_alpha[input_string[now_index]]][j] >= N-1:
                break
            can_max = N - list_alpha[dict_alpha[input_string[now_index]]][j]
            if can_max <= now_max:
                break
            count_index = 1
            while list_alpha[dict_alpha[input_string[now_index]]][j] + count_index < N and input_string[list_alpha[dict_alpha[input_string[now_index]]][i]+count_index] == input_string[list_alpha[dict_alpha[input_string[now_index]]][j]+count_index]:
                count_index+=1
            now_max = max(now_max, count_index)
    list_alpha_count[dict_alpha[input_string[now_index]]] = 0
    if now_max > N - now_index:
        break
print(now_max)
