import array_tools
import time
import numpy as np

class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.end = time.clock()
        self.interval = self.end - self.start

if __name__ == '__main__':

    array = np.linspace(0, 10, 10000)

    with Timer() as t:
        result = np.sum(array)
    print('{:7.5f} (s) {:7.5f}'.format(t.interval, result))

    with Timer() as t:
        result = array_tools.sum(array)
    print('{:7.5f} (s) {:7.5f}'.format(t.interval, result))

