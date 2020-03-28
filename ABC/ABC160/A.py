def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    S = input()
    if S[2]==S[3] and S[4] == S[5]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
