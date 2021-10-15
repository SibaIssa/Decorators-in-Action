import time
from io import StringIO
from contextlib import redirect_stdout
from inspect import signature, getsource

class decorator3:
    def __init__(self, func):
        self.calls = 0 # number of function calls
        self.func = func # function itself
        self.executed_time = 0
        
    def __call__(self, *args, **kargs):
        self.calls += 1
        start_time = time.time()
        f = StringIO()
        with redirect_stdout(f):
            self.func(*args, **kargs)
        executed_time = time.time() - start_time
        self.executed_time = executed_time
        # Put dumps into one file
        # if each function need to be in different files
        # with open(f"stdout_{self.func.__name__}.txt", "w+") as f:
        with open('stdout.txt', 'a') as file:
            file.write("{0} call {1} executed in {2} sec\n".format(self.func.__name__ ,self.calls, round(executed_time, 4)))
            file.write(
            """
            Name: {0}\n
            Type: {1}\n
            Sign: {2}\n
            Args: positional {3}\n
                  key=worded {4}
            Doc: {5}\n
            Source: {6}\n
            Output: {7}\n
            {8}
            """.format(self.func.__name__, type(self.func), signature(self.func), args, kargs, self.func.__doc__, getsource(self.func), f.getvalue(), '-'*20))
        file.close()
