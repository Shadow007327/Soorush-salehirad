from utils import greet, add, multiply

name = input("Enter your name: ")
print(greet(name))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Sum:", add(x, y))
print("Product:", multiply(x, y))
