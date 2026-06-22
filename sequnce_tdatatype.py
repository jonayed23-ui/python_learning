#sequence type datatype[list,tuple,range]
#list
fruits = ["apple", "banana", "orange","grape"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
fruits[1] = "kiwi"
print(fruits)

#List  Methods

num = [1,2,3,55,21,56]
num.append(100)
print(num)

num.insert(3,10)
print(num)

num.remove(3)
print(num)

popped = num.pop()     
print(popped)           
print(num)             

popped_index = num.pop(2)   
print(popped_index) 

num.sort()
print(num)

num.reverse()
print(num)

print(num.count(55))
print(num.index(21))

num.clear()
print(num)

#List in Mixed Data and Nested List

mixed = [1, "hello", 3.214, [1,2,3], True]
print(mixed)
print(mixed[3])
print(mixed[3][1]) #nested list

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]    # 2D list, matrix 

print(matrix[1][2])     # row 1, column 2 -> output: 6


#tuple data type  Immutable Ordered Sequence

my_tuple = (1, "rushmia", 3.14, [1,2,3], True)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:4])
my_tuple[1] = "jonayed"  #This will raise a TypeError since tuples are immutable

#Tuple Packing এবং Unpacking

#packing
coordinates = 10, 20, 30    
print(type(coordinates))    

# Unpacking 
x, y, z = coordinates
print(x)    # output: 10
print(y)    # output: 20
print(z)    # output: 30

# Swap—  use of Tuple unpacking 
a = 5
b = 10
a,b = b,a
print(a,b)

 #String (str) — Text Sequence immutable

name = "samantha"
print(name[0])       # index 0 থেকে প্রথম character নিচ্ছি -> output: P
print(name[-1])      # negative index, শেষ থেকে গণনা -> output: n
print(name[1:4])     # slicing, index 1 থেকে 3 পর্যন্ত (4 exclusive) -> output: yth
print(name[::-1]) 
print(len(name))

#String Methods

text = " hello world"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("world", "Python"))
print(text.split())

sentance = "apple,banana,mango"
print(sentance.split(","))

words = ["apple", "banana", "mango"]
print(", ".join(words)) 

print("hello".startswith("he"))   
print("hello".endswith("lo"))     
print("hello world".find("world"))
print("ha"*3)

#String Immutability
s = "Hello"
s[0] = "J"    # এটা Error দিবে!
print(s)
s = "J" + s[1:]    # s[1:] মানে index 1 থেকে শেষ পর্যন্ত -> "ello"
print(s)   
