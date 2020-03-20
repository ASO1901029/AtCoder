# # TLE
# a,b,c = map(int,input().split())
# is_ng = True
# if a**0.5+b**0.5 < c**0.5:
#     is_ng = False
# print('YNeos'[is_ng::2])

a, b, c = map(int, input().split())
d = c - a - b
print('YNeos'[not (d>0 and d**2 > 4*a*b)::2])

