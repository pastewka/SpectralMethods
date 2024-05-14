---
layout: default
title: "Flow control and functions"
parent: Python
date: 2024-05-14
categories: python
author: Lars Pastewka
nav_order: 3
---

# Flow control and functions

## Learning goals
- Conditionals
- loops
- Comprehensions
- Functions
     - Scope
     - Recursion

## Flow control
We use flow control mechanisms to allow our programs to make decisions, i.e., flow control determines what parts of a program are executed in which order. Python offers three such mechanisms; _conditionals_, _exceptions_, and _loops_. Teaching the handling of exceptions is outside the scope of this class, but if you are interested in learning more about them, feel free to ask us or refer to Chapter 4 of [Effective Computation in Physics](https://ebookcentral.proquest.com/lib/ubfreiburg/reader.action?docID=3564547).

#### Excursion: Python Blocks

So far, we have only used simple Python statements that were executed in a linear fashion one after another. Flow control is precisely about mixing up the order of executions of parts of code.

A piece of code that is executed linearly together is called a _code block_.
Python uses whitespace indentation to delimit program blocks:

```python
Block1
Block1
    Block2
    Block2
Block1
Block1
    Block3
    Block3
        Block4
        Block4
    Block3
    Block3
Block1
Block1
```

Blocks can contain sub-blocks. The recommended indentation depth is [4 spaces](https://www.python.org/dev/peps/pep-0008/).


### Conditionals
This section is partly taken from [software carpentry ](http://swcarpentry.github.io/python-novice-inflammation/07-cond/)

We can ask Python to take different actions, depending on a condition, with an if statement:



```python
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')

```

    not greater
    done


The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the block indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:
![Executing a Conditional](figures/python-flowchart-conditional.svg)

The relevant comparison operators are given in the following table. Assume `a = 10`, `b = 20`.

| Operator | Description                                                                                                      | Example                                           |
|----------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| ==       | If the values of two operands are equal, then the condition becomes true.                                        | (a == b) is not true.                             |
| !=       | If values of two operands are not equal, then condition becomes true.                                            |                                                   |
| <>       | If values of two operands are not equal, then condition becomes true.                                            | (a <> b) is true. This is similar to != operator. |
| >        | If the value of left operand is greater than the value of right operand, then condition becomes true.            | (a > b) is not true.                              |
| <        | If the value of left operand is less than the value of right operand, then condition becomes true.               | (a < b) is true.                                  |
| >=       | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.| (a >= b) is not true.                             |
| <=       | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.   | (a <= b) is true.                                 |

Conditional statements do not necessarily have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:



```python
num = 53
print('before conditional...')
if num > 100:
    print('53 is greater than 100')
print('...after conditional')
```

    before conditional...
    ...after conditional


We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.


```python
num = -3
if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")

```

    -3 is negative


One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.
We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:




```python
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('one part is not true')
```

    one part is not true


while `or` is true if at least one part is true:


```python
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
```

    at least one test is true


#### Tasks

Use your notebook from last week and solve these tasks in. Take advantage of the markdown cells to take notes.

- How many paths?

    Which of the following would be printed if you were to run this code? Why did you pick this answer?

    1.  A
    2.  B
    3.  C
    4.  B and C

```python
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```


- What is truth?

    After reading and running the code below,
    explain what the rule is for which values are considered true and which are considered false.

```python
if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')
```


- Close enough

    Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
    and `False` otherwise.
    Compare your implementation with your partner's:
    do you get the same answer for all possible pairs of numbers?



### Loops
In computational science, it is fairly common to apply an action to a large data set. For instance, if you wish to compute the volume $V$ of a finite element model, you need to
- retrieve the Jacobian of the shape functions $J_i$ for each Gauss point and the associated weights.
- compute the integral of the Jacobian over the entire mesh using Gaussian integration $$V = \sum_i{J_i\, w_i}$$

Assume we have the data in two lists (we will learn about more efficient containers for computational data next week)


```python
J = [ 0.68317717,  0.01132594,  0.36122905,  0.94205695,
      0.69374011,  0.79858585,  0.26400973,  0.64446646]
W = [ 2.0       ,  1.0       ,  0.88888889,  0.55555556,
      2.0       ,  1.0       ,  0.88888889,  0.55555556]
```

With what you learned last time, this seemingly simple task seems shockingly tedious to solve:


```python
volume = J[0]*W[0] + J[1]*W[1] + J[2]*W[2] + J[3]*W[3] + J[4]*W[4] + J[5]*W[5] + J[6]*W[6] + J[7]*W[7]
print(volume)
```

    5.000916056634814


This is not only tedious, but also next to useless if the data changes, for instance because you refined your mesh and have longer lists. The solution for this problem is the use of _loops_.

Python's most widely used type of loop (and the only one we'll show here) is the so-called `for`-loop, which is typically used to iterate over a container (more precisely, over any _iterable_, but more on this later). A `for`-loop has the following syntax:

```python
for <loop-var> in <iterable>:
    <do action using <loop-var>>
```

The action is executed as many times as there is elements in the iterable, and `<loop-var>` takes the value of a new element of the iterable at every passage. A simple example:


```python
for countdown in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "Happy new year!"]:
    print(countdown)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Happy new year!


In this case, the iterable was a `list`, but Python has many iterable objects, for instance strings:


```python
word = "Hakuna"
for letter in word:
    print(letter)
```

    H
    a
    k
    u
    n
    a


Dictionaries:


```python
my_dict = {"height": 0.21022, "width": 0.29730, "title": "The life of Edgar"}
for key in my_dict:
    print(key, ":", my_dict[key])
```

    title : The life of Edgar
    height : 0.21022
    width : 0.2973


Two particularly practical iterables are `range` and `zip`:


```python
word1 = "Hakuna"
word2 = "Matata"

print("loop 1:")
for i in range(len(word1)):
    print(word1[i])

print("loop 2:")
for letter1, letter2 in zip(word1, word2):
    print(letter1, letter2)
```

    loop 1:
    H
    a
    k
    u
    n
    a
    loop 2:
    H M
    a a
    k t
    u a
    n t
    a a


#### Tasks

- Use the notebook help (see last week's session if you forgot how to use it) to understand what `range`, `len`, and `zip` do. Do not get intimidated if you do not understand the help for `zip` but ask us. Reading documentation for a new programming language takes getting used to.

- Solve the FEM mesh volume problem in a smarter way using the `range` function.
- Solve the FEM mesh volume problem in a smarter way using the `zip` function. Which version do yop prefer and why?

### Comprehensions

Loops are great, but sometimes somewhat of an overkill. Imagine you wish to double the elements of a list of integers, or filter out the even ones:


```python
data = [103, 117,  17,  10,  99,  14,  50,  22,  43, 119]

double_data = list()
odd_data = list()

for number in data:
    double_data.append(2*number)
    if number % 2 == 1:
        odd_data.append(number)
double_data
```




    [206, 234, 34, 20, 198, 28, 100, 44, 86, 238]




```python
odd_data
```




    [103, 117, 17, 99, 43, 119]



Python offers the so called _list comprehension_ syntax which is borrowed from set theory.
```python
filtered_list = [<expression> for <loop-var> in <iterable> if <condition>]
```

with this syntax, the above problems become one-liners.


```python
data = [103, 117,  17,  10,  99,  14,  50,  22,  43, 119]

double_data = [2*number for number in data]
odd_data = [number for number in data if number%2 == 1]

double_data
```




    [206, 234, 34, 20, 198, 28, 100, 44, 86, 238]




```python
odd_data
```




    [103, 117, 17, 99, 43, 119]



#### Tasks

- Use the notebook help to learn what the `sum` function does.
- How can you use this to write the FEM mesh volume problem as a _readable_ one-liner?

#### Discussion

You have learned how to get Python to make decisions with `if-elif-else` statements and how to reuse simple code snippets using the `for`-loop. You have also learned to make simple loops more concise and readable using list comprehensions.

What you learned about flow control thus far should be enough for everything we will do in this class. However, Python has much more to offer in this regard, and you are strongly encouraged to learn more about this on your own, specifically about generator object, dict- and set-comprehensions, for instance in Chapter 4 of [Effective Computation in Physics](https://ebookcentral.proquest.com/lib/ubfreiburg/reader.action?docID=3564547).

### Functions
In the previous section, we have learned how to reuse small code snippets and applying them to arbitrarily large data sets using loops and comprehensions,  and have Python make decisions based on what it sees in our data.

But, what if our code is getting pretty long and complicated; what if we had thousands of datasets, and wanted to perform similar, but not the exactly same operations on them?. Also, what if we wanted to use that code again, on a different dataset or at a different point in our program? Cutting and pasting it is going to make our code get very long and very repetative, very quickly. Plus imagine you find a bug in a piece of code that you have pasted in two dozen places in your program; you'd have to fix it one-by-one. We’d like a way to package our code so that it is easier to reuse, and Python provides for this by letting us define things called _functions_ - a shorthand way of re-executing longer pieces of code.

Let’s start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:




```python
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
```

The function definition opens with the word `def`, which is followed by the name of the function and a parenthesized list of parameter names. The body of the function — the statements that are executed when it runs — is indented below the definition line, typically by four spaces.
When we call the function, the values we pass to it are assigned to those variables so that we can use them inside the function. Inside the function, we use a `return` statement to send a result back to whoever asked for it.

Let’s try running our function. Calling our own function is no different from calling any other function:




```python
print('freezing point of water:', fahr_to_kelvin(32), 'K')
print('boiling point of water:', fahr_to_kelvin(212), 'K')
```

    freezing point of water: 273.15 K
    boiling point of water: 373.15 K


We’ve successfully called the function that we defined, and we have access to the value that we returned.

Now that we’ve seen how to turn Fahrenheit into Kelvin, it’s easy to turn Kelvin into Celsius:


```python
def kelvin_to_celsius(temp):
    return temp - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))

