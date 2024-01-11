myPets = ['Ogi', 'Softy', 'Fat Kubu']

while True:
    print('podaj imię zwierzaka:')
    name = input()
    if name not in myPets:
        print('Nie mamy takiego pokemona w naszych zasobach jak ' + name + '.')
    else:
        print(name + ' to mój zwierzak')