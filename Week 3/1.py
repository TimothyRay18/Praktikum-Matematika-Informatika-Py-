""" 
Nama: Timothy
NIM: 1119007
"""
from __future__ import print_function

if __name__== "__main__": 
    daftar_mahasiswa=['Bokir','Kincup','Ucup']

    for x in daftar_mahasiswa:
        print(x)

    print()

    for  index, val in enumerate(daftar_mahasiswa):
        print(index+1, end ='. ')
        print(val)