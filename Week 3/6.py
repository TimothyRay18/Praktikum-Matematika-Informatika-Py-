""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

def is_contradiction(t_value):
    cek=False
    for x in t_value:
        if x==True:
            cek=True
            break
    return cek


if __name__== "__main__": 
    truth_value = [False,False,False,False]
    print("Nilai truth value", end =": ")
    print(truth_value)

    found = is_contradiction(truth_value)
    if found == True:
        print("Bukan Kontradiksi")
    else:
        print("Kontradiksi")