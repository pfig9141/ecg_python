# program zapisuje indeks zapisu qrs do pliku excela do późniejszego 
# wykorzystania\
# https://xlsxwriter.readthedocs.io/working_with_pandas.html
"""
Created on Wed Oct 14 09:18:23 2020

@author: figonpiot
"""
import pandas as pd

# qrs_loc = [794, 1703, 2616, 3474, 4319, 5193, 7976, 9900, 10842, 11735,
#           12610, 13577, 14548, 15465, 16376, 17368, 18388,19431, 20437, 21405, 22399,
#           23402, 24353, 25327, 26334, 27345, 28311, 29265, 30268, 31259, 32197, 33121,
#           34116, 35135, 36139, 37104, 38096, 39097, 40061, 41002, 42023, 43100, 44159,
#           45167, 46120, 47104, 48114, 49098, 50111,
#           51167, 52260, 53306, 54365, 55409, 56374, 57351, 58368, 59410,
#           60477, 61547, 62610, 63623, 64601, 65618, 66620, 67573, 68504,
#           69534, 70540, 71515, 72481, 73508, 74601, 75642, 76638] # patient 104 PTB
qrs_loc = [739, 1517, 2274, 3033, 3821, 4656, 5520, 6321, 7090, 7864, 8638, 9379,
          10120, 10870, 11650, 12420, 13160, 13920, 14720, 15500, 16250,
          17020, 54650, 57030, 59430]

df = pd.DataFrame(qrs_loc)
writer = pd.ExcelWriter('F:/Foldery/Nauka/ECG_DSP/baza_ref/qrs_index/PTB/Healthy control/patient105.xlsx', 
                        engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

