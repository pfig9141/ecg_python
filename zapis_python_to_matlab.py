# -*- coding: utf-8 -*-

# Program importuje dane z bazy zapisów uwzględniając to gdzie znajduje się
# stacja dysków (stacja='WAT') i eksportuje te dane do pliku .mat w którym
# nazwa zmiennej jest taka jak ecg_record.record_name z pliku header
# wykorzystano funckję set_access_path zapisaną w 
# Foldery\Nauka\ECG_DSP\software\python 

import wfdb
import scipy.io
from zmienna import set_access_path
# opis rekordu z bazy referencyjnej
stacja = 'WAT'
patient = 'patient104'
ident = 's0306lre'
# definicja sciezki dostępu dla odczytu (stacja,patient,ident)
# oraz dla zapisu danych 
directory, matfile_directory = set_access_path(stacja,patient,ident)
record, fields = wfdb.io.rdsamp(directory,sampfrom=0,
                                channels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# zapis do .mat pliku
mdic = {'matlab_' + ident: record}
scipy.io.savemat(matfile_directory,mdic)
    





    
  
    
