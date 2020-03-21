import sys
from io import StringIO
import unittest


def resolve():
    import re

    S = input()
    raw = '[ACGT]+'
    pattertn = re.compile(raw)
    p = pattertn.findall(S)
    if p is None:
        print(0)
    else:
        m = 0
        for q in p:
            m = max(m,len(q))
        print(m)




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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