```

    absolute zero in Celsius: -273.15


What about converting Fahrenheit to Celsius? We could write out the formula, but we don’t need to. Instead, we can compose the two functions we have already created:


```python
def fahr_to_celsius(temp):
    return kelvin_to_celsius(fahr_to_kelvin(temp))

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))

```

    freezing point of water in Celsius: 0.0


This is our first taste of how larger programs are built: we define basic operations, then combine them in ever-larger chunks to get the effect we want.

Let us have a closer look at the syntax of a function in Python:
> ```python
> def <fun_name>(<argument(s)>):
>     <body>
> ```

#### The function name `<fun_name>`

  Is just another variable name, and the same restrictions apply: it can contain upper and lower case alphanumeric characters and underscores, but may not start with a numeral. Be aware that - since functions are also just variables - they cannot have the same name as another variable:



```python
f = 24
print(f)

def f(x):
    return 12
print(f) # The function has clobbered the variable name
```

    24
    <function f at 0x7f4d30f60488>


#### The arguments `<argument(s)>`
  Python is extremely flexible when it comes to how function arguments are handled and you are encouraged to read up on the details (Chapter 5 in [Effective Computation in Physics](https://ebookcentral.proquest.com/lib/ubfreiburg/reader.action?docID=3564547)). Here we will look only at functions with a known number of arguments of which some can be optional. As an example, consider the logarithm function


```python
def my_log(x, base):
    from numpy import log
    return log(x)/log(base)

