# NG
from collections import Counter

n = int(input())
l = list(map(int, input().split()))

even_l = l[0::2]
odd_l = l[1::2]

even_c = Counter(even_l)
odd_c = Counter(odd_l)
em = even_c.most_common()
om = odd_c.most_common()

ans = 0
if len(em) > 1 and len(om) > 1:
    if em[0][0] == om[0][0]:
        if em[0][1] > om[0][1]:
            ans += n - em[0][1] - om[1][1]
        else:
            ans += n - em[1][1] - om[0][1]
    else:
        ans += n - em[0][1] - om[0][1]
elif len(em) == 1 and len(om) == 1:
    if em[0][0] == om[0][0]:
        ans = n / 2
    else:
        ans = 0
elif len(em) == 1:
    ans = (n / 2) - om[1][1]
else:
    ans = (n / 2) - om[0][1]
print(int(ans))
