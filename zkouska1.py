import math

def statistika(rezim, cisla):
    # 1. Nejdřív vyřešíme prázdný seznam (kromě součtu a počtu, ty mají být 0)
    # Pokud je seznam prázdný, nemůžeme hledat max/min/průměr -> vracíme None
    if not cisla:
        if rezim == "soucet" or rezim == "pocet":
            return 0
        return None

    # 2. Režim SOUČET (Sum)
    if rezim == "soucet":
        vysledek = 0
        for cislo in cisla:      # Projdi každé číslo
            vysledek += cislo    # Přičti ho k výsledku
        return vysledek

    # 3. Režim POČET (Count)
    elif rezim == "pocet":
        pocitadlo = 0
        for cislo in cisla:      # Projdi každé číslo
            pocitadlo += 1       # Zvyš počítadlo o 1 (čárkař)
        return pocitadlo

    # 4. Režim MAX (Maximum)
    elif rezim == "max":
        nejvetsi = cisla[0]      # Tipnu si, že první je největší
        for cislo in cisla:
            if cislo > nejvetsi: # Když najdu větší...
                nejvetsi = cislo # ...tak si ho zapamatuju
        return nejvetsi

    # 5. Režim MIN (Minimum)
    elif rezim == "min":
        nejmensi = cisla[0]      # Tipnu si, že první je nejmenší
        for cislo in cisla:
            if cislo < nejmensi: # Když najdu menší...
                nejmensi = cislo # ...tak si ho zapamatuju
        return nejmensi

    # 6. Režim PRŮMĚR (Average)
    elif rezim == "prumer":
        # Spočítám součet a počet ručně (jako nahoře)
        soucet_cisel = 0
        pocet_cisel = 0
        for cislo in cisla:
            soucet_cisel += cislo
            pocet_cisel += 1
        
        # Vydělím to
        return soucet_cisel / pocet_cisel

    # Pokud zadali nesmyslný režim
    return None

# --- Testovací část ---
if __name__ == "__main__":
    def test_statistika():
        assert statistika("soucet", [1, 2, 3, 4]) == 10
        assert statistika("soucet", [-1, -2, -3]) == -6
        assert statistika("soucet", []) == 0
        assert statistika("pocet", [1, 2, 3]) == 3
        assert statistika("pocet", []) == 0
        assert statistika("max", [1, 9, 3]) == 9
        assert statistika("max", [-10, -2, -30]) == -2
        assert statistika("max", []) is None
        assert statistika("min", [1, 9, 3]) == 1
        assert statistika("min", [-10, -2, -30]) == -30
        assert statistika("min", []) is None
        assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
        assert math.isclose(statistika("prumer", [1, 2]), 1.5)
        assert statistika("prumer", []) is None
        assert statistika("neco", [1, 2, 3]) is None
        print("Všechny testy prošly OK!")

    test_statistika()