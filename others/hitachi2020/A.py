S = input()
is_hitachi = True
if len(S) %2 == 0:
    for i in range(0, len(S), 2):
        if not (S[i] == 'h' and S[i + 1] == 'i'):
            is_hitachi = False
    print('YNeos'[not is_hitachi::2])
else:
    print('No')
