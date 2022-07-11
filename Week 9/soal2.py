"""
Timothy
1119007
"""
def hitung_kemiripan_by_jaccard(a,b):
    setA = a & b
    setB = a | b
    A = len(setA)
    B = len(setB)
    if(A>B):
        return B/A
    else:
        return A/B

if __name__ == "__main__":
    print("A")
    set1 = {6,7,8}
    set2 = {1,6,7}
    kemiripan = hitung_kemiripan_by_jaccard(set1,set2)
    print("hasilnya: ",end='')
    print(kemiripan)
    print()

    print("B")
    musik_fav = {
        "Jonathan": {'electronica', 'rap', 'industrial', 'rock', 'funk'}, "Anthony": {'funk', 'alternative', 'rap'},
        "Josh": {'alternative', 'funk', 'rap'},
        "Michael": {'jazz', 'electronica'},
        "Brian": {'rock', 'funk', 'industrial', 'rap'},
    }

    nama = input("Masukkan nama untuk dicari nilai kemiripannya: ")

    for x in musik_fav:
        if(x!=nama):
            hasil = hitung_kemiripan_by_jaccard(musik_fav[nama],musik_fav[x])
            print("Nilai kemiripan dengan "+x+" = ",end='')
            print(hasil)