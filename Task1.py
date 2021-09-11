import time
from contextlib import redirect_stdout
import io


def decorator1(original_function):
    def wrapper(*arg, **argn):
        wrapper.count += 1
        with redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            result = original_function(*arg, **argn)
            end = time.perf_counter()
        s = f.getvalue()
        print(f'{original_function.__name__:<10}\tcall {wrapper.count} executed in{end - start: .4f} sec')
        return result
    wrapper.count = 0
    return wrapper
