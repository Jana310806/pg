from abc import ABC, abstractmethod

class Zamestnanec(ABC):
    def __init__(self, jmeno, zakladni_mzda):
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0

    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    @abstractmethod
    def vypocitej_mzdu(self):
        # Zakladni mzda + 1000 Kc za kazdy odpracovany rok
        bonus = 1000 * self.pocet_odpracovanych_let
        return self.zakladni_mzda + bonus

    def __str__(self):
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"



class Programator(Zamestnanec):
    # Programátor nemá speciální init, takže ho psát nemusím (zdědí se)
    
    def vypocitej_mzdu(self):
        # 1. Zavolám rodiče (super), ať mi spočítá základní mzdu i s roky
        zaklad = super().vypocitej_mzdu()
        
        # 2. Programátor má 10% navíc -> vynásobím 1.1
        # Používám int(), aby z toho nebylo desetinné číslo (44000.0)
        return int(zaklad * 1.10)


class Manazer(Zamestnanec):
    def __init__(self, jmeno, zakladni_mzda, pocet_podrizenych):
        # 1. Musím zavolat rodiče, aby nastavil jméno a mzdu
        super().__init__(jmeno, zakladni_mzda)
        # 2. Uložím si navíc počet podřízených
        self.pocet_podrizenych = pocet_podrizenych

    def vypocitej_mzdu(self):
        # 1. Zavolám rodiče pro základní výpočet
        zaklad = super().vypocitej_mzdu()
        
        # 2. Přičtu 1000 Kč za každého podřízeného
        bonus_za_lid = 1000 * self.pocet_podrizenych
        
        return zaklad + bonus_za_lid

# --- KONEC TVÉHO KÓDU ---


if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)

    # Pridame 2 roky praxe
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)