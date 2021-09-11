# Software Desgin with Python Assignment1

This repo contain the files for my first assignment in SDwP subject , M21-RO, Innopolis University.


## Authors

- [@Ali Jnadi](https://github.com/AliJnadi)

  
## Usage/Examples
This repo contains five .py files

1. main.py
  This is the main file where you can find seven functions for testing.

2. Task1.py
  This contains decorator1 witch is a function decorator that print the count of calling a function with the excuation time. It is very imporatant to illustrate that this decorator prvent decorated function from printing its output.
```python
from Task1 import decorator1

@decorator1
def some_function:
  .
  .
  .
  .

if __name__ == '__main__':
  pascal(5)
  pascal(6)
  fib(5)
  pascal(3)
  fib(7)
```
        
Runing the previous code you will get the folowing result:
```python
pascal	call 1 executed in 0.0001 sec
pascal	call 2 executed in 0.0001 sec
fib  	call 1 executed in 0.0000 sec
pascal	call 3 executed in 0.0000 sec
fib  	call 2 executed in 0.0000 sec
```

3. Task2.py
  This contains decorator2 witch is a function decorator that extend decorator1 task and print a full informations about call function like name, type, signatue, parameters, ........ etc...
```python
from Task2 import decorator2

@decorator2
def some_function:
  .
  .
  .
  .

if __name__ == '__main__':
  pascal(3)
```
The output will be the folowing:
```python
pascal call 1 executed in 0.0001 sec
Name: 	pascal
Type: 	<class 'function'>
Sign: 	(n)
Args: 	positional (3,) 
        key_worded {}

Doc:	This function print pascal triangle
		:param n: The number of pascal triangle rows
		This function return None

Source:	@decorator2
		def pascal(n):
		    """
		    This function print pascal triangle
		    :param n: The number of pascal triangle rows
		    This function return None
		    """
		    main_v = [1]
		    added_v = [0]
		    for _ in range(n):
		        print(main_v)
		        main_v = [left + right for left, right in zip(main_v + added_v, added_v + main_v)]
		
Output:	[1]
		    [1, 1]
		    [1, 2, 1]
```
4. Task3.py
This is a class decorator, decorator3, witch is extend for decorator1, this decorator append its output (number of calling and excecuation time) to a Task3.txt file (if file is not exixst it will create it) and this class has a function called "print_rank()", this function print the ranking of calling functions from fastest to slowest depend on excuation time.
```python
from Task3 import decorator3

@decorator3
def some_function:
  .
  .
  .
  .

if __name__ == '__main__':
  pascal(3)
  fib(7)
  factorial(5)
  q_solver(1, 4, 4)

  decorator3.print_rank()
```
The output will be the folowing:
```python
PROGRAM  |  RANK  |  TIME ELAPSED
factorial     1       0.000018960s
fib           2       0.000047165s
pascal        3       0.000105890s
q_solver      4       0.002138820s
```

5. Task4.py
  This is another class decorator, decorator4, this decorator used with any other decorators to prevent errors from interrupting the program. If any other decorator faces an exception this decorater will catch it, write to a log file: time stamp, name of the function that throw the exception, and the exception message.
```python
from Task1 import decorator1
from Task4 import decorator4

@decorator4
@decorator1
def some_function:
  .
  .
  .
  .

if __name__ == '__main__':
  pascal(3)
  test(0)
  factorial(5)
```
The output will be the folowing
```python
pascal    	call 1 executed in 0.0001 sec
Error in calling test written in the log file.
factorial 	call 1 executed in 0.0000 sec
```
As you can see the division by zero dosen't terminate the program, because the exception error sent to the log file, and an erro massage printed on the terminal.
    
    21-09-11 18:55:55:  function test division by zero 
