class Clasa1:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def adauga_culoare(self, culoare):
        self.culoare = culoare

    def afisare_culoare(self):
        print(self.culoare)


class Clasa2(Clasa1):
    def adauga_scaune_incalzite(self, scaune_incalzite):
        self.scaune_incalzite = scaune_incalzite


class Clasa3(Clasa1):
    def adauga_blocuri_optice_led(self, blocuri_optice_led):
        self.blocuri_optice_led = blocuri_optice_led


# Verificări
obiect1 = Clasa2("ARO", "M461")
obiect1.adauga_scaune_incalzite("Nu")
obiect1.adauga_culoare("Rosu")
obiect1.afisare_culoare()

obiect2 = Clasa3("Dacia", "1310")
obiect2.adauga_blocuri_optice_led("Nu")
obiect2.adauga_culoare("Negru")
obiect2.afisare_culoare()

print(obiect1.culoare)
print(obiect2.blocuri_optice_led)
print(obiect1.scaune_incalzite)
print(obiect1.marca)
print(obiect1.tip)
print(obiect2.culoare)
print(obiect2.blocuri_optice_led)
print(obiect2.marca)
print(obiect2.tip)