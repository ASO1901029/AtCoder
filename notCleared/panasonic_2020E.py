# TLE
a = input()
b = input()
c = input()

ls = [a, b, c]

mix_list = []
# 順番を決定する
ans = 2000 * 3
for i in range(len(ls)):
    left = ls[i]
    for j in range(len(ls)):
        if i != j:
            mid = ls[j]
            for k in range(len(ls)):
                if not k in [i,j]:
                    right = ls[k]
                    # 一番合致するところで合体させる
                    for n in range(min(len(left), len(mid)) - 1, -1, -1):
                        lm = left + mid
                        if left[-n] == mid[0] or left[-n]=='?' or mid[0]=='?':
                            is_connect = True
                            for m in range(n):
                                if left[-n] != mid[m] or left[-n]=='?' or mid[m]=='?':
                                    is_connect = False
                                    break
                            if is_connect:
                                lm = left[:-n] + mid
                        lmr = lm + right
                        for n in range(min(len(lm), len(right)) - 1, -1, -1):
                            if lm[-n] == right[0] or lm[-n] == '?' or right[0] == '?':
                                is_connect = True
                                for m in range(n):
                                    if lm[-n] != right[m] or lm[-n] == '?' or right[m] == '?':
                                        is_connect = False
                                        break
                                if is_connect:
                                    lmr = lm[:-n] + right
                        ans = min(len(lmr), ans)
print(ans)
