# 14.10.2020
# program do półautomatycznej detekcji zespołów qrs
# dane wejsciowe to /nazwa pliku (directory)/, 
# oraz /num_tysiac/ czyli numer kolejnego podzbioru danych wejsciowych
# o dlugosci 1000 próbek
# uwaga \\ zakres czasowy w którym poszukiwany jest zapis qrs zależny jest od
# tętna, należy modyfikować parametr /x2/ oraz wektor indeksów w zobrazowaniu
# na końcu programu \\
import numpy as np
import wfdb
import wfdb.processing
import matplotlib.pyplot as plt

# usuń wszystkie aktywne okna graficzne
plt.close('all')
# ustaw scieźkę i nazwę pliku
stacja = 'WAT'
if stacja == 'DOM1':
    directory = 'F:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
else:
    directory = 'G:/Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/patient104/s0306lre'
# zaimportuj dane
record, fields = wfdb.io.rdsamp(directory,sampfrom=0,channels=[0])
# pętla przesuwa się wzdłuż wektora danych porcjami po (x1,x2) próbek 
# w każdej porcji obliczana jest wartosc maksymalna = index
# indeks wartosci maksymalnej (qrs) w danym przedziale (x1,x2) = x11+index
#  
num_tysiac = 3
x1 = 0              # zakres czasowy do analizy od x1 do x2
x2 = 1000
for k in range(num_tysiac):
    maximum=0
    index = 0
    for i,value in enumerate(record[x1:x2]):
        if value>maximum:
            maximum=value
            index=i
            print(i)
    x11 = x1            # wartosc pomocnicza do wykresow 
    x22 = x2
    x1 = x1 + 1000
    x2 = x2 + 1000
plt.figure()     
plt.plot(np.arange(1000),record[x11:x22])
plt.plot(index,record[int(x11)+index],marker='s')
print(int(x11)+index)
#
#fig = plt.figure()
#plt.plot(np.arange(len(record)),record,int(x1)+index,record[int(x1)+index],marker='s')
#plt.xlim(x1,x2)


