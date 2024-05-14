---
layout: default
title: "Introduction to Python"
parent: Python
date: 2024-05-14
categories: python
author: Lars Pastewka
nav_order: 2
---

# Introduction to Python

## Learning goals
- Learn the basics of the Python programming language

## Introduction to Python

In this section, we explain the basics of Python programming with the help of examples. You are expected to follow along in the notebook you have created in the previous section.

In a code cell, type the following, and run the cell


```python
print("Hello, World")
```

    Hello, World


The notebook has read the content of the cell, interpreted it as Python code, executed it and printed the response below the cell.

To get help about any Python object, follow it with two question marks,


```python
print??
```

or use the `help()` function


```python
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    


Do not worry about the terms 'Python object' and 'function' yet. Their precise meaning will be clarified in future exercise sessions.

### Comments
It is often useful to add explanatory text to your code. This text should be skipped by the Python interpreter. Python uses the &#35; character for this and everything between the &#35; character and the end of the line will be ignored:


```python
print("Hello, ") # print("World")
```

    Hello, 


When you run this cell, only the first print function is executed, because the second one is treated as a comment by the Python interpreter. Use comments to document complicated or non-obvious parts of code.

### Variables
In Python, a variable consists of an object and its name. The equal sign (=) is used to assign an object to a name. Variable names can be upper- and lowercase letters, digits, and underscores but the cannot start with a digit. Here, we create a bunch of variables called `height`, `width`, etc.


```python
# Properties of a book with A4 pages
height = 0.21022 # in [m] <- because units are not obvious
width = 0.29730 # in [m]
nb_pages = 434
title = "The life of Edgar"
```

Variables can be used to define new variables. Let us compute the surface area of the the book pages.


```python
area = nb_pages * height * width
print("area of the book '", title, "' is", area)
```

    area of the book ' The life of Edgar ' is 27.124308204


All Python variables have a _type_ which defines how they can be used. For instance integer numbers (`int` in Python) or floating point numbers (`float`) can be used for mathematical operations and strings (`str`) can be used to manipulate pieces of text. If you are not sure what type a given variable has, check using the function `type`.


```python
print(type(area))
print(type(nb_pages))
print(type(title))
```

    <class 'float'>
    <class 'int'>
    <class 'str'>


Using variables with the wrong type in an operation fails.


```python
title + area
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-486d5e63581f> in <module>()
    ----> 1 title + area
    

    TypeError: Can't convert 'float' object to str implicitly


The Python interpreter informs you that a `TypeError` has occurred and where it has occurred. In Python parlance, _a TypeError has been raised_.

Python is _dynamically typed_. This means that a variable can change its type when its object changes. The following is valid in Python.


```python
x = height
print(type(x))
x = nb_pages
print(type(x))
x = title
print((type(x)))
```

    <class 'float'>
    <class 'int'>
    <class 'str'>


There are a few predefined special variables in Python; `True`, `False`, `None` and others. They always exist and cannot be changed.

`None` is the Python variable that denotes that no value is given.

#### Boolean variables

Boolean variables are used to represent the truth of a statement. They can be assigned directly using the special variables `True` and `False`.


```python
abe_lincoln_lies = False
pinocchio_lies = True
```

Alteratively, the truth value can be the result of a Python expression. In general, if the value of a variable is non-zero (in the case of strings or containers: non-empty), the expression is considered `True`, else `False`.


```python
print(bool(area))
print(bool(0))
```

    True
    False


The results of comparisons are also boolean.


```python
print(height == width) # equality comparison
print(height < width)  # greater-than comparison
print(height != width)  # inequality comparison
```

    False
    True
    True


### Modules
Python comes with a large library of modules you can import to access additional variables and functions. The modules we will use the most in this class are
+ *numpy*, the fundamental package for scientific computing with Python.
+ *scipy*, collection of software for mathematics, science, and engineering
+ *matplotlib*, a 2D plotting library

Modules can be imported with the help of the `import` statement in different ways. The simplest form is just `import <module_name>`.


```python
import numpy
```

After the import, all of `numpy`'s variables are accessible as `numpy.<var>`,


```python
print(numpy.pi)
print(numpy.sin(numpy.pi/2))
```

    3.141592653589793
    1.0


It can be annoying to always type `<module_name>.<variable_name>`. You can make your life easier by using selective imports, or aliased imports. In selective imports, you import only the variables you are interested in.


```python
from numpy import log, e
print(log(e))
```

    1.0


In aliased imports, you give a module a shorter name.


```python
import numpy as np
np.cos(np.pi)
```




    -1.0



Finally, selective and aliased import can also be combined.


```python
from numpy import pi as PI
print(PI)
```

    3.141592653589793


### Containers

So far, we have only looked at simple, single variables. Very often, however, it is convenient to to group variables together and handle them as a single entity. Here, we will look at two container types in particular, the `list` and the `dictionary`.

