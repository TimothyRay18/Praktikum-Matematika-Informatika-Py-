"""
Nama:Timothy
NIM:1119007
"""
#konstanta global
NEGATION = '\u00ac'
CONJUNCTION = '\u2227'
DISJUNCTION = '\u2228'
XOR = '\u2295'
IMPLICATION = '\u21d2' 
IFF =  '\u21d4'

if __name__ =="__main__":
    boolean_func = input("Masukan input:")
    code = compile(boolean_func, '<string>', 'eval') 
    variable_names = code.co_names
    for x in variable_names:
        print('{:10}'.format(x), end='')
    print('{:10}'.format(boolean_func), end='')