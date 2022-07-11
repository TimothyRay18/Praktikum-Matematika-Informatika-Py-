"""
Nama:Timothy
NIM:1119007
"""
def cetak_truth_table(list_p_q):
    for x in list_p_q:
        print('{:6}{:6}{:6}'.format(str(x[0]),str(x[1]),str(x[2])))
if __name__ == "__main__":
    list_p_or_q_values = [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    list_p_xor_q_values = [
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    print('{:6}{:6}{:6}'.format('p', 'q', 'p or q'))
    cetak_truth_table(list_p_or_q_values)
    print('{:6}{:6}{:6}'.format('p', 'q', 'p xor q'))
    cetak_truth_table(list_p_xor_q_values)
