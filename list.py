#list
fruits = ["apple", "ornage", "banana"]

print(fruits)

print(fruits[0])#accessing elements

fruits.append("grapes")#adding elements
print(fruits)

fruits.insert(1,"kiwi") #inserting elements at specific position
print(fruits)

#removing elements
fruits.remove("banana")
print(fruits)

print(len(fruits))#length of list

for fruit in fruits:  #iterating through list
    print(fruit)

#sorting the list
fruits.sort()
print(fruits)
#reversing the list
fruits.reverse()
print(fruits)

fruits.pop() #removes last element
print(fruits)

#slicing the list
print(fruits[1:3])
print(fruits[:1])

i =1
num = []
while i <= 5:
    num.append(i)
    i += 1
print(num)