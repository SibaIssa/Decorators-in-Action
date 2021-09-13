import time
import inspect 	
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
        
        with contextlib.redirect_stdout(io.StringIO())as f:
            self.func(*args, **kwargs)
        self.exce_time = time.time() - start

        with open ('Output.txt','w') as w:
            w.write(f"{self.func.__name__} call {self.count} executed in {self.exec_time} sec")
            w.write('\n')
            w.write(f"Name:   {self.func.__name__}")
            w.write('\n')
            w.write(f"Type:   {type(self.func)}")
            w.write('\n')
            w.write(f"Sign:   {inspect.signature(self.func)}")  
            w.write('\n')            
            w.write(f"Args:   positional ({self.func.args}) key=worded ({self.func.kwargs})") 
            w.write('\n')            
            w.write(f"Doc:    {self.func.__doc__}")
            w.write('\n')            
            w.write(inspect.getsource(self.func))
            w.write('\n')            
            w.write(f"Output: {self.func(*args, **kwargs)}") 
            w.write('\n\n')

        if self.calls==4:   #This condition to print the table once all 4 functions are called
            A=sorted(self.calls.items(),key = lambda x: (x[1],x[0]))
            print("PROGRAM  |  RANK  |  TIME ELAPSED")
            for i in range(len(A)):
                print (A[i][0], '       ',i+1,'      ',A[i][1])                        
