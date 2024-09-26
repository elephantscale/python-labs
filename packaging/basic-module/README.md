# Basic Python Modules

This python will show you how to create your own python module.

## Step 1: Examine Python Module
Go ahead and examine the python file `primes.py`.  

```python
# Primes.py
# This is a simple module which generates prime numbers.

def prime_gen(n):
    """ This generates prime numbers using the sieve of Eratososthenes.
    Input: n: upper bound for prime numbers.
    """
    prime_list = []
    return_primes = []
    for i in range(2, n+1):
        if i not in prime_list:
            return_primes.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return return_primes
```

See what it does?  It generates prime numbers, using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).


## Step 2: Use the module

Let us go ahead and try to use this module in python.

First, let's invoke python:

```bash
python
```

Now you should be at a python prompt.  Go ahead and invoke the module in the following fashion:

```pycon
>>> import primes
>>> primes.prime_gen(100)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

It works!  Pop champagne!

## Step 3: Alter path

What happens if our Python module needs to be invoked from somewhere else?

First, let's get our present working directory (PWD). On Linux/Mac, you can type the following:

```bash
pwd 
```

And you can select the present working directory.

On Windows, simply type

```bash
cd 
```

And it will print the current directory.  On Windows you need to convert the path such as this:

`C:\USERS\MYUSERNAME\PYTHON\` 

to this:

`C:/USERS/MYUSERNAME/PYTHON/`

In other words, change the backslashes to foward slashes.

Now we are in a different directory.so we need to add this to the path.

```python
import sys
sys.path.append('PUT YOUR PRESENT WORKING DIRECTORY HERE')
```

Now, you should be able to do the following:

```pycon
>>> import primes
>>> primes.prime_gen(100)
```

