#input 

name = input("enter your name:")
print("your name is:", name)
print(type(name))

age =int(input("enter your age:"))
print("your age is:", age)

#type casting

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
sum = num1 + num2
print("the sum is:", sum)
print("the type of sum is:", type(sum))
sum_float = float(sum)
print("the sum in float is:", sum_float)
