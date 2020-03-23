def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    A, B, K = input_number_list()
    t = 0
    i = max(A,B)+1
    while t < K:
        i -= 1
        t += 1 if A % i == 0 and B % i == 0 else 0
    print(i)

if __name__ == '__main__':
    main()
