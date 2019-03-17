import primes
import time

class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.end = time.clock()
        self.interval = self.end - self.start


if __name__ == '__main__':
    n = 39916801

    # We can call pre-existing c++ code from Python 
    # by wrapping it in Cython 
    with Timer() as t:
        result = primes.is_prime(n)
    print('{} (s) {}'.format(t.interval, result))
