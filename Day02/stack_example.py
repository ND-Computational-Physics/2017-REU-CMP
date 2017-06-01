"""stack_example.py -- example of basic python

Modified 2017-06-01
"""

def c(x, y, z):
  total = x + y + z
  square = b(total)**2
  return square


def b(z):
  prod = a(z, z)
  print(z, prod)
  return prod


def a(x, y):
  x = x + 1
  return x * y


x = 1
y = x + 1
print('c =', c(x, y + 3, x + y))

