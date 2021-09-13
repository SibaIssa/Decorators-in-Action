import time

def decorator1(func):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        start = time.time()
        Out1=func(*args,**kwargs)
        time1 = time.time()-start
        print(f'{func.__name__} call {count} executed in {time1} sec')
    return wrapper 