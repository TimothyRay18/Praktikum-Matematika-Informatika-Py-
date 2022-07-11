""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

if __name__== "__main__": 
    var_assignment = {
        'p' : True,
        'q' : False,
        'r' : True
    }

    print("Fungsi boolean: (p and q) or r")
    for x in var_assignment:
        print(x, end = ': ')
        print(var_assignment[x])
        