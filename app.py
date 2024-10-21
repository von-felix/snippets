from IPython.display import display
import pandas as pd 
  
# reading two csv files 
data1 = pd.read_csv('hosts.csv') 
data2 = pd.read_csv('ips.csv') 

dict1 = data1.to_dict()
dict2 = data2.to_dict()

data3 = pd.DataFrame.from_dict(dict1)
data4 = pd.DataFrame.from_dict(dict2)
  
# using merge function by setting how='inner' 
output1 = pd.merge(data1, data2,  
                   on='hostname',  
                   how='outer') 
  
with pd.ExcelWriter('output.xlsx') as writer:  

    data1.to_excel(writer, index=False, sheet_name='Sheet_name_1')

    data2.to_excel(writer, index=False, sheet_name='Sheet_name_2')
    
    output1.to_excel(writer, index=False, sheet_name='Sheet_name_3')

print(f'Process completed.')
         
pass