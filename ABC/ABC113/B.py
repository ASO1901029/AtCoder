def main():
    from builtins import int, map, list, float, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    T,A = input_number_list()
    H = input_number_list()
    m = float('inf')
    idx = -1
    for i in range(N):
        if m > abs(A-(T-H[i]*0.006)):
            m = abs(A-(T-H[i]*0.006))
            idx = i
    print(idx+1)

if __name__ == '__main__':
    main()
