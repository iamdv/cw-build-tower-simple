def tower_builder(n_floors):
    # build here
    myList = []
    for i in range(1, n_floors + 1):
        if (i == 1):
            myList.append((' ' * (n_floors - 1)) + '*' + (' ' * (n_floors - 1)))
        elif (i < n_floors):
            myList.append( (' ' * (n_floors - i)) + ('*' * ((i * 2)-1)) + (' ' * (n_floors - i)))
        else:
            myList.append('*' * ((i * 2)-1))
    return myList
