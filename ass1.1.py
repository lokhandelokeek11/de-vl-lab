# basics of list
print("Basics of the list: ")
list1 = [1,4,5,6]
list2 = ["red","green"]
print(list1)
print(list2)
print()

# list index
print("Understanding about list indexing: ")
colleges = ["pccoe", "coep", "vit", "vjti"]
print(colleges[3])
print(colleges[2])
print(colleges[0])
print()

#add list items
#1. append - add data at the end of the list
print("Adding List items - Append() ")
colors = ["violet","red", "blue"]
colors.append("reddish blue")
print(colors)
print()

#2. extend - add list to list
print("Adding list items - Extend() ")
sample_cars = ["bmw", "audi", "range rover"]
sample_colors = ["cameron green", "blue", "red"]
sample_cars.extend(sample_colors)
print (sample_cars)
print()

#3. insert 
print("Adding list items - Inserting() ")
animals = ["dog", "cat", "rhino", "hippo"]
animals.insert(3, "giraffe")
print(animals)

#4. removing list items (pop) - removes last element of the list
print("Removing list items - Pop() ")
car_companies = ["mahindra", "tata", "suzuki"]
car_companies.pop()
print(car_companies)

#5. removing list items (remove) - removes any item from the list
print("Removing list items - remove() ")
students = ["aditya", "swayam", "kaustubh", "lokeek"]
students.remove("aditya")
print(students)

#6. removing list items (del) - removes any list item from specific location
print("Removing list items - del()")
apps = ["insta", "facebook", "google", "twitter"]
del apps[0]
print(apps)

#7. removing list items(clear)- clears all the list items

things = ["pen", "book", "eraser"]
things.clear()
print(things)

#8. change list items (add) 

name = ["Sakshi", "Rohini","Rishi", "Rohan","ayush","harshal"]
name[2:5] = ["Zeeshan","Khush"]
print(name)

#9. List Method - sorting list (ascending order)

eg_color = ["violet", "red", "yellow"]
eg_color.sort()
print(eg_color)

num = [1,89,77,54,6,19]
num.sort()
print(num)

# sorting list (descending order)
number = [56,78,99,14,67]
number.sort(reverse=True)
print(number)

#10. List Method - reverse (this method reverses the order)

divison = ["a", "c", "h", "j"]
divison.reverse()
print(divison)

#11. List Method - index (this method tells you the index of the string or num)

smartphone_brands = ["samsung", "apple", "xiomi", "micromax", "motorola"]
print(smartphone_brands.index("motorola"))

#12. List Method - count (this method gives us the count of the no of items in the list)
colorr = ["blue", "white", "green","blue","violet"]
print(colorr.count("blue"))

num_ber = [5,6,7,3,7,9,7,0,5,7]
print(colorr.count(7))

#13.List Method - copy (this method copies the list)
names = ["lokeek","rishi","santosh","kamlesh"]
newlist = names.copy()
print(names)
print(newlist)

#14. List Slicing 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing with Start and End Indices

print(numbers[2:6]) 
   
# Assigning Values to a Slice:
numbers[3:6] = [100, 200, 300]
print(numbers)  

# Deleting Elements Using Slicing

del numbers[4:7]
print(numbers)  

# 15. Concatinating list 

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
combined_list = list_1 + list2
print(combined_list)  

#16. Multiplying List 
repeated_list = [18] * 5
print(repeated_list) 

#17. Finding Length

cars = ["Suzuki", "Mercedez", "bajaj", "mahindra"]
print(len(cars)) 
