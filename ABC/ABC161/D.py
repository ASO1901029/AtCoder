def main():
    from builtins import int, map, list, print, len
    from collections import deque
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    K = input_number()
    cnt = [0]
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def check():
        now = 0
        while len(queue) > 0 and cnt[0] < K:
            now = queue.popleft()
            cnt[0] += 1
            x = now % 10
            num_ls = [x - 1, x, x + 1]
            for num in num_ls:
                if num < 0 or num > 9: continue
                queue.append(now * 10 + num)
        print(now)
    check()


if __name__ == '__main__':
    main()
