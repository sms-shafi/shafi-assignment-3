# Python Assignment 3

## Task 1: Factorial using function
---
# code
```
f = int(input('Enter the number: '))
# This line takes input from the user and convert it into an integer.

def factorial(f):
# This line defines a function named factorial that accepts a number f.

if f < 2:
# If f is less than 2 (i.e., 0 or 1), it returns 1 because:

0! = 1

1! = 1

return f * factorial(f - 1)

# The function keeps calling itself with f - 1

ans = factorial(f)

# Calls the factorial function with the user's input and stores the result in ans.

print('Factorial of', f, 'is:', ans)

# Displays the final result to the user.
```
# Sample output:
```
Enter the number: 5
Factorial of 5 is: 120
```
---
# Task 2 - Using the Math Module for Calculations
---
# code
```
import math

# This line imports Python's built-in math module, which provides mathematical functions.

a = float(input('Enter the number: '))

# This line takes input from the user and converts it into a float.

sqrt = math.sqrt(a)

# This calculates the square root of the number a using math.sqrt().

print('Square root:', sqrt)

# This prints the square root result.

log = math.log(a)

# This calculates the natural logarithm of the number a using math.log().

print('Logarithm:', log)

# This prints the logarithm result.

sine = math.sin(a)

# This calculates the sine of the number a using math.sin()

print('Sine:', sine)

# This prints the sine value.
```
# Sample output
```
Enter the number: 10
Square root: 3.1622776601683795
Logarithm: 2.302585092994046
Sine: -0.5440211108893698

