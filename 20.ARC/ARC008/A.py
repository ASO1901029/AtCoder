N = int(input())
a = N * 15
b = N//10*100 + N%10*15
c = -(-N//10)*100
print(min(a,b,c))