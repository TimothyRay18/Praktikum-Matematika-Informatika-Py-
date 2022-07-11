"""
Timothy
1119007
"""
def desimal_ke_biner3digit(desimal):
    x = bin(desimal)
    x = x[2:]
    x = x.zfill(3)
    return x

if __name__ == "__main__":
    for x in range(8):
        print(x)
    print()

    for x in range(8):
        print(x,end ='')
        print(" ->",desimal_ke_biner3digit(x))
    print()

    for x in range(8):
        print(x,end ='')
        biner = desimal_ke_biner3digit(x)
        print(" ->",biner,"-> ", end='')
        for a in biner:
            print(a,"",end='')
        print()
    print()