print("log_10(100) =", my_log(100, 10))
print("log_2(1024) =", my_log(1024, 2))
```

    log_10(100) = 2.0
    log_2(1024) = 10.0


  It takes two arguments; the value we want to compute the logarithm of, and the logarithm base. In physical computations, however, it it very rare to use anything but the natural logarithm. So let us set $e$ as the _default value_ for `base`


```python
from numpy import e
def my_log(x, base=e):
    from numpy import log
    return log(x)/log(base)

print("log_10(100) =", my_log(100, 10))
print("log_2(1024) =", my_log(1024, 2))
print("ln(2.718281828459045) =", my_log(2.718281828459045))
```

    log_10(100) = 2.0
    log_2(1024) = 10.0
    ln(2.718281828459045) = 1.0


Thanks to the possibility to define default values, `my_log` can behave like two different functions when it is appropriate.

Functions can also have multiple arguments with default values, e.g. this function for the evaluation of second order polynomials:


```python
def poly2(x, a=1, b=1, c=1):
    return a*x**2 + b*x + c
```

Such optional arguments are called _keyword arguments_ since they can be named (by their keyword) in a function call:


```python
x0 = 12
poly2(x0)
```




    157




```python
poly2(x0, b=3.5)
```




    187.0



#### The body `<body>`

The function body is where the behaviour of function is determined and where return values are determined. It can contain zero or multiple return statements. Functions without return statement in their body always return the special variable `None`


```python
return_value = print("What is the return value of the print function?")
print(return_value)
```

    What is the return value of the print function?
    None


When a `return` statement is reached in a function body, execution of the function is immediately terminated


```python
from numpy import sin
def sin_inv_x(x):
    if x == 0:
        return 0.
        print(("Oh no, I won't get printed because "
               "I follow a return statement"))

    print("But I do when x != 0, I'm before the return statement")
    return sin(1/x)

