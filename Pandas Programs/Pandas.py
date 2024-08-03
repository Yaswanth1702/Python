
import pandas as pd
#a=["Yaswanth","Abhishek","Shimlan"]
#print(type(a))
#a={"Name" : ["Yaswanth","Abhishek","Shimlan"]}
a={"Name" : ["Yaswanth","Abhishek","Shimlan"],
   "Age" : [22,23,23],
   "Sal" : [50000,60000,70000]}
data=pd.DataFrame(a)
print(type(data))
print(data)

