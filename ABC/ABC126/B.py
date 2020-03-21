S = input()
is_YYMM = True
is_MMYY = True
if int(S[0] + S[1]) > 12 or int(S[0] + S[1]) == 0:
    is_MMYY = False
if int(S[2] + S[3]) > 12 or int(S[2] + S[3]) == 0:
    is_YYMM = False

if is_MMYY and is_YYMM:
    print('AMBIGUOUS')
elif is_YYMM:
    print('YYMM')
elif is_MMYY:
    print('MMYY')
else:
    print('NA')
