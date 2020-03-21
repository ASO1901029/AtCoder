S = input()
is_odd = True
is_ng = False
for c in S:
    if is_odd:
        if c == 'L':
            is_ng = True
            break
        is_odd = not is_odd
    else:
        if c == 'R':
            is_ng = True
            break
        is_odd = not is_odd
print('YNeos'[is_ng::2])