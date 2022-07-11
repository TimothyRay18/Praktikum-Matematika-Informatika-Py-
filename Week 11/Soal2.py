"""
Timothy
1119007
"""

def get_terhubung(graf,str):
    list_nama = graf[str]
    return list_nama

def is_terhubung(graf,str1,str2):
    hasil=False
    for x in graf[str1]:
        if(x==str2):
            hasil=True
            break
    return hasil


if __name__ == "__main__":
    graf = {
        'Paulo': ['Max', 'Igor', 'Andreas', 'Derrick', 'Eloy'],
        'Max': ['Paulo', 'Igor'],
        'Igor': ['Max', 'Paulo', 'Andreas'],
        'Andreas': ['Igor', 'Derrick', 'Paulo'],
        'Derrick': ['Andreas', 'Paulo'],
        'Eloy': ['Paulo', 'Bella'],
        'Bella': ['Eloy'],
        'Gloria': ['Roxanne'],
        'Roxanne': ['Gloria']
    }

    #A
    list_andreas = get_terhubung(graf,'Andreas')
    print(list_andreas)
    print()

    #B
    igor_dan_gloria = is_terhubung(graf, 'Igor', 'Gloria')
    print(igor_dan_gloria)
    igor_dan_max = is_terhubung(graf, 'Igor', 'Max')
    print(igor_dan_max)
    print()

    #C
    person1 = input("Masukan orang ke-1: ")
    person2 = input("Masukan orang ke-2: ")
    print()

    #D
    list_person1 = get_terhubung(graf,person1)
    list_person2 = get_terhubung(graf,person2)
    print(person1)
    print(list_person1)
    print(person2)
    print(list_person2)
    print()

    #E
    print(person1,end=' dan ')
    print(person2,end=':')
    print()
    print(is_terhubung(graf,person1,person2))