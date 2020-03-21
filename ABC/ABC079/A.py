N = input()
print('YNeos'[not (N[0]==N[1]==N[2] or N[1]==N[2]==N[3])::2])