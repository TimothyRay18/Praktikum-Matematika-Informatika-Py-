""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

def ubah(a):
    if a == "True" or a == "true":
        return True
    else:
        return False

if __name__== "__main__": 
    var_assignment = {

    }

    var_assignment['p'] = True
    var_assignment['q'] = False
    var_assignment['r'] = True

    boolean_func = '(p and q) or r'
    
    print("Fungsi boolean: (p and q) or r")

    for x in var_assignment:
        print(x, end = ': ')
        print(var_assignment[x])

    eval_rslt = eval(boolean_func,var_assignment)

    print(boolean_func,end=': ')
    print(eval_rslt)