"""
Timothy
1119007
"""
def hitung_kemiripan_by_kardinalitas(a,b):
    set3 = a & b
    return set3

if __name__ == "__main__":
    print("A")
    set1 = {6,7,8}
    set2 = {1,6,7}
    kemiripan = hitung_kemiripan_by_kardinalitas(set1,set2)
    print("hasilnya: ",end='')
    print(len(kemiripan))
    print()

    print("B")
    musik_jonathan = {'electronica', 'rap', 'industrial', 'rock', 'funk'}
    musik_anthony = {'funk', 'alternative', 'rap'}
    musik_josh = {'alternative', 'funk', 'rap'}
    musik_michael = {'jazz', 'electronica'}
    musik_brian = {'rock', 'funk', 'industrial', 'rap'}

    musik= hitung_kemiripan_by_kardinalitas(musik_jonathan,musik_anthony)
    print(len(musik))
    print(musik)

    musik= hitung_kemiripan_by_kardinalitas(musik_jonathan,musik_josh)
    print(len(musik))
    print(musik)

    musik= hitung_kemiripan_by_kardinalitas(musik_jonathan,musik_michael)
    print(len(musik))
    print(musik)

    musik= hitung_kemiripan_by_kardinalitas(musik_jonathan,musik_brian)
    print(len(musik))
    print(musik)

    musik= hitung_kemiripan_by_kardinalitas(musik_josh,musik_michael)
    print(len(musik))
    print(musik)