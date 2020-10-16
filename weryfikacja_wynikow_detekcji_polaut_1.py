# 14.10.2020 
# program przeznaczony do weryfikacji wyników półautomatycznej detekcji 
# zespołów QRS 
# dane wejsciowe to /indeksy wartosci maksymalnej zespołu (qrs_loc)/
# /nazwa pliku (directory)/ 
# /parametry zakresu czasowego (width1,width2)/
import numpy as np
import wfdb
import wfdb.processing
import matplotlib.pyplot as plt
import pandas as pd

# all graphics windows removed
plt.close('all')
# set path and filename
stacja = 'WAT'
if stacja == 'DOM1':
    directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
else:
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
# load data
record, fields = wfdb.io.rdsamp(directory,sampfrom=0,channels=[0])
# qrs index
qrs_loc = [794, 1703, 2616, 3474, 4319, 5193, 7976, 9900, 10842, 11735,
          12610, 13577, 14548, 15465, 16376, 17368, 18388,19431, 20437, 21405, 22399,
          23402, 24353, 25327, 26334, 27345, 28311, 29265, 30268, 31259, 32197, 33121,
          34116, 35135, 36139, 37104, 38096, 39097, 40061, 41002, 42023, 43100, 44159,
          45167, 46120, 47104,48114,49098,50111]
# recording time range and time vector
width1, width2 = 200,300
# set allocation
Rec1 = np.empty((0,2*width1+width2+1))
Time = np.empty((0,2*width1+width2+1))
# writing vectors to the array
for M in qrs_loc:
    a, b = M-width1, M+width2
    t = np.linspace(a,b,2*width1+width2+1,dtype='int')
    Time = np.vstack((Time,t))
    rec1 = record[t] 
    Rec1 = np.vstack((Rec1,rec1.transpose()))
# window with 25 graphs    
n_plot = int(np.floor(len(qrs_loc)/25))
# number of windows
n_plot = np.arange(n_plot+1)
# number of windows
z = 0
for l in n_plot:
    fig, ax = plt.subplots(5,5)
    for k in range(5):
        for p in range(5):
            if z <= len(qrs_loc)-1:
                ax[k,p].plot(Time[z,:],Rec1[z,:])
                ax[k,p].set_xticks([])
                ax[k,p].set_yticks([])
                z = z + 1
# delete timeline desctription
for k in range(0,5):
    for p in range(0,5):
        ax[k,p].set_xticks([])
        ax[k,p].set_yticks([])
        print(p)
        print(k)
        
# some additional lines
# z = np.remainder(z,25)
# pos = [ int((z-np.remainder(z,10))/5) , int(np.remainder(z,10)) ]