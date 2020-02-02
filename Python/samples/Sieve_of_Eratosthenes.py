# エラトステネスのふるい
# １～ｎまでの素数を求めるような処理が高速にできる

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


if __name__ == '__main__':
    n = 100
    data = get_sieve_of_eratosthenes(n)
    print(' '.join(map(str, data)))
    print("2～{0}までで以上が素数です\n".format(n))
