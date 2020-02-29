# 문제 제목 : 컬러볼 , 언어 : Python, 날짜 : 20190731, 결과 : 시간초과
# https://www.acmicpc.net/problem/10800 문제 제목 : 컬러볼 , 언어 : Python, 날짜 : 2020-02-29, 결과 : 실패

num = int(input())
list_color = []
list_input = []
list_seq = []
for a in range(num):
    input_data = input().split()   
    input_data[0] = int(input_data[0])
    input_data[1] = int(input_data[1])
    if not input_data[0] in list_color:
        list_color.append(input_data[0])
        list_input.append([])
    color_index = list_color.index(input_data[0])
    list_input[color_index].append(input_data[1])
    list_seq.append([color_index,len(list_input[color_index])-1])

for a in range(num):
    asum = 0
    list_color_find = [b for b in range(len(list_color)) if not b == list_seq[a][0]] 
    for c in list_color_find:
        asum += sum([d for d in list_input[c] if d < list_input[list_seq[a][0]][list_seq[a][1]]])
    print(asum)

#___________________________________________________________________________________________________________
# 밑은 다시 작성한 버전, 시간초과..

num = int(input())
#list_a = [input().split() for _ in range(num)]
list_a = []
list_b = [0 for _ in range(num)]
for a in range(num):
    input_ob = input().split()
    input_ob[0] = int(input_ob[0])
    input_ob[1] = int(input_ob[1])
    list_a.append(input_ob)
    for b in range(a+1):
        if not list_a[b][0] == input_ob[0]:
            if input_ob[1] > list_a[b][1]:
                list_b[a] += list_a[b][1]
            elif input_ob[1] < list_a[b][1]:
                list_b[b] += input_ob[1]
[print(c) for c in list_b]
