# TLE
import sys
from io import StringIO
import unittest


def resolve():
    from collections import defaultdict
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(lambda: 0)
    for i in range(len(A)):
        d[A[i]] += 1
    total = 0
    for k,v in d.items():
        total += v*(v-1)//2
    for a in A:
        print(total - (d[a]-1))


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
        input = """5
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
