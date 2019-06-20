create 2D numpy  based array with given conditions:

i)   take input from user in terms of dimension like (3x2 or 6x7)
ii)   fill this numpy array with random number
iii)  store this array in a file


import numpy as np

x=int(input("Enter no of rows:"))
y=int(input("Enter no of columns:"))

z=np.random.randint(10,size=(x,y))
print(z)

f=open('new.txt','w')
f.write(z)
f.close()
