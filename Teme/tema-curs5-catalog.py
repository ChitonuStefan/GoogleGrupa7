class catalog:
    def init(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0
        pass

    def str(self):
        return f"Numarul de absente: {self.absente} "

    def inc_absente(self):
        self.absente +=1

    def sterge_absente(self, nr_abs):
        self.nr_abs = nr_abs
        if self.absente - nr_abs <= 0:
            self.absente = 0
        else:
            self.absente = self.absente - nr_abs

class extensie1(catalog):
    def adauga_materie(self, materie, note):
        self.materii[materie] = note

    def afiseaza_materii(self):
        for materia in self.materii:
            print(materia)

    def afiseaza_medii(self):
        for materia, note in self.materii.items():
            numere = [x for x in note if isinstance(x, int)]
            if numere:
                medie = sum(numere) / len(numere)
                print(f"Materia: {materia}, Medie: {medie}")

# Verificări

lon_roata = extensie1("Ion", "Roata")
lon_roata.inc_absente()
lon_roata.inc_absente()
lon_roata.inc_absente()
lon_roata.sterge_absente(5)

george_cerc = extensie1("George", "Cerc")
george_cerc.inc_absente()
george_cerc.inc_absente()
george_cerc.inc_absente()
george_cerc.inc_absente()
george_cerc.sterge_absente(2)

print(lon_roata)
print(george_cerc)

lon_roata.adauga_materie("Python", [9, 7, 8])
george_cerc.adauga_materie("Python", [10, 8, 9])

lon_roata.adauga_materie("Romana", [6, 7, 5])
george_cerc.adauga_materie("Matematica", [9, 8, 10])

lon_roata.afiseaza_materii()
george_cerc.afiseaza_materii()

lon_roata.afiseaza_medii()
george_cerc.afiseaza_medii()