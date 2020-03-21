N = int(input())
a = list(map(int, input().split()))

isApproved = True

for x in a:
    if x % 2 == 0:
        if not(x % 3 == 0 or x % 5 == 0):
            isApproved = False

if isApproved:
    print("APPROVED")
else:
    print("DENIED")
