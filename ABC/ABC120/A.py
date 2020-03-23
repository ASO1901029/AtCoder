def main():
    from builtins import int, map, list, print, min
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    A,B,C = input_number_list()
    print(min(B//A,C))

if __name__ == '__main__':
    main()
