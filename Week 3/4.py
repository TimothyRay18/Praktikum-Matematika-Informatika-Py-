""" 
Nama: Timothy
NIM: 1119007
"""

from __future__ import print_function

def ubah(a):
    if a == "T" or a == "t":
        return True
    else:
        return False

if __name__== "__main__": 
    var_assignment = {

    }

    boolean_func = "(p and q) or r"
    variable_names = ('p','q','r')

    for x in variable_names:
        y = raw_input(x+": ")
        var_assignment[x]=ubah(y)

    eval_rslt = eval(boolean_func,var_assignment)
    
    print(boolean_func, end=' = ')
    print(eval_rslt)