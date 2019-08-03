data = [int(b) for b in input().split()]
day = data[0]- data[1]
days = data[2]/day
a = data[2] - data[0]
if a/day - int(a/day)>0:
    print(int(a/day)+2)
else:
    print(int(a/day+1))
