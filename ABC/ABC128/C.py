def main():
    from builtins import int, str, map, list, dict, float, print, len, sorted, max, min
    from itertools import accumulate, permutations, combinations
    from collections import deque, defaultdict, Counter
    from operator import itemgetter
    from bisect import bisect_left, bisect_right, bisect
    from heapq import heappop, heappush
    from fractions import gcd
    import sys, re, math, copy
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N,M = input_number()
    k = []
    s = []
    p = []
    for i in range(M):
        ls = input_number_list()
        k.append(ls[0])
        s.append(ls[1:])
    p = input_number_list()


if __name__ == '__main__':
    main()
