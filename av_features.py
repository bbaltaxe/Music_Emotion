"""
This file takes a large number of csvs. 
The output is a csv where each row is the columnwise average of each input csv 
"""

import pandas as pd

def main(): 

    df = pd.read_csv("~/Downloads/features/10.csv",sep=';')
    df = df.filter(regex='mean',axis=1)
    adf = pd.DataFrame(columns=df.columns)
    
    for n in range(2060):
        filename = "~/Downloads/features/{}.csv".format(n)
    
        try: 
            df = pd.read_csv(filename,sep=';')
        except FileNotFoundError: 
            print("no file here, sir")
            continue
        #only use columns that include the mean
        df = df.filter(regex='mean',axis=1)
        #df = df.iloc[:,0]
        #df = pd.concat([df,ndf],axis=1)
   
        #create new dataframe 
        #adf = pd.DataFrame(columns=df.columns)
    
        #add a row for each csv
        #each col is the av of the full csv
        s = df.mean(numeric_only=True)
        s.name = n
        adf = adf.append(s)

    
        print(adf.info())
    
    adf.to_csv("out.csv")
    
    return 
    


if __name__ == "__main__":
    main()

