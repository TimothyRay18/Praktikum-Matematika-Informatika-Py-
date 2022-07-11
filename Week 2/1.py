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
    input_truth_values = [(True,True,True),(True,True,False),(True,False,True),(True,False,False),(False,True,True),(False,True,False),(False,False,True),(False,False,False)]

    print("Truth table")
    print("Proporsisi: p "+CONJUNCTION+" q "+CONJUNCTION+" r")
    print('{:8} {:8} {:8} {:8}'.format('p','q','r','p '+CONJUNCTION+' q '+CONJUNCTION+' r'))
    for x in(input_truth_values):
        print('{:<8} {:<8} {:<8} {:8}'.format(x[0],x[1],x[2],x[0] and x[1] and x[2]))