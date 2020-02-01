# 準備
num_list = [0] * 1000000
i = 2
cnt = 0
for num in range(2,len(num_list)):
    if num_list[i] == -1:
        num_list[i] = num_list[i-1]
        i += 1
        continue
    cnt+=1
    num_list[i] = cnt
    for j in range(i*2,len(num_list),i):
        num_list[j] = -1
    i += 1

while True:
    try:
        n = int(input())
    except Exception as e:
        break
    print(int(num_list[n]))