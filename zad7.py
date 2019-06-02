import math
import datetime
zanrovi = ['action', 'historic', 'shooter', 'first-person', 'sci-fi']

# funkcije


def print_filtered(list_dict_igr):
    if len(list_dict_igr) > 0:
        print('Sledeca igrica/e zadovoljava filter:'
              '\n----------------------')
        for igr in list_dict_igr:
            print(igr)
    else:
        print('Nijedna igrica ne zadovoljava filter'
              '\n----------------------')
    return True


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
    if (set(map(lambda x: x.lower(), zanr.split(', '))) <= set(zanrovi) and
            len(zanr.split(', ')) <= 3):
        return True
    return False

# fajl
with open("igrice.txt", 'r') as f:
    igrice = f.readlines()
    igrice = [x.strip() for x in igrice]
igrice_split = []
for igra in igrice:
    igrice_split.append(igra.split(';'))

# filtriranje fajla
igrice_filter = []
for igra in igrice_split:
    if (chk_naziv(igra[0]) and chk_ocjena(igra[1]) and chk_godina(igra[2]) and
            chk_izdavac(igra[3]) and chk_zanrovi(igra[4])):
        igrice_filter.append(igra)


# dictionary
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

# korisnicki dio - glavna petlja
while True:
    print('\n----------Filtrirane igrice----------')
    for i in list_dict_igrice:
        print(i)
    main_petlja = input('---------------------------------\nIzaberi:\n1-za '
                        'unos novoe igrice\n2-za filtriranje\n3-za izlaz iz '
                        'programa\n')
    if main_petlja == '1':
        unos_igre = input('Unesite igru u obliku naziv;ocjena;godina;izdavac;'
                          'zanr (dostupni zanrovi su action, historic, '
                          'shooter, first-person, sci-fi):\n')
        unesena_igra = unos_igre.split(';')
        if len(unesena_igra) < 5:
            print('Niste unijeli sve atribute. Ponovo pokrenite program.')
            break
        if (chk_naziv(unesena_igra[0]) and
                chk_ocjena(unesena_igra[1]) and
                chk_godina(unesena_igra[2]) and
                chk_izdavac(unesena_igra[3]) and
                chk_zanrovi(unesena_igra[4])):
            igrice_filter.append(unesena_igra)
            with open("igrice.txt", 'a') as f:
                f.write('\n'+unos_igre)
            list_dict_igrice.append({
                'naziv':   unesena_igra[0],
                'ocjena':  unesena_igra[1],
                'godina':  unesena_igra[2],
                'izdavac': unesena_igra[3],
                'zanrovi': unesena_igra[4]
            })
            print('------------------\nIgrica je dodata\n--------------------')
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
        # filtriranje
        izbor_filtriranja = input('----------------------\nUnesite atribut '
                                  'koji zelite da filtrirate:\n'
                                  '1-naziv\n'
                                  '2-ocjena\n'
                                  '3-godina\n'
                                  '4-izdavac\n'
                                  '5-zanr\n')
        # filtriranje po nazivu
        if izbor_filtriranja == '1':
            naziv = input('----------------------\n'
                          'Unesite rijec/slovo kojim pocinje naziv: ')
            dict_igrice_filt = []
            for dict_igrica in list_dict_igrice:
                if naziv == dict_igrica['naziv'][0:len(naziv)].lower():
                    dict_igrice_filt.append(dict_igrica)
            print_filtered(dict_igrice_filt)

        # filtriranje po ocjeni
        if izbor_filtriranja == '2':
            ocjena = input('----------------------\n'
                           'Unesite ocjenu (broj od 1 do 10) : ')
            dict_igrice_filt = []
            for dict_igrica in list_dict_igrice:
                if ocjena < dict_igrica['ocjena']:
                    dict_igrice_filt.append(dict_igrica)
            print_filtered(dict_igrice_filt)

        # filtriranje po godini
        if izbor_filtriranja == '3':
            izbor_godine = input('Zelite li da prikazete igrice:'
                                 '\n1-poslije unesene godine'
                                 '\n2-prije unesene godine\n')
            if izbor_godine == '1':
                godina_poslije = input('Unesite godinu: ')
                dict_igrice_filt = []
                for dict_igrica in list_dict_igrice:
                    if godina_poslije < dict_igrica['godina']:
                        dict_igrice_filt.append(dict_igrica)
                print_filtered(dict_igrice_filt)
            if izbor_godine == '2':
                dict_igrice_filt = []
                godina_prije = input('Unesite godinu: ')
                dict_igrice_filt = []
                for dict_igrica in list_dict_igrice:
                    if godina_prije >= dict_igrica['godina']:
                        dict_igrice_filt.append(dict_igrica)
                print_filtered(dict_igrice_filt)
        # filtriranje po izdavacu
        if izbor_filtriranja == '4':
            izdavac = input('Unesite rijec/slovo kojim pocinje '
                            'naziv izdavaca: ')
            dict_igrice_filt = []
            for dict_igrica in list_dict_igrice:
                if izdavac == dict_igrica['izdavac'][0:len(izdavac)].lower():
                    dict_igrice_filt.append(dict_igrica)
            print_filtered(dict_igrice_filt)
        # filtriranje po zanrovima
        if izbor_filtriranja == '5':
            dict_igrice_filt = []
            izbor_zanra = input('Izaberite do 3 zanra za filtriranje:'
                                '\n1- action\n2- historic\n3- shooter'
                                '\n4- first-person\n5- sci-fi\nUnesite brojeve'
                                ' u formi br,br,br: ')
            lista_unesenih_zanrova = []
            for i in izbor_zanra.split(','):
                lista_unesenih_zanrova.append(zanrovi[int(i)-1])
            for dict_igrica in list_dict_igrice:
                if (set(lista_unesenih_zanrova) <=
                        set(dict_igrica['zanrovi'].lower().split(', '))):
                    dict_igrice_filt.append(dict_igrica)
            print_filtered(dict_igrice_filt)
    if main_petlja == '3':
        print('Izlaz iz programa')
        break
