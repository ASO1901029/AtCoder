import sys
from io import StringIO
import unittest


def resolve():
    N, Q = map(int, input().split())
    S = input()
    count_AC = [0]
    tmp = 0
    for i in range(1, len(S)):
        if S[i - 1] + S[i] == 'AC':
            tmp += 1
        count_AC.append(tmp)
    for i in range(Q):
        l, r = map(int, input().split())
        print(count_AC[r-1] - count_AC[l-1])


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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
