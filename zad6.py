

class Zahtjev:
    def __init__(self, quote, quantity, price, status):
        self.quote = quote
        self.quantity = int(quantity)
        self.price = float(price)
        self.status = status

    def sum_b(self):
        if self.status == 'B':
            return self.price * self.quantity
        else:
            return 0

    def sum_s(self):
        if self.status == 'S':
            return self.price * self.quantity
        else:
            return 0

akcija = input('Unesite ponudu:')
akcija = akcija.split(',')

suma_b = 0
suma_s = 0

for i in akcija:
    akcija = i.split()
    akcija = Zahtjev(akcija[0], akcija[1], akcija[2], akcija[3])
    suma_b += akcija.sum_b()
    suma_s += akcija.sum_s()

suma_B = format(round(suma_b, 2), '.2f')
suma_S = format(round(suma_s, 2), '.2f')
print("Buy: " + suma_B + " Sell: " + suma_S)
