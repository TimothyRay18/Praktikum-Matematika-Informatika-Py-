"""
Timothy
1119007
"""

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

    list_sisi=[]

    for x in graf:
        for y in graf[x]:
            sisi = {x,y}
            if sisi not in list_sisi:
                list_sisi.append(sisi)
    print(list_sisi)
    print(len(list_sisi))