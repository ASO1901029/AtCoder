S = input()
w = ['Sunny', 'Cloudy', 'Rainy']
idx = w.index(S) + 1
if idx == 3:
    idx = 0
print(w[idx])
