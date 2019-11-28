import  re
import string
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', nargs='+', metavar='', help="INPUT.xvg/supports multiple files", default="test.xvg")
parser.add_argument("-o",help="OUTPUT.csv", metavar='', default="test.csv")
options = parser.parse_args()

data=[]
metadata=[]
pattern1=re.compile('xaxis  label "(.*)"')
pattern2=re.compile(' legend "(.*)"')

i=0
#Reading for the header
for file in options.f:
    with open(file,'r') as f:
        metadata.append(pattern1.findall(f.read()))      
    with open(file,'r') as f:
        metadata.append(pattern2.findall(f.read()))
        gen = (r for r in open(file) if not r[0] in ('@', '#'))
        if i==0:
           data= np.genfromtxt(gen, delimiter='')      
        else:
           metadata.append(pattern2.findall(f.read()))
           tmp= np.genfromtxt(gen, delimiter='') 
           data=np.hstack((data,tmp[:,1:len(tmp.T)]))
    i=i+1

#removing duplicates if there is any
def Remove_duplicate(header):
    list = []
    for element in header:
        if element not in list:
            list.append(element)
    return(list)
metadata=Remove_duplicate(metadata)

#Making list without brackets
header=str(metadata).translate(string.maketrans('', ''), '[]\'\'' )

print("Columns  :\n%s"%(header))

#Writing CSV
with open(options.o, 'w') as f:
    f.write("%s\n"%(header))
    np.savetxt(f, data,  fmt="%.3f", delimiter=',')


