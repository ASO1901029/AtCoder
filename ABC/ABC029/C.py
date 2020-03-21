def next(s=''):
    if len(s) < N:
        for c in c_ls:
            next(s+c)
    else:
        print(s)


N = int(input())
c_ls = ['a','b','c']
next()