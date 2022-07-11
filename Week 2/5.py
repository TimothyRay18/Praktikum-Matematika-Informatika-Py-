"""
Nama:Timothy
NIM:1119007
"""

def ubah(a):
    if a=="True":
        return True
    else:
        return False

if __name__ == "__main__":
    var_assignment = {

    }

    boolean_func = raw_input("Masukan input:")
    code = compile(boolean_func, '<string>', 'eval') 
    variable_names = code.co_names

    for x in (variable_names):
        y = raw_input("Masukan input:")
        var_assignment[x] = ubah(y)

    eval_rslt = eval(boolean_func,var_assignment)

    print(eval_rslt)