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
    print("Truth table")
    print("Proporsisi: p "+DISJUNCTION+" q "+DISJUNCTION+" r")
    print('{:8} {:8} {:8} {:8}'.format('p','q','r','p '+DISJUNCTION+' q '+DISJUNCTION+' r'))
    input_truth_values_iterator = product([True,False], repeat=3) 
    input_truth_values = list(input_truth_values_iterator)
    for x in(input_truth_values):
        print('{:<8} {:<8} {:<8} {:8}'.format(x[0],x[1],x[2],x[0] or x[1] or x[2]))
