import sys
from io import StringIO
import unittest


def resolve():
    S = input()
    S2 = S[:(len(S) - 1) // 2]
    S3 = S[(len(S) + 3) // 2 -1:]
    is_ng = False
    for i in range(len(S)):
        if S[i] != S[-i - 1]:
            is_ng = True
    for i in range(len(S2)):
        if S2[i] != S2[-i - 1]:
            is_ng = True
    for i in range(len(S3)):
        if S3[i] != S3[-i - 1]:
            is_ng = True
    print('YNeos'[is_ng::2])

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
        input = """akasaka"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """level"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
