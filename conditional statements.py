#if loop

age = 24
if age < 18:
    print("you are a minor")

#if else loop

if age <18:
    print("you cant vote")
else:
    print("you can vote")


#if elif else loop

mark = int(input("enter your mark: "))

if mark >= 90:
    print("grade A")
elif mark >= 75:
    print("grade B")        
elif mark >= 50:
    print("grade C")
else:
    print("grade D")

#nested if


num = int(input("enter a number: "))
if num >= 0:
    if num % 2 == 0:
        print("the number is positive even")
    else:
        print("the number is positive odd")

else:
    print("the number is negative")

    