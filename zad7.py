import math
import datetime
zanrovi = ['action','historic','shooter','first-person','sci-fi']

#funkcije
def chk_naziv(naziv):
    if 2<len(naziv)<50:
        return True
    return False

def chk_ocjena(ocjena):
    f_ocjena=float(ocjena)
    if 1<f_ocjena<10 and not ((f_ocjena*100-math.trunc(f_ocjena*100))>0):
        return True
    return False

def chk_godina(godina):
    now = datetime.datetime.now()
    if (now.year+1)>int(godina)>1950:
        return True
    return False

def chk_izdavac(izdavac):
    if 2<len(izdavac)<40:
        return True
    return False

def chk_zanrovi(zanr):
    if set(map(lambda x: x.lower(), zanr.split(', '))) <= set(zanrovi):
        return True
    return False
#fajl
with open("igrice.txt", 'r') as f:
    igrice = f.readlines()
    igrice = [x.strip() for x in igrice]
    #print(igrice)
igrice_split=[]
for igra in igrice:
    igrice_split.append(igra.split(';'))
print(igrice_split)

#filtriranje
igrice_filter = []
for igra in igrice_split:
    if chk_naziv(igra[0]) and chk_ocjena(igra[1]) and chk_godina(igra[2]) and chk_izdavac(igra[3]) and chk_zanrovi(igra[4]):
        igrice_filter.append(igra)
print(igrice_filter)

print('rjecnik-----------')
#dictionary
for i in igrice_filter:
    dict_igrice = {
        'naziv' : i[0],
        'ocjena' : i[1],
        'godina' : i[2],
        'izdavac' : i[3],
        'zanrovi' : i[4]}
    print(dict_igrice['godina'])
'''
print(chk_naziv(igrice_split[0][0]))
print(chk_ocjena(igrice_split[0][1]))
print(chk_godina(igrice_split[0][2]))
print(chk_izdavac(igrice_split[0][3]))
'''

'''
while True:
    main_petlja = input('Izaberi:\n1-za unos novog filma\n2-za filterisanje\n3-za izlaz iz programa\n')
    if main_petlja=='1':
        print('Izabrao je unos novog filma')
    if main_petlja=='2':
        print('Izabrao je filterisanje')
    if main_petlja=='3':
        print('Izabrao je izlaz iz programa')
        break
'''