print("sin_inv_x(0.) =", sin_inv_x(0.))
```

    sin_inv_x(0.) = 0.0



```python
print("sin_inv_x(12.) =", sin_inv_x(12.))
```

    But I do when x != 0, I'm before the return statement
    sin_inv_x(12.) = 0.0832369162003


#### Multiple return values

It is frequently useful for a function to return multiple result values. For example, consider a function that computes the kinetic and potential energy of a pendulum.


```python
from numpy import cos, pi
def pendulum(l, m, theta, omega, g=9.8):
    """ computes the mechanical energies for a pendulum of length l and 
        mass m at angular position theta (from the lower vertical) and 
        angular velocity omega.

        returns:
        e_kin, e_pot
    """
    e_kin = 0.5* m * (l*omega)**2
    e_pot = m * g * (1-cos(theta))*l
    return e_kin, e_pot

l = .5
m = 12
theta = pi/2
omega = -4

energies = pendulum(l, m, theta, omega)
energies
```




    (24.0, 58.799999999999997)



As you can see, the function returned something that looks like a list, but with paretheses (`()`) instead of brackets (`[]`). This container is called a tuple, and its content can be accessed by indexing (like for lists) or by _unpacking_:


```python
e_kin, e_pot = energies
print("unpacked: E_kin =", e_kin, "E_pot =", e_pot)
```

    unpacked: E_kin = 24.0 E_pot = 58.8


If you payed attention, you may have noticed that a bunch of explanatory text has been snuck into the function definition. This is called a docstring. Use the notebook help on the pendulum function. What do you see?

### Variable scope
Variable scope is a very important concept in every programming language, and understanding it is critical to the correct use of functions. The main concept is that the lifetime of variables that are defined within a function ends with the end of the function. Consider the following (admittedly silly) example:


```python
def scopefun(x):
    fun_var = 10*x
    print("I'm in the scope, I can see fun_var:", 1)
    return x

print(scopefun(42))
print("I'm out of scope, Python complains:", fun_var)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-03324d320755> in <module>()
          5 
          6 print(scopefun(42))
    ----> 7 print("I'm out of scope, Python complains:", fun_var)
    

    NameError: name 'fun_var' is not defined


    I'm in the scope, I can see fun_var: 1
    42


As you can see, variables that have been defined in a lower (indented) block are not visible from the outer block. This is called _local scope_ with respect to the function. If you are interested in a more solid understanding of scoping, particularly at the concept of non-local scoping, you are strongly encouraged to look at it in more detail in the book, or to discuss it with us.

### Recursion

Since functions have their own variable scope, they can also call themselves without the variables in their bodies clobbering each other. Usually, this leads to obvious and unsurprising disaster:

> ```python
> def my_dumb_recursion():
>     return my_dumb_recursion()
> 
> my_dumb_recursion()
> ```
> ```python
> <ipython-input-87-e13c9e990db6> in my_dumb_recursion()
>       1 def my_dumb_recursion():
> ----> 2     return my_dumb_recursion()
>       3 
>       4 my_dumb_recursion()
> 
> RuntimeError: maximum recursion depth exceeded
> ```

However, with a proper _termination clause_, recursion can be an elegant solution. Consider for instance the calculation of the factorial:


```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

factorial(5)
```




    120



The factorial is a good moment to mention what happens when you compute extremely large numerical values:


```python
factorial(171) # Yes, Python can handle large ints
```




    1241018070217667823424840524103103992616605577501693185388951803611996075221691752992751978120487585576464959501670387052809889858690710767331242032218484364310473577889968548278290754541561964852153468318044293239598173696899657235903947616152278558180061176365108428800000000000000000000000000000000000000000




```python
factorial(171.) # Floats run out of range at some point
```




    inf



#### Tasks
- Write a recursive function `fibonacci_recursive(n)` that calculates the $n$-th value of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) (we will assume the modern usage, starting at zero, and we start counting at zero).

- Write a function `fibonacci_loop(n)` that gives the same resultn as `fibonacci_recursive(n)`, but uses a loop instead of recursion

#### Discussion

Now that you've understood the basics of flow control and looping, you are ready to automate repetitive tasks on large data sets. With your knowledge of functions, you are able to split complex problems into simple (and therefore less buf-prone) sub-problems that you can join together.

This was the last exercise session about python in general, so if you have questions do not hesitate to contact us, because next week we will move on to efficient scientific computation.
