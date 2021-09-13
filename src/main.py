import random
import math
from task1 import decorator1
from task2 import decorator2
from task3 import decorator3

#@decorator1
#@decorator2
#@decorator3
#@decorator4
def palindromes(a):
    res=list(filter(lambda word: word.lower() == "".join(reversed(word.lower())),a))    
    print(res)

#@decorator1
#@decorator2
#@decorator3
#@decorator4
def even_numbers(n):
    return list(filter(lambda i: i % 2 == 0, n))

#@decorator1
#@decorator2
#@decorator3
#@decorator4
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]


#@decorator1
#@decorator2
#@decorator3
#@decorator4
def quardicEqSolver(a, b, c): 
    d = b * b - 4 * a * c  
    sqrt_ = math.sqrt(abs(d))
    if d > 0:
        print(f"{(-b + sqrt_) / (2 * a)} and {(-b - sqrt_) / (2 * a)}")
    elif d == 0:
        print(f"{-b / (2 * a)}")  
      
    else:
        print(f"{- b / (2 * a)} + i {sqrt_} and {- b / (2 * a)} - i {sqrt_} ")  
            

        

    
if __name__ == "__main__": 
    palindromes(["php", "Innopolis", "Python", "Pop", "Java", "aaa"])
    even_numbers([1, 2, 3, 4, 5])
    pascal_triangle(4)
    quardicEqSolver(5,10,3)
    