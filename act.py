import numpy as np
import csv
import pandas as pd 
import matplotlib.pyplot as plt


bills = pd.read_csv("C:/Users/phindulo/Documents/python/mpg.csv",index_col = 0)



bills["Displacement-To-Cylinder-Ratio"] =  bills["displacement"] / bills["cylinders"] 

newSet = pd.DataFrame(bills,columns = ['cylinders', 'displacement',  'horsepower',  'weight',  'acceleration',  'model_year',  'origin','name','Displacement-To-Cylinder-Ratio'])
setTwo = newSet[newSet['origin'] == 'usa']
setFour = newSet[newSet['origin'] == 'japan']
setFive = newSet[newSet['origin'] == 'europe']
print("")
print("")
print("")
print("")

print("*********************************************************************")
print("This is a data set(subset) consisting of all the records filtered by Japan")
print("")
print("")
print("")
print("")
print(setTwo)
print("*********************************************************************")
print("")
setThree = np.corrcoef(setTwo['displacement'],setTwo['cylinders'])
print("*********************************************************************")
print("Below is the correlation(generated by the program) between Displacement and Cylinders:" )
print(setThree)
print("")
print("")
if(setThree[0][1] < -0.8 or setThree[0][1]   > 0.8):
    print("Significantly different from zero: SIGNIFICANT")
    print("CORRELATION VALUE: " + str(setThree[0][1]))
else:
     print("Not significantly different from zero: NOT SIGNIFICANT")
     print("CORRELATION VALUE: " + str(setThree[0][1]))


       
print("")
print("")
print("*********************************************************************")
print("")
ax = setTwo.plot(kind='scatter', x='cylinders', y='displacement', color='white', alpha=0.5, linewidth=0,label='USA_CylinderDisplacement')

ax.set_ylim((0, 600))
ax.set_xlim((0,10))
ax.legend()
# Specify background color for the axis/plot
ax.set_facecolor("lightslategray")

plt.title('Projection of Cylinders to Displacement')
plt.show()



 

