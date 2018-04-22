# Python for erettsegi
https://www.python.org

## File read
```py
f = open('filename.txt','r')
f = f.read()
f.close()
```
## File write
```py
f = open('filename.txt', 'w')
f.write(content)
f.close()
```
## Array
```py
array = [0,[8,9],2,3,4,5]
print(array[0])
print(array[1][1])

content = 'hello\nworld'
content = content.split('\n')
print(content)
print(content[1])
```
## If statement
```py
x = True
y = False
if (x):
	print('x is True')
if (y):
	print('y is True')
elif (x):
	print('x is True but y is not')
else:
	print('x and y are False')
```
## Operators
```py
number = 49
print(number)
number += 2
print(number)
number = 2 ** 3 # = 2^3
print(number)

hi = 'Hello'
hi += ' World'
print(hi)

if(number == 8 or number < 0):
	print(number)
```
## For
```py
array = [5,4,3,2,1]
for i in range(len(array)):
	print(array[i])
```
## Input
```py
s = input()
s = s.split(" ")
print(s[0])
```
## Function
```py
def hello(name):
	print('Hello '+name)
hello('World')
```
