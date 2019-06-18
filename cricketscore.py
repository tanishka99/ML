#!usr/bin/python3

import matplotlib.pyplot as plt

#only loading python ori lib
player=["virat","dhoni","pandey"]
runs=[120,150,78]
plt.xlabel("players")
plt.ylabel("runs")    
plt.bar(player,runs)
plt.grid(color="pink")  #to form grid in graph
plt.legend() #to show label wth plot
plt.show()
