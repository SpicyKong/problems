'''
프로그램 상단의 주석과 list.md파일에 추가할 텍스트를 자동으로 만들어 주는 프로그램
'''

import requests
import datetime
from bs4 import BeautifulSoup    #BeautifulSoup import



def get_form(problem_num,value_result):
    response = requests.get('https://www.acmicpc.net/problem/'+problem_num)
    html = response.text
    soup = BeautifulSoup(html, "html.parser") #html.parser를 사용해서 soup에 넣겠다
    data=soup.select('#problem_title')
    name = data[0].text
    if value_result=='1':
        print("|[Q_"+problem_num+"](https://github.com/SpicyKong/problems/blob/master/BOJ/Q_"+problem_num+".py)|["+name+"](https://www.acmicpc.net/problem/"+problem_num+")|:smile:(성공)|")
        print("\n")
        print("# https://www.acmicpc.net/problem/"+problem_num+" 문제 제목 : "+name+" , 언어 : Python, 날짜 : "+str(datetime.date.today())+", 결과 : 성공")
    else:
        print("|[Q_"+problem_num+"](https://github.com/SpicyKong/problems/blob/master/BOJ/Q_"+problem_num+".py)|["+name+"](https://www.acmicpc.net/problem/"+problem_num+")|:exclamation:(실패)|")
        print("\n")
        print("# https://www.acmicpc.net/problem/"+problem_num+" 문제 제목 : "+name+" , 언어 : Python, 날짜 : "+str(datetime.date.today())+", 결과 : 실패")


a=input().split()
get_form(a[0],a[1])


