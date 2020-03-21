def next(S='a'):
    idx = len(S)
    cnt = len(set(list(S)))
    if idx == N:
        print(S)
        return
    for i in range(cnt):
        if cnt < i:
            break
        next(S +ls[i])

N = int(input())
ls = ['a','b','c','d','e','f','g','h','i','j']
next()