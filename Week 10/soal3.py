"""
Timothy
1119007
"""
def UbahDes(n):
    tuple_nilai = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    list_hasil=[]
    while(True):
        n,hasil_mod=divmod(n,16)
        list_hasil.insert(0,tuple_nilai[hasil_mod])
        if(n==0):
            return("".join(list_hasil))
    return 0;

if __name__ == "__main__":
    for x in range(0,35):
        print(x,end=' ')
        str_hex=UbahDes(x)
        print('{:<4}'.format("0x"+str_hex))