#import glob
#mport pandas as pd

#path=f"C:/Users/Vaishnavi/OneDrive/Desktop/workspace/csv project/drive file"
#all_files=glob.glob(path+"/*.csv")
#df_list=[]
#for file in all_files:
 #   df=pd.read_csv(file)
  #  df_list.append(df)

#combined_df=pd.concat(df_list,ignore_index=True)
#print(combined_df)    

import os
import glob
import pandas as pd

path = 'C:/Users/Vaishnavi/OneDrive/Desktop/workspace/csv project/drive file'
files=os.listdir(path)
for s in files:
    #print(s)
    #all_files=os.path.isfile(os.path.join(path,s))
    #print(all_files)
    for track in os.scandir(path+"/"+s):
        if(track.is_file()):
            print(track.name) 