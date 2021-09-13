import datetime;
import time,io
import contextlib
import inspect
import traceback

def decorator4(func):           
    count = 0
    def wrapper(*args,**kwargs): 
        nonlocal count 
        count += 1 
        start = time.time()
        try:    
            func(*args,**kwargs) 
        except Exception as error:
            with open("log file.txt","a") as w:
                w.write(f'{datetime.datetime.now().timestamp()}\n')
        else:           
            print(f'{func.__name__} call {count} executed in {time.time()-start} sec')
          
    return wrapper 