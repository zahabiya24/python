#array functon using linspace
from numpy import *
a=linspace(1,5,5)
print("linspace: ",a)

#creating array using logspace
from numpy import *
a=logspace(1,5,5)
print("logspace: ",a)


#creating array using arange
from numpy import *
a=arange(1,10,3)
print("arange(1,10,3): ",a)
b=arange(10)
print("arange(10): ",b)
c=arange(5,10)
print("arange(5,10): ",c)


#creating array using zeros and ones
from numpy import *
a=zeros(5)
print("zeros: ",a)
b=ones(10)
print("ones: ",b)
