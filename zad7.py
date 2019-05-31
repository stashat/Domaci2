#
# unos = input("Unesite igricu: ")

with open("igrice.txt", 'r') as f:
    for line in f:
        print(line, end = '')