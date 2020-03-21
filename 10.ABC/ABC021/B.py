N = int(input())
a,b = map(int,input().split())
K = int(input())
P_list = list(map(int,input().split()))
is_ng = False
is_ng = True if a in P_list or b in P_list else is_ng
is_ng = True if len(P_list) != len(set(P_list)) else is_ng
print('YNEOS'[is_ng::2])