# https://www.acmicpc.net/problem/2733 문제 제목 : Brainf*ck , 언어 : Python, 날짜 : 2020-03-16, 결과 : 성공
"""
    회고:
    정말 난해한 문제다ㅋㅋ 맨 처음에는 입력을 받자마자 바로 처리해주었는데 생각해보니 그렇게되면 반복문 구현이 굉장히 까다로워지는것 같았다.
    그래서 맘 편하게 입력을 쫘라락 전처리해주고 시작을 했더니 맞았다. 그나저나 문제를 풀다보니 이름부터 악랄한 Brainf*ck 언어의 탄생비화가 궁금해진다ㅋㅋ
    
    오늘은 내 인생 대학 첫 개강일이지만 코로나 때문에 아쉽게도 2주간 온라인 강의가 진행된다. 하지만 온라인 강의도 서버문제로 원활한 학습이 어렵다ㅠㅠ
    새벽에 공부해야겠다..

"""
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    commands = []
    count_command = 0
    dict_iterator = {}
    latest_iterator = []
    error = 0
    end = False
    while not end:
        check_annotation = 0
        command1 = sys.stdin.readline().strip()
        if command1 == 'end':
            break
        for command in command1:
            if command == '%':
                check_annotation = 1
            elif command == '[':
                if not check_annotation:
                    commands.append('[')
                    count_command+=1
                latest_iterator.append(count_command)
            elif command == ']':
                if latest_iterator:
                    goto = latest_iterator.pop()
                    dict_iterator[count_command] = goto-1
                    dict_iterator[goto-1] = count_command
                if not check_annotation:
                    commands.append(']')
                    count_command+=1
                else:
                    error = 1
                    end = True
                    break
            elif not check_annotation:
                commands.append(command)
                count_command+=1
    if latest_iterator:
        error = 1
    if not error:
        point_list = [0]*32768
        pointer = 0
        jump_token = 0
        i=0
        result = []
        while i <= count_command-1:
            if commands[i] == '<':
                pointer-=1
                if pointer<0:
                    pointer = 32767
            elif commands[i] == '>':
                pointer+=1
                if pointer > 32767:
                    pointer = 0
            elif commands[i] == '+':
                point_list[pointer] += 1
                if point_list[pointer] > 255:
                    point_list[pointer] = 0
            elif commands[i] == '-':
                point_list[pointer] -= 1
                if point_list[pointer] < 0:
                    point_list[pointer] = 255
            elif commands[i] == '.':
                result.append(chr(point_list[pointer]))
            elif  commands[i] == '[':
                if point_list[pointer] == 0:
                    jump_token = 1
            elif commands[i] == ']':
                if point_list[pointer]:
                    jump_token = 1
            if jump_token:
                i = dict_iterator[i]+1
                jump_token = 0
            else:
                i+=1
    print('PROGRAM #'+str(_+1)+':')
    if error:
        print('COMPILE ERROR')
    else:
        print(''.join(result))
