'''enumerate_and_zip.py -- explainer for enumerate and zip functions

Ben Rose
2017-06-08
Python3.6
'''

#set up lists
a = [4, 5, 6, 7 , 8]
name = ['Isabel', 'Liam', 'Jade', 'Mia', 'Ethan']

#show how `enumerate` works
print('Example of enumerate()')
for i, num in enumerate(a):
    print(i, num)

#Loop through two lists together with `enumerate`
print('\nLooping through two lists')    #Adds a blank line for a clean output
for i, age in enumerate(a):
    print(f'{name[i]} is {age} years old.')

#Loop through two lists with zip
print('\nLooping through two lists is better with zip')
for b in zip(name, a):
    print(f'{b[0]} is {b[1]} years old.')