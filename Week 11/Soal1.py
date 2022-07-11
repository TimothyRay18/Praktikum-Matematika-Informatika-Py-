"""
Timothy
1119007
"""

if __name__ == "__main__":
    #A
    graf={
        'Paulo' : ['Max','Igor','Andreas','Derrick','Eloy'],
        'Max' : ['Paulo','Igor'],
        'Igor' : ['Max','Paulo','Andreas'],
        'Andreas' : ['Igor','Derrick','Paulo'],
        'Derrick' : ['Andreas','Paulo'],
        'Eloy' : ['Paulo','Bella'],
        'Bella' : ['Eloy'],
        'Gloria' : ['Roxanne'],
        'Roxanne' : ['Gloria']
    }

    #B
    list_simpul=[]

    for x in graf:
        cek=False
        for y in list_simpul:
            if(graf[x]==y):
                cek=True
                break
        if(cek==False):
            list_simpul.append(x)

    print(list_simpul)
    print(len(list_simpul))