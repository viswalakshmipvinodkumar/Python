#key value pair

student ={
    "name" :"Lakshmi",
    "age" :21,
    "course" :"Python"
    
}
print(student)

print(student["name"]) #accessing value using key
student["age"] = 23 #updating value
print(student["age"])

student["city"] = "bangalore" #adding new key value pair
print(student)

student.__setitem__("phone", "1234567890") #adding new key value pair using setitem
print(student)
del student["course"] #removing key value pair
print(student)

#looping through dictionary

for k in student:
    print(k, ":", student[k])