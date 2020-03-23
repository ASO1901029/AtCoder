def resolve():
    from ABC.ABC058 import C
    C.main()

import sys
from io import StringIO
import unittest

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
        input = """3
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()