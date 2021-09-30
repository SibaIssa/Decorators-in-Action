# Decorators in action

This repository is part of an assignment for Software Design with Python [SDwP] course, in which we will try to exhaust all the characteristics of python.
__________________________________________________________________________________________________________________________________________________________
This main idea of this repository is to solve Four main tasks as it shown in the below structure:

![sss](https://user-images.githubusercontent.com/51207510/133052391-ecd7d639-b36b-42fe-b005-95a9372a6440.png)


- The First task is to Create a function decorator that calculates function execution time and the number of times the decorated function was called (function call trace).

- In the Second task is an extended implementation of the first task so the decorator could dump original source code of the function. 

- The third task is to implement the decorator behavior in tasks 1 & 2 using a class decorator.

- and the last task is to extend our program so that if a decorated function encounters an error it wouldn’t put it back into stdout. Instead, pipe the error stream into a log file together with a timestamp. 
__________________________________________________________________________________________________________________________________________________________

I implemented the methods that is covered on SDwP course by using Python 3.8.

If you open the 'src' folder you will find five '.py' files. Four files to solve main tasks and a 'main.py' file to test our tasks (I used Four functions for testing process). You can try it by yourself; just open the 'main.py' file and uncomment whatever you want.
