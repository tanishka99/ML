import numpy as np

x=int(input("Enter no of rows:"))
y=int(input("Enter no of columns:"))

z=np.random.randint(10,size=(x,y))
print(z)

f=open('new.txt','w')
f.write(z)
f.close()
