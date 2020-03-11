def solution(clothes):
    answer = 1

    dict_clothes = {}
    dict_count = {}
    list_names = []
    count_c = 0

    for something in clothes:
        try:
            dict_clothes[something[1]].append(something[0])
            dict_count[something[1]]+=1
        except:
            dict_clothes[something[1]]=[something[0]]
            dict_count[something[1]]=1
            list_names.append(something[1])
    for name in list_names:
        answer*=(dict_count[name]+1)
    return answer

"""
각 파츠를 입나 안입나.
입는다면 각각의 종류의 개수만큼 곱해줌
안입는다면 그냥 1 곱해줌
5 + 3 +3 + 3 +1
a,d,e
b
c
"""
