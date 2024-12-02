
# 1- import libraries(pandas, numpy, seaborn, warning, matplotlib)
import pandas  as pd
import numpy as np
import seaborn as ssn
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
 #---------------------------------------------------------------------------------------------------------
#Display only 2 decimal rather than the default of 6
#pd.set_option("precision", 2)
#pd.options.display.float_format = '{:.2f}'.format
 #---------------------------------------------------------------------------------------------------------
# 2- Define path for the dataset file
file_path = "/home/mack/Downloads/predict+students+dropout+and+academic+success/data.csv"
#----------------------------------------------------------------------------------------------------------
# 3- read the csv file
psas=pd.read_csv(file_path,sep =";")
#matplotlib inline
plt.rcParams["figure.figsize"] = (8, 6)
#----------------------------------------------------------------------------------------------------------- 
# 4- get general information about my data set as head, shape, columns
psas_Heads=psas.head(5)
print(psas_Heads)
psas_shapes=psas.shape
print(psas_shapes)
psas_columns=psas.columns
print(psas_columns)
#-----------------------------------------------------------------------------------------------------------
# 5- Get feneral information(general insight)
print(psas.info())
#-----------------------------------------------------------------------------------------------------------
# 6- hows the main statistical characteristics
     #of the dataset for each numerical feature
      #Mean, Median, mode
print(psas.describe())
#-----------------------------------------------------------------------------------------------------------
# 7- Describe the non numerical data
#print(psas.describe(include="all"))
print(psas.describe(include="object"))
#-----------------------------------------------------------------------------------------------------------
# 8- counting each secore of my data
print(psas["Marital status"].value_counts())
print(psas["Nacionality"].value_counts())
#-----------------------------------------------------------------------------------------------------------
# 9- Find  the ratio of each part according to the total(proportion)      
print(psas["Marital status"].value_counts(normalize="True"))
print(psas["Nacionality"].value_counts(normalize="True"))
print(psas["Father's qualification"].value_counts(normalize = "True"))
print(psas["Mother's qualification"].value_counts(normalize = "True"))
print(psas["Age at enrollment"].value_counts(normalize = "True"))      
#-----------------------------------------------------------------------------------------------------------
# 10- Find the maxium  & minimum value in each column 
print(psas.apply(np.max))
print(psas.apply(np.min))
#-----------------------------------------------------------------------------------------------------------
##d={1:"married",2:"single"}
##psas[""]=psas[""].map(d)
#-----------------------------------------------------------------------------------------------------------
# 11- Sort the data using one columns or more 
print(psas.sort_values(by="Marital status",ascending = False))
print(psas.sort_values(by=["Age at enrollment","GDP"],ascending = [False,True]))
#----------------------------------------------------------------------------------------------------------
##import sqlite3 as d
##connection=db.connect("/home/mack/Downloads/predict+students+dropout+and+academic+success/data.csv")
##query1="SELECT * FROM data"
##df1 = pd.read_sql_query(query1,connection)
##print(df1) 
#-----------------------------------------------------------------------------------------------------------
# 12- Pivot table for some features
#Note:putting r before the column name to skip the \ in the name
# A- Two features
print(pd.crosstab(psas["Marital status"],psas["Target"]))
print(pd.crosstab(psas["Target"],psas["Mother's qualification"]))
print(pd.crosstab(psas["Target"],psas["Father's qualification"]))
# B- Three features
print(pd.crosstab(psas[r"Marital status"],psas["Daytime/evening attendance\t"],psas["Target"], aggfunc = "count"))
#-----------------------------------------------------------------------------------------------------------
# 13- More Pivot table for some features
print(pd.crosstab(psas["Marital status"],psas["Age at enrollment"],normalize = 'index'))


print(psas.pivot_table(["Marital status", "Mother's qualification"], ["Target"], aggfunc = "mean").head(10))

print(psas.pivot_table(["Marital status", "Mother's qualification"], ["Target"], aggfunc = "count"))

#-----------------------------------------------------------------------------------------------------------
# 13- Visualization:
#                 A-Scatter_matrix
#pd.plotting.scatter_matrix(psas[["Marital status","Age at enrollment", "Mother's qualification"]],figsize=(13,13),diagonal = "kde")
#plt.show()

#pd.plotting.scatter_matrix(psas[["Target","Marital status"]],figsize=(13,13),diagonal = "kde")
#plt.show()

#pd.plotting.scatter_matrix(psas[["Target","Age at enrollment","Marital status"]],figsize=(13,13),diagonal = "kde")
#plt.show()
#                  B-Histogram
#psas["Marital status"].hist()
#plt.show()

#psas["Pervious qualifcation"].hist()
#plt.show()

#                  More Histogram
#psas.hist(color = "k",bins = 35, figsize=(20,13))
#plt.show()

#               C-Box Plot
psas.boxplot(column = "Age at enrollment", by = "Target")
plt.show()

#                 D-
