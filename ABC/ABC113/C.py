def main():
    from builtins import int, map, list, print
    from collections import deque
    from bisect import bisect_left
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number_list = (lambda: list(map(int, input_list())))

    N, M = input_number_list()
    pref = [[0] for i in range(N + 1)]
    q = deque()
    for i in range(M):
        p, y = map(int, input_number_list())
        pref[p].append(y)
        q.append((p, y))
    for p in pref:
        p.sort()
    for p, y in q:
        print('{:06}{:06}'.format(p, bisect_left(pref[p], y)))


if __name__ == '__main__':
    main()
