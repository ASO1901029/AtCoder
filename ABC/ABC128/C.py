def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number_list = (lambda: list(map(int, input_list())))

    N, M = input_number_list()
    k = []
    s = []
    p = []
    for i in range(M):
        ls = input_number_list()
        k.append(ls[0])
        s.append(ls[1:])
    p = input_number_list()
    switch_max = 2 ** N
    ans = 0
    for i in range(switch_max):
        cnt_if = 0
        for j, switchs in enumerate(s):
            cnt = 0
            for sw in switchs:
                h = 1 << (sw - 1)
                if h & i:
                    cnt += 1
            if cnt % 2 == p[j]:
                cnt_if += 1
        if cnt_if == M:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
