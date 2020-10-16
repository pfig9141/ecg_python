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
# ustalenie źródła zapisów
stacja = 'DOM2'
if stacja == 'DOM1':
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
    # directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre' 14.10.2020
elif stacja == 'WAT':
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
    # directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
elif stacja == 'DOM2':
    directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
    # directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
# zaimportowanie zapisu/zapisów
record, fields = wfdb.io.rdsamp(directory,sampfrom=0,channels=[2])
# zaimportowanie numerów qrs (PTB 104) z excela
# qrs_loc = pd.read_excel('F:/Foldery/Nauka/ECG_DSP/baza_ref/qrs_index/PTB/Healthy control/patient104.xlsx')
# qrs_loc = np.array(qrs_loc)[:,0]
qrs_loc =[739, 1517, 2274, 3033, 3821, 4656, 5520, 6321, 7090, 7864, 8638, 9379,
          10120, 10870, 11650, 12420, 13160, 13920, 14720, 15500, 16250,
          17020, 54650, 57030, 59430]
          
# recording time range and time vector
width1, width2 = 200,400
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
n_plot = int(np.floor(len(qrs_loc)/25))+1
# number of windows
n_plot = np.arange(n_plot)
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
        
# some additional lines
# z = np.remainder(z,25)
# pos = [ int((z-np.remainder(z,10))/5) , int(np.remainder(z,10)) ]