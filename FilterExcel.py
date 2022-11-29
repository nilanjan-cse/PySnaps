import pandas as pd
import sys
import string
import random

def filterExcel(filename,filter,key):
    print(filename)
    print(filter)
    print(key)
    df = pd.read_csv(filename)
    df = df[df[filter].str.contains(key)]
    N = 7
 

    res = ''.join(random.choices(string.ascii_lowercase +string.digits, k=N))
    df.to_csv(filename.replace('.csv','_filtered_{}.csv'.format(res)),index=False)

def addHeader(filename,header):
    df = pd.read_csv(filename,names=header,encoding='latin1')
    N = 7
 

    res = ''.join(random.choices(string.ascii_lowercase +string.digits, k=N))
    df.to_csv(filename.replace('.csv','_filtered{}.csv'.format(res)),index=False)
    

filterExcel(sys.argv[1],sys.argv[2],sys.argv[3])