from collections import deque
def solution(priorities, location):
    object_p = priorities[location]
    priorities = deque(priorities)
    check_list = [0]*10
    list_priority = []
    len_n = 0
    for num in priorities:
        if not check_list[num]:
            list_priority.append(num)
        check_list[num]+=1
        len_n+=1
    list_priority.sort()
    answer = 0

    while priorities:
        print('###################', location)
        print(check_list)
        print(priorities)
        print(list_priority)
        now_num = priorities.popleft()
        
        location-=1
        if now_num < list_priority[-1]:
            priorities.append(now_num)
            if location == -1:
                location = len_n-1
        else:
            check_list[now_num]-=1
            len_n-=1
            answer+=1
            if not check_list[now_num]:
                list_priority.pop()
            if location == -1:
                break
        


        
        
    return answer

list_a = [1,2,3,4,5,6,7]
index = 1
print(solution(list_a, index))
