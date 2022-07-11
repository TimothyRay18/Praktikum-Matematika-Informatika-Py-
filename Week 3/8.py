""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

def is_Contingency(t_value):
    cek=False
    for x in t_value:
        if t_value[x]!=t_value[x+1] or t_value[x]!=t_value[len(t_value)-1]:
            cek = True
            break
    return cek


if __name__== "__main__": 
    truth_value = [True,True,True,False]
    print("Nilai truth value", end =": ")
    print(truth_value)

    found = is_Contingency(truth_value)
    if found == True:
        print("Contingency")
    else:
        print("Tidak Contingency")