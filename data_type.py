#string data type
car = "BMW"
print(car)
#string indexing
print(car[0])
#string concate
first_name = "rush"
last_name = "mia"
print(first_name + last_name)
print(first_name + " " + last_name)
#boolean data type
is_student = True
print(is_student)
print(type(is_student))

x = 8
y = 10
print(x>y)
print(x<y)
print(x==y)
#number data type
#int (Integer) Stores whole numbers (no decimal)
years = 2026
print(years)
#float (Floating Point) stores numbers with decimal points
pi = 3.1416
print(pi)
#complex data type
z = 2 + 3j
print(z)
#Collection Data Types
#list data tyoe
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
#tupple data type
colors = ("red", "green", "blue")
print(colors)
print(colors[1])
#set data type
numbers = {1,2,3,4,4,5}
print(numbers)
#dictionary data type
person = {"name": "jonayed",
          "age": 25,
          "city": "Dhaka"}
print(person)
print(person["name"])
#binary data type image file,audio file,video file
list = [1,211,21,17,90]
b = bytes(list)
print(type(b))
print(b)

#bitary
list1 = [1,211,21,17,90]
b1 = bytearray(list1)
print(type(b1))
print(b1)
text = "Hello"
ba = bytearray(text, "utf-8")
print(ba)
b1[0] = 100
print(b1)

#none data type
x = None
print(x)



