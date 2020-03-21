N = int(input())
s = set()
word = input()
s.add(word)
tmp = word[-1]
is_ng = False
for i in range(N-1):
    word = input()
    if word[0] != tmp:
        is_ng = True
        break
    if word in s:
        is_ng = True
        break
    tmp = word[-1]
    s.add(word)
print('YNeos'[is_ng::2])