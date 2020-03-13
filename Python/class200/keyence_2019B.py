S = input()
ls = ['k', 'e', 'y', 'e', 'n', 'c', 'e']
is_ng = True
idx = 0
tmp = 0
for i in range(len(ls)):
    l = S[:i]
    r = S[-len(ls)+i:]
    if l+r == 'keyence':
        is_ng=False

print('YNEOS'[is_ng::2])
