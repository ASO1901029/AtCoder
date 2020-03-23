def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)  # 再帰上限を10＊＊6に

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    t = N // 2
    one = N%2
    print(t+one)
    for i in range(t):
        print(2)
    if one == 1:
        print(1)

main()
