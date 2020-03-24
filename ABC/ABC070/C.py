def main():
    from builtins import int, print
    from fractions import gcd
    from functools import reduce
    import sys
    def lcm(x, y):
        return (x * y) // gcd(x, y)

    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_number = (lambda: int(input()))

    N = input_number()
    T = [input_number() for i in range(N)]
    ans = reduce(lcm, T, 1)

    print(ans)


if __name__ == '__main__':
    main()
