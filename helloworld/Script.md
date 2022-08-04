Running with Script
=============

## Overview

We will now run a python script from a file.

## Step 1: Open helloworld.py in your favorite text editor.

Start your favorite programmer's text editor. This will depend on your platform:

Windows:

* pycharm **(Recommended)**
* Notepad++ (don't use notepad.exe)
* Sublime Text

Mac:

* pycharm **(Recommended)**
* Textedit (included with macOS)
* Sublime Text

Linux:

* pycharm **(Recommended)**
* Vscode (included with Lab environment)
* vi/vim
* nano
* Sublime Text

Create a file called `helloworld.py`  and open it with the editor of your choice.

## Step 2: Start Typing Python Code

Type the following code into your text editor

```python
print("Hello world!")

a = 10
b = 3.1
c = "hello world"
```

Save your text editor code.

## Step 3: Run your program from the command line

```bash
python3 helloworld.py
```

Which should print out the following

```console
Hello world!
```

## Step 3: Evaluate the result of your variables

Note that simply typing variable names doesn't actually print anything here.

**Why not?**

We can explicitly print things:

```python
print(a)
print(b)
```

**=> TRY re-running to see the results.**

Use concatenation operator as plus on strings

```python
"Hello" + c 
```

This operator requires things to be strings. If not, you can always convert it using str(variablename)

```python
print("hello" + str(a))
```

Try some arithmetic operations with your variables, like this:

```python
a + b
a * b
a / b
```





