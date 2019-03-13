import primes
import time

class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.end = time.clock()
        self.interval = self.end - self.start

def is_prime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':

    n = 39916801

    with Timer() as t:
        result = is_prime(n)
    print('{} (s) {}'.format(t.interval, result))

    with Timer() as t:
        result = primes.is_prime(n)
    print('{} (s) {}'.format(t.interval, result))

