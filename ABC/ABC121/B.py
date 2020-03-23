def main():
    from builtins import int, map, list, print
    import sys

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: map(int,input().rstrip().split()))
    input_number_list = (lambda: list(map(int, input_list())))

    N, M, C = input_number()
    B = input_number_list()
    A = [None] * N
    for i in range(N):
        A[i] = input_number_list()
    ans = 0
    for i in range(N):
        t = C
        for j in range(M):
            t += A[i][j] * B[j]
        ans += t > 0 and 1 or 0
    print(ans)


def resolve():
    main()


if __name__ == '__main__':
    resolve()

import sys
import unittest
from io import StringIO


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 3 -10
1 2 3
3 2 1
1 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
