num=int(input("Enter any number:"))

def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)

result=factorial(num)
print(f'factorial of {num} is {result}')