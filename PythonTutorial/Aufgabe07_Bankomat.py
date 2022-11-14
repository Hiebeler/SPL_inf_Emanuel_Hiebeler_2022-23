class Bankomat:
    kontostand = 0

    def einzahlen(self, betrag):
        self.kontostand += betrag
        return betrag

    def abheben(self, betrag):
        self.kontostand -= betrag
        return betrag

    def getKontostand(self):
        return self.kontostand
    
print("1. Einzahlen")
print("2. Auszahlen")
print("3. Kontostand")
print("4. Beenden")
bankomat = Bankomat()

while True:
    selection = int(input())
    if selection == 1:
        print("Amount: ")
        print(str(bankomat.einzahlen(int(input()))) + "€ Einbezahlt")
    elif selection == 2:
        print("Amount: ")
        print(str(bankomat.abheben(int(input()))) + "€ Ausbezahlt")
    elif selection == 3:
        print("Kontostand: " + str(bankomat.getKontostand()))
    elif selection == 4:
        break