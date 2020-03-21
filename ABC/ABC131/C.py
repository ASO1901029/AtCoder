import fractions

A,B,C,D = map(int,input().split())
l = C*D // fractions.gcd(C,D)
x = (A-1) -(A-1)//C - (A-1)//D + (A-1)//l
y = B - B//C - B//D + B//l
print(y-x)