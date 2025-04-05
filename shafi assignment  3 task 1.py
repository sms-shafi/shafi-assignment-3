f=int(input('Enter the number: '))
def factorial(f):
    if f<2:
        return 1
    else:
        return f * (factorial(f-1))
ans = factorial(f)
print('Factorial of',f,'is :',ans)