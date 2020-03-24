def main():
    from builtins import int, map, list, print, min
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    ls = []
    for i in range(5):
        ls.append(input_number())
    mini = min(ls)
    cnt = -(-N//mini)+4
    print(cnt)

if __name__ == '__main__':
    main()
