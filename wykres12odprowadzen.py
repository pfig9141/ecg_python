# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:51:42 2020
@author: Piotr
"""
"""
Prosty program do wizualizacji odprowadzeń i,ii,iii,avr,avl,avf,v1,v2,v3,v4,v5,v6
dane wejciowe to /definicja zakresu czasowego względem indeksu qrs - width1, width2/
"""
import numpy as np
import wfdb
import wfdb.processing
import matplotlib.pyplot as plt
import pandas as pd

plt.close('all')
# ustalenie źródła zapisów
stacja = 'WAT'
if stacja == 'DOM1':
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
    # directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre' 14.10.2020
elif stacja == 'WAT':
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient105/s0303lre'
elif stacja == 'DOM2':
    directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
# importowanie danych związanych z okreslonym zapisem    
ecg_record = wfdb.io.rdheader(directory) # ecg_record.sig_name[0]
ecg_record_data, fields = wfdb.io.rdsamp(directory,sampfrom=0,sampto=10000,
                                         channels=[0,1,2,3,4,5,6,7,8,9,10,11])
r_peaks = pd.read_excel('G:/Foldery/Nauka/ECG_DSP/baza_ref/qrs_index/PTB/Healthy control/patient104.xlsx',
                        index_col=0,skiprows=0)
r_peaks = r_peaks['rp']
width1, width2 = 200,300
n = np.linspace(r_peaks[0]-width1,r_peaks[0]+width2,width1+width2+1,dtype='int')
fig, ax = plt.subplots(3,4)
fig.suptitle(ecg_record.comments[4])
loc = 'left'
fontdict = {'fontsize':12}
z = 0
for k in range(4):
    for p in range(3):
        ax[p,k].plot(n,ecg_record_data[n,z])
        ax[p,k].set_xticks([])
        ax[p,k].set_yticks([])
        ax[p,k].set_title(ecg_record.sig_name[z],fontdict,
                          loc=loc)
        z = z+1
        
        