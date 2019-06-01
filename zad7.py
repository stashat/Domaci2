import math
import datetime
zanrovi = ['action', 'historic', 'shooter', 'first-person', 'sci-fi']

# funkcije


def chk_naziv(naziv):
    if 2 < len(naziv) < 50:
        return True
    return False


def chk_ocjena(ocjena):
    f_ocjena = float(ocjena)
    if 1 < f_ocjena < 10 and not ((f_ocjena*100-math.trunc(f_ocjena*100)) > 0):
        return True
    return False


def chk_godina(godina):
    now = datetime.datetime.now()
    if (now.year+1) > int(godina) > 1950:
        return True
    return False


def chk_izdavac(izdavac):
    if 2 < len(izdavac) < 40:
        return True
    return False


def chk_zanrovi(zanr):
    if set(map(lambda x: x.lower(), zanr.split(', '))) <= set(zanrovi):
        return True
    return False

# fajl
with open("igrice.txt", 'r') as f:
    igrice = f.readlines()
    igrice = [x.strip() for x in igrice]
    # print(igrice)
igrice_split = []
for igra in igrice:
    igrice_split.append(igra.split(';'))
# print(igrice_split)

# filtriranje fajla
igrice_filter = []
for igra in igrice_split:
    if (chk_naziv(igra[0]) and chk_ocjena(igra[1]) and chk_godina(igra[2]) and
            chk_izdavac(igra[3]) and chk_zanrovi(igra[4])):
        igrice_filter.append(igra)
# print(igrice_filter)


# dictionary
'''
ODJE TI JE GRESKA.
TREBA NAPRAVITI LISTU SA ELEMENTIMA KOJI SU DICTIONARU
A TI SI NAPRAVILA SAMO JEDA DICTIONARY KOJI IMA ELEMTE OD 
ZADNJE IRETACIJE KROZ LISTU
Red Dead Redemption - je zadnji u listi i zato ti se pojavljivao
for i in igrice_filter:
    dict_igrice = {
        'naziv' : i[0],
        'ocjena' : i[1],
        'godina' : i[2],
        'izdavac' : i[3],
        'zanrovi' : i[4]
    }
'''
list_dict_igrice = []
for igrica in igrice_filter:
    dict_igrica = {
        'naziv':   igrica[0],
        'ocjena':  igrica[1],
        'godina':  igrica[2],
        'izdavac': igrica[3],
        'zanrovi': igrica[4]
    }
    list_dict_igrice.append(dict_igrica)
# print(list_dict_igrice)

# korisnicki dio - glavna petlja
while True:
    main_petlja = input('---------------------------------\nIzaberi:\n1-za '
                        'unos novog filma\n2-za filterisanje\n3-za izlaz iz '
                        'programa\n')
    if main_petlja == '1':
        unos_igre = input('Unesite igru u obliku naziv;ocjena;godina;izdavac;'
                          'zanr: ')
        unesena_igra = unos_igre.split(';')
        if len(unesena_igra) < 5:
            print('Niste unijeli sve atribute.')
        if (chk_naziv(unesena_igra[0]) and
                chk_ocjena(unesena_igra[1]) and
                chk_godina(unesena_igra[2]) and
                chk_izdavac(unesena_igra[3]) and
                chk_zanrovi(unesena_igra[4])):
            igrice_filter.append(unesena_igra)
            print('------------------\nIgrica je dodata\n--------------------')
            print(igrice_filter)
        if not chk_naziv(unesena_igra[0]):
            print('------------------\nPogresno unesen naziv\n---------------')
        if not chk_ocjena(unesena_igra[1]):
            print('------------------\nPogresno unesena ocjena\n-------------')
        if not chk_godina(unesena_igra[2]):
            print('------------------\nPogresno unesena godina\n-------------')
        if not chk_izdavac(unesena_igra[3]):
            print('------------------\nPogresno unesen izdavac\n-------------')
        if not chk_zanrovi(unesena_igra[4]):
            print('------------------\nPogresno unesen zanr\n----------------')

    if main_petlja == '2':
        izbor_filtriranja = input('----------------------\nUnesite atribut '
                                  'koji zelite da filtrirate:\n'
                                  '1-naziv\n'
                                  '2-ocjena\n'
                                  '3-godina\n'
                                  '4-izdavac\n'
                                  '5-zanr\n')
        if izbor_filtriranja == '1':
            naziv = input('----------------------\n'
                          'Unesite rijec/slovo kojim pocinje naziv: ')
            for dict_igrica in list_dict_igrice:
                if naziv == dict_igrica['naziv'][0:len(naziv)].lower():
                    print('sledeca igrica/e zadovoljava filter')
                    print(dict_igrica)

    if main_petlja == '3':
        print('Izabrao je izlaz iz programa')
        break
