color = ("red", "green", "blue")
#print 
print(color[0])

#length
print(len(color))

#iterating through tuple

for i in color:
    print(i)

#adding elements - tuples are immutable, so we cannot add elements directly
#we can convert tuple to list, add elements and convert back to tuple   
color_list = list(color)
color_list.append("yellow") 
color = tuple(color_list)
print(color)
 #removing elements - tuples are immutable, so we cannot remove elements directly
#we can convert tuple to list, remove elements and convert back to tuple    
color_list = list(color)
color_list.remove("green")
color = tuple(color_list)
print(color)
#slicing
print(color[1:3])
print(color[:2])
#tuples are immutable - we cannot change elements directly
#but we can convert tuple to list, change elements and convert back to tuple

color_list = list(color)
color_list[0] = "purple"
color = tuple(color_list)
print(color)
#reverse indexing
print(color[-1]) #last element
print(color[-2]) #second last element
print(color[:-1])

#sorting - tuples are immutable, so we cannot sort directly
color_list = list(color)
color_list.sort()
color = tuple(color_list)
print(color)
#reversing - tuples are immutable, so we cannot reverse directly
color_list = list(color)
color_list.reverse()
color = tuple(color_list)
print(color)

