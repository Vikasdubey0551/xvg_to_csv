import  re
import string
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-xvg",help="INPUT.xvg", default="test.xvg")
parser.add_argument("-csv",help="OUTPUT.csv", default="test.csv")
options = parser.parse_args()

#Reading for the header
with open(options.xvg,'r') as f:
   pattern1=re.compile('xaxis  label "(.*)"')
   metadata1=pattern1.findall(f.read())
with open(options.xvg,'r') as f:
   pattern2=re.compile(' legend "(.*)"')
   metadata2=pattern2.findall(f.read())

#Making list without brackets
header=[metadata1,metadata2]
header=str(header).translate(string.maketrans('', ''), '[]\'\' \'')
print("columns : %s"%(header))

#Reading XVG data
gen = (r for r in open(options.xvg) if not r[0] in ('@', '#'))
data = np.genfromtxt(gen, delimiter='')

#Writing CSV
with open(options.csv, 'w') as f:
   f.write("%s\n"%(header))
   np.savetxt(f, data,  fmt="%.3f", delimiter=',')
f.close()
