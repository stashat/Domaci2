#i = int(input("Unesite br igrice: "))
one_game = []
imena = []
ocjene = []
godine = []
with open("igrice.txt", 'r') as f:
    igrice = f.readlines()
    igrice = [x.strip() for x in igrice]
    print(igrice)
    for i in igrice:
        one_game = i.split(';')
        imena.append(one_game[0])
        ocjene.append(one_game[1])
        godine.append(one_game[2])
        
        print(one_game)

print(imena)
print(ocjene)
print(godine)

imena_filter = list(filter(lambda x: 2<len(x)<50, imena ))
print(imena_filter)
ocjene_filter = list(filter(lambda x: 1<x<10, ocjene))
print(ocjene_filter)