def main():
    from builtins import int, map, list, print, min
    from collections import Counter
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_str = (lambda: input().rstrip())
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    N = input_number()
    S = [None] * N
    for i in range(N):
        S[i] = list(input_str())

    ans = ""
    for c in alphabet:
        t = 10**9
        for i in range(N):
            t = min(t,int(Counter(S[i])[c]))
        ans += c*t
    print(ans)

if __name__ == '__main__':
    main()
