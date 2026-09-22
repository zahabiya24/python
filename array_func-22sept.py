#array function
from array import *
a=array('i',[10,20,30,40,50,30,80])
a.append(60)
print("append: ",a)
a.pop()
print("delete from last: ",a)
a.pop(2)
print("delete from specific index (2) : ",a)
a.remove(50)
print("delete specific value (50): ",a)
a.reverse()
print("reverse: ",a)

print("count 30: ",a.count(30))
print("index of 20 value: ",a.index(20))
