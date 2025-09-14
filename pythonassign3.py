def factorial(n) :
    if n < 2 :
        return (1)
    else :
        return (n * factorial(n - 1))
    
y = int(input("Enter a number :"))
x = factorial(y) 

print(f"The factorial of {y} is : {x}") 
