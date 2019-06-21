visualize data graphs 
i)  take input from  a file where you have 4 rows and 5 columns
ii)  columns having - student_name , marks , age , contact , study_hours
iii)  visualize this data as pie chart
iv)  file name must  student.csv with all column separated by ','



#!usr/bin/python3
import csv
import pandas as pd
import matplotlib.pyplot as plt

data=[['student_name','marks','age','contact','study_hours'],['tanu','89','19','8291047284','5'],['ritika','87','18','72910472628','6'],['shreya','90','19','8391047389','7']]

with open('st.csv','w') as csvFile:
	writer=csv.writer(csvFile)
	writer.writerows(data)
csvFile.close()

df=pd.read_csv('/home/adhoc/ml_tasks/st.csv')
print(df)
study=df["study_hours"]
name=df["student_name"]
exp=[0.1,0,0.1]
plt.pie(study,labels=name,explode=exp,autopct='%1.5f%%',shadow=True)
plt.grid(color="red")
plt.show()
