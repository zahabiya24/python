'''# Program to create List, Tuple and Dictionary
#write a program to perform data types using operations (list tuple dic)
# Creating a List
my_list = [10, 20, 30, 40, 50]

# Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)

# Creating a Dictionary
my_dict = {
    "Name": "Zahabiya",
    "Age": 20,
    "Course": "Python"
}

# Display the data
print("List:", my_list)
print("Tuple:", my_tuple)
print("Dictionary:", my_dict)

#operations:-add new value,remove value, list size and ascending value.
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Add an element
my_list.append(60)
print("Append:", my_list) 

# Insert an element
my_list.insert(2, 25)
print("Insert:", my_list)

# Remove an element
my_list.remove(40)
print("Remove:", my_list)

# Access an element
print("Element:", my_list[0])

# Sort the list
my_list.sort()
print("Ascending Order:", my_list)


#in dic key and value different show:
print("Keys:",my_dict.keys())
print("Values:",my_dict.values())
'''


n = int(input("Enter n: "))

for i in range(0, n):
    for j in range(0, n):
        print(i, j)
