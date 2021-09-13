import time
from inspect import*	

def decorator2(func):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        start = time.time()
        Out1=func(*args)
        time1 = time.time()-start
        print(f'{func.__name__} call {count} executed in {time1} sec')
        print('Name:', func.__name__)
        print('Type:', type(func))
        print('Sign:', func.__code__.co_varnames)
        print('Args:', 'positional', args, 'key=worded', kwargs)
        print('Doc:', func.__doc__)
        print('Source:', getsource(func))
        print('Output:',func(*args, **kwargs))
    return wrapper 