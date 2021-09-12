import time
from contextlib import redirect_stdout
import io


def decorator1(original_function):
    def wrapper(*arg, **kwargs):
        wrapper.count += 1
        with redirect_stdout(io.StringIO()) as _:
            start = time.perf_counter()
            result = original_function(*arg, **kwargs)
            end = time.perf_counter()
        print(f'{original_function.__name__:<10}\tcall {wrapper.count} executed in{end - start: .4f} sec')
        return result
    wrapper.count = 0
    return wrapper
