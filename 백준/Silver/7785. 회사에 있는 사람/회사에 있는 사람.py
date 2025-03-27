import sys

dic=dict()
num=int(sys.stdin.readline())

for i in range(num):
    name, door = sys.stdin.readline().split(' ')
    if(door=='enter\n'):
        dic[name]=1
    else:
        dic[name]=0

li=[]
for temp in dic:
    if dic[temp]==1:
        li.append(temp)

li.sort(reverse=True)

for i in range(len(li)):
    print(li[i])