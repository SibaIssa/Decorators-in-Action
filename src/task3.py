import time
from inspect import*	
import contextlib 
import io

class decorator3:
    def __init__(self,func):
        self.func=func
        self.calls=0
        self.exce_time=0.0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        start = time.time()
        self.func(*args, **kwargs)
        self.exce_time = time.time() - start
        with open('output.txt', 'w') as w :
            w.write(f"{self.func.__name__} call {self.count} executed in {exectime} sec")
            w.write('\n')
            w.write(f"Name:   {self.func.__name__}")
            w.write('\n')
            w.write(f"Type:   {type(self.func)}")
            w.write('\n')
            w.write(f"Sign:   {signature(self.func)}")  
            w.write('\n')            
            w.write(f"Args:   positional ({self.func.args}) key=worded ({self.func.kwargs})") 
            w.write('\n')            
            w.write(f"Doc:    {self.func.__doc__}")
            w.write('\n')            
            w.write(getsource(self.func))
            w.write('\n')            
            w.write(f"Output: {self.func(*args, **kwargs)}") 
            w.write('\n\n')

    def Rank_table():
        rank_table = dict(sorted(table.items(), key=lambda item: item[1]))
        print("PROGRAM|RANK|TIME ELAPSED")
        n = 1
        for i in rank_table:
            print(i,"\t", n, "\t", rank_table[i])
            n+=1