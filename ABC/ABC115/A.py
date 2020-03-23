def main():
    from builtins import int, map,list, print
    import sys

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))
    sys.setrecursionlimit(10 ** 6)  # 再帰上限を10＊＊6に

    D = input_number()
    ans = 'Christmas'
    r = 25 - D
    for i in range(r):
        ans+=' Eve'
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
        input = """25"""
        output = """Christmas"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """22"""
        output = """Christmas Eve Eve Eve"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()