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

from itertools import product

if __name__ =="__main__":
    boolean_func = raw_input("Masukan input:")
    code = compile(boolean_func, '<string>', 'eval') 
    variable_names = code.co_names

    input_truth_values_iterator = product([True,False],repeat=len(variable_names))
    input_truth_table = list(input_truth_values_iterator)

    print(input_truth_table)