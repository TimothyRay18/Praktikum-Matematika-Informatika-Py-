"""
Timothy
1119007
"""
def UbahBiner(n):
    list_mod=[]
    while(True):
        n,hasil_mod = divmod(n,2)
        list_mod.insert(0,str(hasil_mod))
        if(n==0):
            biner="".join(list_mod)
            return ('{:>4}'.format(biner))
            break
if __name__ == "__main__":
    for x in range(0,10):
        print(x,end=" ")
        str_biner=UbahBiner(x)
        print(str_biner)
        #print(type(str_biner))