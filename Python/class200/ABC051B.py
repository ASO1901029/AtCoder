k, s = map(int, input().split())
cnt = 0

for i in range(k, -1, -1):
    # 1桁目を決定する
    if s - i > k * 2:
        continue

    # 2桁目を決定する
    for j in range(k, -1, -1):
        # 3桁目を決定する
        x = s - i - j

        if x > k:
            # 3桁目が設定できないとき
            continue
        cnt += x >= 0
print(cnt)
