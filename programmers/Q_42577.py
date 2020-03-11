"""
    회고:
    아래코드가 시간초과가 안나는 이유를 모르겠다. O(N^2)인데..
    그리고 처음보는 함수로 구현하신분들도 있고 regex로 구현하신분도 있어서 내 지식의 짧음을 뼈저리게 느꼇다.
    이 코드는 로컬에만 저장해야겠다..ㅋㅋ

    todo:
    startswith + zip, regex,
"""
def solution(phone_book):
    phone_book=sorted(phone_book, key = lambda a:len(a))
    for i1, num1 in enumerate(phone_book):
        for i2, num2 in enumerate(phone_book):
            if not i1==i2:
                token = 0
                for i,word in enumerate(num1):
                    if not num1[i] == num2[i]:
                        token = 1
                        break
                if token == 0:
                    return False
    return True