#### Lists

A `list` is a one-dimensional, ordered container of Python objects. The syntax for creating a list is square brackets ([])


```python
my_list = [6, 24.5, True, "Hakuna Matata"]
print(my_list)
```

    [6, 24.5, True, 'Hakuna Matata']


The variables in a list are called its items and can be any python object, even another list.


```python
my_new_list = [1, PI, my_list, None]
print(my_new_list)
```

    [1, 3.141592653589793, [6, 24.5, True, 'Hakuna Matata'], None]


Lists can be extended using the `extend` method, or single elements can be appended to them using the `append` method.


```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)

# Note the difference
my_list = [1, 2, 3]
my_list.append([4, 5, 6])
print(my_list)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, [4, 5, 6]]
    [1, 2, 3, 4]


##### Indexing

Frequently, you will wish to access individual elements or a part of a list. In Python, this is done using square brackets ([]).


```python
my_list = [1, 2, 3, 4, 5, 6, 8, 9]
print(my_list[0])
print(my_list[1])
```

    1
    2


Note that the list indices start at zero, i,e, the index of the first list item is `0`. You can also a index a list backwards using negative indices.


```python
print(my_list[-1])
print(my_list[-2])
```

    9
    8


If you wish to access multiple items (a _slice_ of the list), you define a range of indices by providing a start and a stop index, separated by a colon (:).


```python
print(my_list[2:5])
print(my_list[5])
```

    [3, 4, 5]
    6


Note that the item `my_list[5]` is not part of the selected sub-list. A slice is defined to be inclusive at the start index and exclusive an the stop index of the slice.

If you omit either the start or the stop index, Python chooses sensible default values.


```python
print(my_list[:3])   # the first three items
print(my_list[-2:])  # the last 2 items
print(my_list[:])    # all items
```

    [1, 2, 3]
    [8, 9]
    [1, 2, 3, 4, 5, 6, 8, 9]


Furthermore, a slice can also have a third parameter: the stride. This can be useful when you wish to look at every third item, for instance.


```python
print(my_list[0:-1:3])
```

    [1, 4, 8]


Just like indices, the stride can also be a negative value. A simple way to reverse a list is to use a stride of -1.


```python
print(my_list[::-1])
```

    [9, 8, 6, 5, 4, 3, 2, 1]


In addition to item access, indices can also be used to change or remove items to or from the list.


```python
print(my_list)
my_list[2] = "A"
print(my_list)
my_list[3:5] = ['x', True]
print(my_list)
del my_list[5]
print(my_list)
```

    [1, 2, 3, 4, 5, 6, 8, 9]
    [1, 2, 'A', 4, 5, 6, 8, 9]
    [1, 2, 'A', 'x', True, 6, 8, 9]
    [1, 2, 'A', 'x', True, 8, 9]


#### Dictionaries

A dictionary (`dict`) is an unordered collection of key/value pairs. This means that in a dictionary, every key object is _associated_ with a value object. Keys must be unique within a dictionary, but several keys can refer to the same value.

The syntax for creating a dictionary is curly braces ({}) surrounding `key: value` pairs


```python
my_dict = {"height": height, "width": width, "title": title}
print(my_dict)
```

    {'width': 0.2973, 'height': 0.21022, 'title': 'The life of Edgar'}


You can access value objects in a dictionary using their key as index


```python
print(my_dict["title"])
```

    The life of Edgar


You can also modify the content of a dict through the keys


```python
my_dict["weight"] = 379.8e-3 # in kg
my_dict["nb_pages"] = nb_pages
del my_dict["weight"]
print(my_dict)
```

    {'width': 0.2973, 'nb_pages': 434, 'height': 0.21022, 'title': 'The life of Edgar'}


If you try to access a non-existing key, a `KeyError` is raised


```python
del my_dict["hakuna matata"]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-31-b85b46565a4a> in <module>()
    ----> 1 del my_dict["hakuna matata"]
    

    KeyError: 'hakuna matata'



```python
print(my_dict[24])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-32-40f0f7df6cb7> in <module>()
    ----> 1 print(my_dict[24])
    

    KeyError: 24


Python is telling you that the keys `'hakuna matata'` and `24` are not present in the dictionary.

Save the notebook.

#### Discussion

You should have learned about variables and types in Python and seen that Python is a dynamically typed language, in which variables can change their type. 

You understand how to import variables you need from external modules, and without knowing exactly what a Python function is, you have used the `print`, `type`, `numpy.cos`, and several other functions.

You know how to create list and dictionary containers and can manipulate them using indices.

This class will teach just enough Python for you to get through the numerical contact mechanics exercises. If you are interested in getting a more complete foundation in how to go about scientific numerical calculations, the book [Effective Computation in Physics](https://ebookcentral.proquest.com/lib/ubfreiburg/reader.action?docID=3564547) is an excellent resource, and do not hesitate to contact us with any questions you might have.
