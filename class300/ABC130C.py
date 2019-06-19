W,H,x,y = map(int,input().split())
w = W/2
h = H/2
ansA,ansB = 0
ansA = W*H/2
if w == x and h == y:
    ansB = 1
print(ansA,ansB)