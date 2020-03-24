def main():
    from builtins import int, map, list, float, print, len, min
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    t = 753
    N = input()
    ans = float('inf')
    for i in range(len(N)-2):
        m = int(N[i:i+3])
        ans = min(ans,abs(t-m))
    print(ans)

if __name__ == '__main__':
    main()
