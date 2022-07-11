""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

if __name__== "__main__": 
    truth_value = [True,True,True,False]
    print("Nilai truth value", end =": ")
    print(truth_value)
    
    found=False
    for x in truth_value:
        if x==False:
            found=True
            break

    if found == True:
        print("Bukan Tautologi")
    else:
        print("Tautologi")