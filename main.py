class Mahsulot:
    def yetkazib_berish_narxi(self, shahar):
        raise NotImplementedError

    def chegirma_qollash(self, foydalanuvchi):
        raise NotImplementedError

    def kafolat_muddati(self):
        return None


class Elektronika(Mahsulot):
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

    def yetkazib_berish_narxi(self, shahar):
        return 30000 if shahar == "Toshkent" else 50000

    def chegirma_qollash(self, foydalanuvchi):
        return self.narx * 0.9  

    def kafolat_muddati(self):
        return "12 oy"


class Kiyim(Mahsulot):
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

    def yetkazib_berish_narxi(self, shahar):
        return 15000

    def chegirma_qollash(self, foydalanuvchi):
        return self.narx * 0.95 


class Kitob(Mahsulot):
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

    def yetkazib_berish_narxi(self, shahar):
        return 10000

    def chegirma_qollash(self, foydalanuvchi):
        return self.narx  

savat = [
    Elektronika("Noutbuk", 8000000),
    Kiyim("Kurtka", 300000),
    Kitob("Python", 60000)
]

yetkazib = sum(x.yetkazib_berish_narxi("Toshkent") for x in savat)
chegirmadan_keyin = sum(x.chegirma_qollash("user") for x in savat)

print("Umumiy yetkazib berish narxi:", yetkazib)
print("Chegirmadan keyingi umumiy narx:", chegirmadan_keyin)
print("Noutbuk kafolat muddati:", savat[0].kafolat_muddati())
