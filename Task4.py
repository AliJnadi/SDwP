import sys
import traceback
from datetime import datetime

class decorator4:
    def __init__(self, original_decorator):
        self.fun = original_decorator

    def __call__(self, *args, **kwargs):
        try:
            res = self.fun(*args, **kwargs)
            return res
        except Exception as e:
            tb = sys.exc_info()[-1]
            stk = traceback.extract_tb(tb)
            with open('log_file.txt', 'a+') as f:
                f.write(f'{datetime.strftime(datetime.now(), f"%y-%m-%d %H:%M:%S: ")}function {stk[2][2]} {e} \n')
        return None
