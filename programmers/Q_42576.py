def solution(participant, completion):
    dict_completion = {}
    while completion:
        name = completion.pop()
        try:
            dict_completion[name]+=1
        except:
            dict_completion[name]=1
    for name in participant:
        try:
            dict_completion[name]-=1
            if dict_completion[name] < 0:
                answer = name
                break
        except:
            answer = name
            break
    return answer
