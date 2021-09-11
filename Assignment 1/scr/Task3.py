import time
from contextlib import redirect_stdout
import io


class decorator3:
    rank = {}

    def __init__(self, original_function):
        self.fun = original_function
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        with redirect_stdout(io.StringIO()) as _:
            start = time.perf_counter()
            result = self.fun(*args, **kwargs)
            end = time.perf_counter()
            self.rank[self.fun.__name__] = end - start
            with open('Task3_Output.txt', 'a+') as f:
                f.write(f'{self.fun.__name__: <10}\tcall {self.count} executed in{end - start: .4f} sec\n')
        return result

    @staticmethod
    def print_rank():
        print('PROGRAM  |  RANK  |  TIME ELAPSED')
        res = dict(sorted(decorator3.rank.items(), key=lambda item: item[1]))
        i = 0
        for k in res:
            i += 1
            print(f'{k: <14}{i: <8}{res[k]:.9f}s')
