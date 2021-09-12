import time
from contextlib import redirect_stdout
import io
import inspect


def decorator2(original_function):
    def wrapper(*arg, **kwargs):
        wrapper.count += 1
        with redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            result = original_function(*arg, **kwargs)
            end = time.perf_counter()
        s = f.getvalue()

        print(f'{original_function.__name__} call {wrapper.count} executed in {end - start:.4f} sec')
        print(f'Name: \t{original_function.__name__}')
        print(f'Type: \t{type(original_function)}')
        print(f'Sign: \t{inspect.signature(original_function)}')
        print(f'Args: \tpositional {arg} \n\t\tkey_worded {kwargs}\n')
        print(f'Doc:\t{inspect.getdoc(original_function)}'.replace('\n', '\n\t\t'), end='\n\n')
        print(f'Source:\t{inspect.getsource(original_function)}'.replace('\n', '\n\t\t'), end='\n')
        print(f'Output:\t{s}'.replace('\n', '\n\t\t'))

        return result
    wrapper.count = 0
    return wrapper
