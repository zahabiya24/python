#import array 
'''import array
a= array.array('i',[10,20,30,40,50])
print(a)
for i in range(5):
    print(a[i])'''
#==================================
#import array as arr
'''import array as arr
b=arr.array('i',[10,20,30,40,50])
for i in range(5):
    print(b[i])'''
#=================================
#from array import *
'''from array import *
c=array('i',[1,2,3,4,5])
for i in range(5):
    print(c[i])'''

#===============================
#unicode f=float & u=character
'''a=array('f',[1.5,2.5,3.5,4.5,5.5])
for i in range(5):
    print(a[i])
b=array('u',['a','b','c','d','e'])
for i in range(5):
    print(b[i])'''
#=====================================
#array slicing
from array import *
a= array('i',[10,20,30,40,50])
print(a[1:3:])
print(a[:2:3])
print(a[1::3])
print(a[::2])
