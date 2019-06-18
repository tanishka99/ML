#!usr/bin/python3

import matplotlib.pyplot as plt

#only loading python ori lib
x=[2,3]
x1=[4,9,2]
y1=[8,0,3]
y=[9,5]
plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="water")
plt.plot(x1,y1,label="sand")     #this will draw a straight line
plt.bar(x,y)
plt.bar(x1,y1) #to plot bar
plt.grid(color="pink")  #to form grid in graph
plt.legend() #to show label wth plot
plt.xlim(0,12)
plt.ylim(0,15) #to show min n max no in y axis
plt.show()
