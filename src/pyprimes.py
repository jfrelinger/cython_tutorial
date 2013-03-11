def primes():
    result = []
    kmax = 10
    p = [0,0,0,0,0,0,0,0,0,0]
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

if __name__ == '__main__':
    print primes()