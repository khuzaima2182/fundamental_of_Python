def factorial(n):
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)
num = input("Enter a number = ")
print("Factorial = ",factorial(int(num)))