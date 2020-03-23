import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    h = list(map(int, input().split()))

    dp = [0] * N
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))
    print(dp[-1])


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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
