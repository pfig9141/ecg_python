def set_access_path(stacja,patient,ident):
    if stacja == 'DOM':
        disk = 'F:/'    
        directory = disk + 'Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/' + patient
     #   directory = directory_DOM + ident
     #   matfile_directory = directory_DOM + 'matlab_' + ident
    elif stacja == 'WAT':
        disk = 'G:/'    
        directory = disk + 'Foldery/Nauka/ECG_DSP/baza_ref/baza_ref_PTB/' + patient + '/' + ident
        matfile_directory =  disk + 'Foldery/Nauka/ECG_DSP/baza_ref/matlab_baza_ref_PTB/' + patient + '/' + ident
    return directory, matfile_directory 