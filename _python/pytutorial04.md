---
layout: default
title: "numpy"
parent: Python
date: 2024-05-14
categories: python
author: Lars Pastewka
nav_order: 4
---

# *numpy*: Efficient numerical computation

## Learning goals:
* Understand why to use specialized arrays for numerics
* Common numerical operations on arrays
  * Broadcasting rules
  * Slicing revisited
  * Linear algebra

## Computation and Python

Python's great flexibility and ease of use make it a great general purpose language. Because it is an interpreted language (not a compiled language, like for instance C++ or Fortran) with a flexible type system, it is very easy to write code quickly.

However, this flexibility comes at a cost that can be prohibitive when it comes to computations. The following video summarizes some aspects of scientific computing and motivates the use of Python.

<center>
<iframe src="https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=d0b8c5d5-6cde-4c65-a1c0-ab9a00e3d644&autoplay=false&offerviewer=false&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</center>

### Motivating the use of NumPy

The Python module NumPy defines a new type of object - the so-called _array_ -  that allows us to trade Python's flexibility and slow speed for for the constraints and efficiency of compiled, closer-to-the-metal languages when dealing with numeric data.

The following simple example illustrates the improvement that can typically be expected when using NumPy. Given a set of data $$ t = (0, 0.001, 0.002, \cdots, 0.999),$$ we compute $y = \sin(\omega\,t + \varphi)$, first using the standard Python tools - comprehensions and the `math` module - then using the NumPy module.

>```python
>import math
>import numpy as np
>omega = 24.5
>phi = np.pi/6
>nb_pts = 1000
>```
>
>
>```python
>%%timeit
># Using just standard Python libraries
>t = (i/nb_pts for i in range(nb_pts))
>y = [math.sin(t_val*omega + phi) for t_val in t]
>```
>
>```
>    1000 loops, best of 3: 301 µs per loop
>```
>
>
>```python
>%%timeit
># Using Numpy arrays
>t = np.arange(nb_pts)/nb_pts
>y = np.sin(t*omega + phi)
>```
>
>```
>    10000 loops, best of 3: 34.8 µs per loop
>```

The `%%timeit` statement is a notebook-function that evaluates the time it takes to evaluate the cell. As you can see, the equvalent computation is about _one order of magnitude faster_ when using numpy arrays. At the end of today's session, you should be able to know when and how to use them to accelerate your numerical calculations.

The basic construct that lets NumPy perform so well is the `numpy.array`, a homogeneous array of data of a single type. Because all data points in such an array are of the same type and they sit in memory one after the other without jumps or interruptions (both of which are not guaranteed for Python `list`s), NumPy can make many optimisations when it comes to operations that involve looping through those sets.

