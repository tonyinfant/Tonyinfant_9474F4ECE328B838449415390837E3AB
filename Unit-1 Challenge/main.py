def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

num=int(input("Enter the value:"))
fact=factorial(num)
print("Factorial of",num,"is",fact)