#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

def quantif(path,names):
    
    '''
    Quantification of the paper_based test
    Computes the ratio of absorbance intensity between the control and test band
    
    Arguments:
    path: string of where the file is located
    names: a list of string of the names of the sample for the plotting
    
    '''
    
    results = pd.read_csv(path)
    intensity = list(results.Mean)
    bck = []
    test = []
    control = []
    
    counter = 0
    
    # Gather the background values situated every 2 measurements
    
    for i in range(len(intensity)):
        if counter == 3:
            counter = 0
            bck.append(intensity[i-2])
        counter+=1

    bck.append(intensity[-2])
    counter = 1
    pos = 0
    
    #remove the background to all the intensities
    
    for i in range(len(intensity)):
        if counter == 3:
            counter = 0
            intensity[i]= intensity[i]-bck[pos]
            pos += 1
        else:
            intensity[i]= intensity[i]-bck[pos]
        counter +=1

    intensity = [i for i in intensity if i != 0]

    counter = 0
    
    # get 2 lists for test and control 
    
    for i in range(len(intensity)):
        if counter == 1:
            counter = 0
            test.append(intensity[i])
        else:
            control.append(intensity[i])
            counter+=1
            
    #check that everything is good i.e there are as much control bands as tests
    
    if len(test) == len(control):
        print('Good!')
        
    #computes the ratio
    
    ratio = [test[i]/control[i] for i in range(len(test))]
    
    # plot 
    
    plt.bar([i for i in range(len(test))],ratio)
    plt.xticks([i for i in range(len(test))],names,rotation=20)
    plt.ylabel("Ratio test/control (A.U)")
    plt.tight_layout()
    plt.show()
