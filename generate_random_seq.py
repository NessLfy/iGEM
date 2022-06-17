# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:33:26 2022

@author: nessl
"""

from random import choice
#import sys
#import matplotlib.pyplot as plt 

def String(length):
   
   DNA=""
   for count in range(length):
      DNA+=choice("CGTA")
   return DNA
  

#print(String(int(sys.argv[1])))

def write_fa(path,seq,name):
    ofile = open(path+".fa", "w")

    for i in range(len(seq)):
        ofile.write(">" + name[i] + "\n" +seq[i] + "\n")

    #do not forget to close it

    ofile.close()

"""
seq = []
name = []

for i in range(10):
    seq.append(String(28))
    name.append(str(i))
    
write_fa("sequences_10",seq,name)
"""
"""
Testing of randomness

A = []
T = []
G = []
C = []

for i in range(1000):
    
    m = String(1000)
    A.append(m.count("A"))
    T.append(m.count("T"))
    G.append(m.count("G"))
    C.append(m.count("C"))

alpha= 0.6
plt.hist(A,alpha=alpha)
plt.hist(T,alpha=alpha)
plt.hist(G,alpha=alpha)
plt.hist(C,alpha=alpha)
plt.show()

"""




        
