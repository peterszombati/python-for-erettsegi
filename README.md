# Python for erettsegi
https://www.python.org

## File read
```py
f = open('filename.txt','r')
content = f.read()
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
print(content)
content = content.split('\n')
print(content[1])
print(array)
array.append(101)
print(array)
```
## If statement
```py
x = True
y = False
if (x):
	print('x is True')
if (not y):
	print('y is False')
if (y == False):
	print('y is False')
elif (x):
	print('x and y are True')
else:
	print('y is True but x is not')
if (x == True and y == True):
	print('x and y are True')
```

## For
```py
array = [5,4,3,2,1]
for i in range(len(array)):
	print(array[i])
for element in array:
	print(element)
```
## While
```py
i = 0
while(i < 10):
	print(i)
	i+=1
```
## Input
```py
s = input()
print(s)
s = s.split(" ")
print(s[0])
```
## Function
```py
def hello(name):
	print('Hello '+name)
hello('World')
```
## Change variable type
```py
v = "8"
print(v + v)

v = int(v)
print(v + v)

v = str(v)
print(v + v)

v = "3.5"
v = float(v)
print(v * 2)
```
## Random number
```py
from random import randint
a = 0
b = 10
print(randint(a, b))
```
## Exchange variable
```py
a = 1
b = 0
print(a)
a,b = b,a
print(a)
```
## Sorting
```py
numbers = [5, 2, 3, 1, 4]
numbers = sorted(numbers)
print(numbers)

numbers = sorted(numbers, reverse=True)
print(numbers)

def test(a):
	return a[0]

numbers = [[5,'A'], [2,'B'], [3,'C'], [1,'D'], [4,'E']]
numbers = sorted(numbers, key=test, reverse=True)
print(numbers)
```
## Assignment Operators
| Operator | Description | Example |
| ------------- |:-------------:| -----:|
| = | Assigns values from right side operands to left side operand | c = a + b assigns value of a + b into c |
| += Add AND | It adds right operand to the left operand and assign the result to left operand | c += a is equivalent to c = c + a |
| -= Subtract AND | It subtracts right operand from the left operand and assign the result to left operand | c -= a is equivalent to c = c - a |
| *= Multiply AND | It multiplies right operand with the left operand and assign the result to left operand | c *= a is equivalent to c = c * a |
| /= Divide AND | It divides left operand with the right operand and assign the result to left operand | c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a |
| %= Modulus AND | It takes modulus using two operands and assign the result to left operand | c %= a is equivalent to c = c % a |
| **= Exponent AND | Performs exponential (power) calculation on operators and assign value to the left operand | c **= a is equivalent to c = c ** a |
| //= Floor Division | It performs floor division on operators and assign value to the left operand | c //= a is equivalent to c = c // a |
