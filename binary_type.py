#binary type data
hablulist = [1,2,5,67,90]
#coonvert to byte
b = bytes(hablulist)
print(type(b))

b2 = b"jonayed"                 
print(b2)                     
print(type(b2))    

#bytearray Type — Mutable Binary Data
ba = bytearray([65,66,67])
print(ba)
#change the value of 1st index
ba[0] = 90
print(ba)

#new element added use append() method
ba.append(72)
print(ba)

#bytes ↔ str convert  — encode() and decode()
text = "my name is jonayed"
encode = text.encode('utf-8')
print(encode)
print(type(encode))
decode = encode.decode('utf-8')
print(decode)

#Bitwise Operators — Binary Operation
a = 12
b = 13
print(a & b)    
print(a | b)    
print(a ^ b)    
print(~a)       
print(a << 2)  
print(a >> 2)

#memoryview — big Binary Data Efficiently Access

data = bytearray([1, 2, 3, 4, 5])
mv = memoryview(data)           

print(mv[0])                    
print(list(mv[1:3]))            

mv[0] = 99                      
print(data)   