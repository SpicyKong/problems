# 문제 제목 : 카드 역배치 , 언어 : Python, 날짜 : 20190730

list_a = list(range(1,21)) # 1부터 20까지 들어있는 리스트 생성

input_a = [input().split(' ') for _ in range(10)] # 입력받기

for a in input_a:
    start_r = int(a[0])-1 # 바꾸기 시작하는 인덱스
    end_r = int(a[1]) # 끝나는 인덱스
    list_a[start_r:end_r] = list_a[start_r:end_r].__reversed__() # 리스트[start_r:end_r]를 뒤집고 원래 리스트의 자리에 저장
    
    
[print(b, end=' ') for b in list_a] # 문제의 조건에 맞게 출력하기
