import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw_a_1 = (x1 * y3 + x3 *y4+ x4*y1)-(x3*y1+x4*y3+x1*y4)
ccw_a_2 = (x2*y3+x3*y4+x4*y2) - (x3*y2+x4*y3+x2*y4)

ccw_a = ccw_a_1 * ccw_a_2

ccw_b_1 = (x3 * y1 + x1 *y2+ x2*y3)-(x1*y3+x2*y1+x3*y2)
ccw_b_2 = (x4 * y1 + x1 *y2+ x2*y4)-(x1*y4+x2*y1+x4*y2)

ccw_b = ccw_b_1 * ccw_b_2

if(ccw_a==0 and ccw_b==0):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2)<= max(y3, y4) and min(y3,y4) <= max(y1, y2):
        print(1)
    else:
        print(0)
elif(ccw_a<=0 and ccw_b<=0):
    print(1)
else:
    print(0)