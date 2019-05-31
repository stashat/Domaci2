#
i = input("Unesite br igrice: ")
one_game = []
with open("igrice.txt", 'r') as f:
    #for line in f:
        igrice = f.readlines()
        igrice = [x.strip() for x in igrice]
        print(igrice)


one_game.append(igrice[i])
print(one_game)