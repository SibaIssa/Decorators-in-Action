import time
import datetime
import sys, traceback
from io import StringIO
from contextlib import redirect_stdout
from inspect import signature, getsource


def decorator4(func):
    def wrapper(*args, **kargs):
        wrapper.counter +=1
        start_time = time.time()
        try:
            f = StringIO()
            with redirect_stdout(f):
                func(*args, **kargs)
        except Exception:
            with open("exceptionLog.txt", "a") as log:
                date = datetime.datetime.now()
                log.write("Date timestamp: {0}".format(date))
                # traceback.print_exc(file=log) or format_exc() same functionality
                # print_exc put to file  but format_exc to string 
                trace_str = traceback.format_exc()
                log.write(trace_str)
            log.close()

        executed_time = time.time() - start_time
        print("{0} call {1} executed in {2} sec\n".format(func.__name__ ,wrapper.counter, round(executed_time, 4)))
        print(
            """
            Name: {0}\n
            Type: {1}\n
            Sign: {2}\n
            Args: positional {3}\n
                  key=worded {4}
            Doc: {5}\n
            Source: {6}\n
            Output: {7}
        """.format(func.__name__, type(func), signature(func), args, kargs, func.__doc__, getsource(func), f.getvalue()))
    wrapper.counter = 0
    return wrapper


class BestDecor4:
    def __init__(self, func):
        self.calls = 0 # number of function calls
        self.func = func # function itself
        self.executed_time = 0
        
    def __call__(self, *args, **kargs):
        self.calls += 1
        start_time = time.time()
        try:
            f = StringIO()
            with redirect_stdout(f):
                self.func(*args, **kargs)
        except Exception:
            with open("exceptionLog.txt", "a") as log:
                date = datetime.datetime.now()
                log.write("Date timestamp: {0}".format(date))
                # traceback.print_exc(file=log) or format_exc() same functionality
                # print_exc put to file  but format_exc to string
                # trace_str = traceback.format_exc()
                traceback.print_exc(file=log)
            log.close()

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
        