NumPy is a vast module, and we will only be able to touch the surface. You are expected to learn a bit on your own using the [NumPy documentation](http://www.numpy.org/) and the notebook help when you get stuck. Please also watch the following video giving a brief introduction into numpy.

<center>
<iframe src="https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=0fe8b95c-0783-4eb9-9a1f-ab9a00eb6203&autoplay=false&offerviewer=false&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</center>

### Array creation

There are a few functions that allow you to create arrays. The most important ones are `np.array()`, `np.linspace()`, `np.arange()`, `np.zeros()` and `np.ones()`.


```python
import numpy as np
# use array when you aready have the data in some form:
a = np.array([12, 24.5, 15.3])
a
```




    array([12. , 24.5, 15.3])




```python
# arrays can have more than 1 dimension
b = np.array([[1, 2, 7], [8, 24, -6]])
b
```




    array([[ 1,  2,  7],
           [ 8, 24, -6]])




```python
# use linspace and arange to generate spaced grid points
print(np.linspace(5, 7.5, 6))
print(np.arange(0, 1., .1))
```

    [5.  5.5 6.  6.5 7.  7.5]
    [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]



```python
# use zeros and ones to initiate an array with uniform values
print(np.zeros(4))
print(np.ones((3, 2)))
```

    [0. 0. 0. 0.]
    [[1. 1.]
     [1. 1.]
     [1. 1.]]


NumPy arrays have a few attributes that are important to know:

Attribute | Description
----------|------------------------------------------------------------------
`dtype`   | Type information abouth the data
`shape`   | Tuple of ints that represent the number of entries along any axis

If you have paid attention, you will have noticed that array `a` contains floating point values, but that array `b` contains only integers. This data type (`dtype`) is the most important attribute. It determines the size of the array and the operations it allows to be applied to the data points. In numerical computations, you will mostly use arrays of floating point values.


```python
print("dtype of a is", a.dtype)
print("dtype of b is", b.dtype)
```

    dtype of a is float64
    dtype of b is int64


Pay attention to the data type; creating arrays with the wrong `dtype` can lead to surprising and difficult-to-find bugs


```python
int_arr = np.array([1, 1, 2])
print(int_arr)
```

    [1 1 2]



```python
int_arr[2] = 5.7
print(int_arr)
```

    [1 1 5]


When you try to assign a floating point value to an integer array, it will be truncated. It is prudent choose the data type of an array explicitely when in doubt:


```python
float_arr = np.array([1, 1, 2], dtype=float)
float_arr[2] = 5.7
print(float_arr)
```

    [1.  1.  5.7]


The `shape` attribute tells you the size of the array in each of its dimensions


```python
a.shape # one-dimensional array: has only a length
```




    (3,)




```python
b.shape # two-dimensioal array, has 3 columns and 2 rows
```




    (2, 3)



#### Tasks
- Use the notebook help to understand what the functions `np.array()`, `np.linspace()`, `np.arange()`, `np.zeros()` and `np.ones() do.
- The help on `np.linspace()` mentions an efficient way to generate data that is uniformly distributed in log space. Use it to generate an array that contains 12 logarithmically distributed data points between 1 and 500

### Indexing

NumPy arrays can be indexed similarly to lists and strings:


```python
a = np.arange(5)
a
```




    array([0, 1, 2, 3, 4])




```python
a[::-1]
```




    array([4, 3, 2, 1, 0])




```python
a[1:4]
```




    array([1, 2, 3])




```python
a[::2]
```




    array([0, 2, 4])



However, NumPy arrays can have multiple dimensions, and so can their indices:


```python
a = np.arange(9)
a.shape = (3, 3)
a
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
a[1:, :]
```




    array([[3, 4, 5],
           [6, 7, 8]])




```python
a[:, ::-1]
```




    array([[2, 1, 0],
           [5, 4, 3],
           [8, 7, 6]])



An important, and extremely useful feature of indexed arrays (so-called _slices_ of arrays) is that they are not a copy of the original data, but only a _view_ on it. The following example clarifies this:


```python
# Create an array
a = np.ones((4, 4))
print(a)
```

    [[1. 1. 1. 1.]
     [1. 1. 1. 1.]
     [1. 1. 1. 1.]
     [1. 1. 1. 1.]]



```python
# slice it to obtain a view on a sub-region
b = a[:2, 1:3]
print(b)
```

    [[1. 1.]
     [1. 1.]]



```python
# modify the content of the slice
b += 12
print(b)
```

    [[13. 13.]
     [13. 13.]]



```python
# because the slice is not a copy, but a view on the
# original data, the array a has also been modified
print(a)
```

    [[ 1. 13. 13.  1.]
     [ 1. 13. 13.  1.]
     [ 1.  1.  1.  1.]
     [ 1.  1.  1.  1.]]


### Arithmetic and Broadcasting

Operations on arrays are performed in an _element-wise_ fashion. Consider the following examples:


```python
a = np.arange(4, dtype=float)
a
```




    array([0., 1., 2., 3.])




```python
a+2
```




    array([2., 3., 4., 5.])




```python
a*5
```




    array([ 0.,  5., 10., 15.])




```python
a + np.array([12, 5, .3, 5])
```




    array([12. ,  6. ,  2.3,  8. ])




```python
a ** 2 + 2*a
```




    array([ 0.,  3.,  8., 15.])



The concept is trivial for the case when we mix scalars and arrays or arrays of the same shape. Element-wise operations are however not limited to this case: NumPy can _broadcast_ arrays together, if they have compatible shapes. The rules are (from the [NumPy doc](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html))

> When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions, and works its way forward. Two dimensions are compatible when
>
>    1. they are equal, or
>    2. one of them is 1

Furthermore,

> Arrays do not need to have the same number of dimensions. For example, if you have a 256x256x3 array of RGB values, and you want to scale each color in the image by a different value, you can multiply the image by a one-dimensional array with 3 values. Lining up the sizes of the trailing axes of these arrays according to the broadcast rules, shows that they are compatible:
>    ```
>    Image  (3d array): 256 x 256 x 3
>    Scale  (1d array):             3
>    Result (3d array): 256 x 256 x 3
>    ```



```python
a = np.arange(4)
a.shape = (2, 2)
a
```




    array([[0, 1],
           [2, 3]])




```python
b = np.array([[8], [9]])
a + b

```




    array([[ 8,  9],
           [11, 12]])



#### Tasks
- Explain what happened here. Ask us if you have questions.
- Create an array that has the shape and pattern of a chess board with zeros for black and ones for white squares (the A-1 square of a chess board is black)
- Using what you learned about broadcasting rules, complete the code snippet
    > ```python
    > a = np.arange(4)
    > b = 10*a
    > b.shape = ?????
    > print(a+b)
    > ```
    so that the result is
    > ```
    > [[ 0  1  2  3]
    >  [10 11 12 13]
    >  [20 21 22 23]
    >  [30 31 32 33]]
    > ```
    
<center>
<iframe src="https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=0fd150f2-1321-4f48-bd1c-aba100da23c8&autoplay=false&offerviewer=false&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</center>

### Basic Linear Algebra

Arrays can be used to represent vectors and matrices and NumPy provides functions to perform basic linear algebra operations on them (see [Numpy doc](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html)). For instance, matrix multiplication and matrix-vector multiplications use the function `np.dot()`:


```python
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
np.dot(a, b)
```




    array([[4, 1],
           [2, 2]])




```python
c = np.array([1, 8])
np.dot(b, c)
```




    array([12, 18])



The inverse of matrix can be computed with `np.linalg.inv()`


```python
np.linalg.inv(b)
```




    array([[ 0.33333333, -0.16666667],
           [-0.33333333,  0.66666667]])



Two-dimensional matrices can also conveniently by transposed


```python
b
```




    array([[4, 1],
           [2, 2]])




```python
b.T
```




    array([[4, 2],
           [1, 2]])



Or eigenvalues and -vectors are convently computed using `np.linalg.eig`


```python
values, vectors = np.linalg.eig(b)
values
```




    array([4.73205081, 1.26794919])




```python
vectors
```




    array([[ 0.80689822, -0.34372377],
           [ 0.59069049,  0.9390708 ]])



#### Tasks
- Solve the following system of equations using NumPy's linear algebra
    
$$
    \begin{align}
        12\,x + 16\,y &= 4\\
       8\, x + 12\, y &=0
    \end{align}
    $$

- Read about `np.linalg.solve` and use it to solve the system in a more efficient and compact way.
- Use NumPy's `linalg` module to
    1. find the principal stresses, 
    1. find the direction of the smallest principal stress.
    
    Given a stress tensor

$$
    \boldsymbol \sigma = 
    \left[
        \begin{array}{cc}
          15 & -35 \\
          -35 & 15
        \end{array}
    \right]\ \mathrm{MPa}
    $$

    
