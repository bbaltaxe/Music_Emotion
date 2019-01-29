"""
This file takes a large number of csvs. 
The output is a csv where each row is the columnwise average of each input csv 
"""

import pandas as pd

def main(): 

    #create new data frame from existing cols
    df = pd.read_csv("~/Downloads/features/10.csv",sep=';')
    df = df.filter(regex='mean',axis=1)
    adf = pd.DataFrame(columns=df.columns)
    
    #iterate over all song csvs
    for n in range(2060):
        filename = "~/Downloads/features/{}.csv".format(n)
    
        try: 
            df = pd.read_csv(filename,sep=';')
        except FileNotFoundError: 
            print("no file here, sir")
            continue

        #only use columns that include the mean
        df = df.filter(regex='mean',axis=1)
    
        #add a row for each csv
        #each col is the av of the full csv
        s = df.mean(numeric_only=True)
        s.name = n
        adf = adf.append(s)

    
        print(adf.info())
    
    #save new df as csv
    adf.to_csv("out.csv")
    
    return 
    


if __name__ == "__main__":
    main()

