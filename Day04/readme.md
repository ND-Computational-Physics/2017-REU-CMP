# Special Topics in Standard Python

Ben Rose

`brose3@nd.edu`

8 June 2017

!

# Goals

Review

1. Be able to use `git`'s `pull`, `add`, `commit`, and `push` commands
3. Be able to import and manipulate text or data from a file

New

5. Know what and `f-string` is and how to use it
4. Be able to describe how and when to use `range`, `enumerate`, and `zip`
6. Be able to use at least one special container form the `collections` class
7. Know how and when to use `assert`, `true`, and `except`

!

# Last Time

!

## File I/O

* For *prose* -- `f.read()`

* For *tabular data* -- `csv.read()`
    - This is the "best" because you will mostly be working with tabular data

!

# Better printing

```python
s1 = 'num: {}'.format(value)
s2 = 'num: {.4f}'.format(value)
```

!

## Better printing (Python 3.6)

```python
s1 = f'num: {value}'
s2 = f'num: {value:.4f}'
```

!

# More Lists and Looping

!

## Lists for math

- If a list contains *only* numbers, we can treat it as a vector:

`v = [0., 0., -9.81]`

- If a nested list contains *only* numbers, we can treat it as a matrix:

`m = [[0, 1], [1, 1]]`

- This is inefficient, but we don't know a better way yet...

!

## Lists expanded

Create a string from a list: `''.join(l)`

- everything in `l` **must be a string**

!

## List from a sequence

`.append()` is slow, so use this trick: 

- `l = [i**2 for i in range(10)]`
- This is extremely useful for a lot of different situations, like file
    processing:

```python
with open(filename, 'r') as f:
    data = [line.split() for line in f]
```

!

## Special for-looping functions

We already know about `range`

`enumerate` gets the value and index

`zip` "walks" through two lists at the same time

!

# Special collections

Aside from lists, tuples, sets, and dictionaries, there are a few special-case
collections we can use

```python
import collections

counter = collections.Counter()
colors = ['red', 'blue', 'red',
          'green', 'blue', 'blue']
for word in colors:
    counter[word] += 1

Isotope = collections.namedtuple(
    'Isotope', ['symbol', 'A', 'Z'])
he4 = Isotope('He4', 4, 2)
```

!

# Testing

`assert <condition>`

- stops program execution if condition is false

- useful for making sure we read in the right amount of data, for instance

!

## Protecting yourself

We place operations within `try`-blocks to safeguard ourselves from unwanted
operations (bad division, importing the wrong thing, requiring user input, etc.)

```python
try:
    x = 5 / 0
except Exception as e:
    print('divided by zero')
    x = 0.
```

* `Exception`  the most generic 
    - Will often use `TypeError` or `ZeroDivisionError`
* `e` now contains the Exception message, but not the Exception name.

!

# Practice Time!

- Practice with the handout
- Import `nothwind.txt` then separate by word
    + Try to count how many times each word appears
- Calculate the average sunspot form `sunspots.txt` 
    + Can you count the days who's number of sunspots fell with an arbitrary range?

Read Newman Ch 3 - Intro to Matplotlib & I will update the External Resources section with a few Numpy articles.

* Office Hours: Tuesdays at 3pm, NSH 186
* And Class at 4:30