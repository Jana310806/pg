import sys

def spocitej_statistiku(text):
    # Ošetření: Pokud je text prázdný, vrátíme samé nuly
    if not text:
        return 0, 0, 0
        
    # 1. Počet řádků
    # Použijeme splitlines(), což rozseká text na seznam řádků
    radky = text.splitlines()
    pocet_radku = len(radky)
    
    # 2. Počet slov
    # Funkce split() bez parametrů rozseká text podle mezer a "bílých znaků"
    slova = text.split()
    pocet_slov = len(slova)
    
    # 3. Počet znaků
    # Funkce len() vrátí délku celého řetězce včetně mezer
    pocet_znaku = len(text)

    return pocet_radku, pocet_slov, pocet_znaku


def test_spocitej_statistiku():
    assert spocitej_statistiku("Ahoj svet\nToto je test.") == (2, 5, 23)
    assert spocitej_statistiku("") == (0, 0, 0)
    assert spocitej_statistiku("Jediny radek bez novych radku") == (1, 5, 29)
    assert spocitej_statistiku("Prvni radek\nDruhy radek\nTreti radek") == (3, 6, 35)


if __name__ == "__main__":
    try:
        vstupni_soubor = 'data.txt'
        vystupni_soubor = 'statistika.txt'

        # --- ČÁST 1: NAČTENÍ ---
        # Používám 'with open', aby se soubor sám zavřel
        # encoding='utf-8' je nutné kvůli české diakritice!
        with open(vstupni_soubor, 'r', encoding='utf-8') as f:
            obsah = f.read()
    
        # Spuštění tvé funkce
        pocet_radku, pocet_slov, pocet_znaku = spocitej_statistiku(obsah)

        # --- ČÁST 2: ZÁPIS ---
        with open(vystupni_soubor, 'w', encoding='utf-8') as f:
            f.write(f"Pocet radku: {pocet_radku}\n")
            f.write(f"Pocet slov: {pocet_slov}\n")
            f.write(f"Pocet znaku: {pocet_znaku}\n")

        # volitelne info pro uzivatele
        print("Statistika byla ulozena do souboru", vystupni_soubor)

    except FileNotFoundError:
        print("Vstupni soubor neexistuje")
    except Exception as e: # Přidal jsem 'as e', aby se vypsalo, co se stalo
        print(f"Doslo k chybe pri praci se souborem: {e}")
        
    # Spuštění testů pro kontrolu (nemusí tam být, ale je to dobré pro tebe)
    test_spocitej_statistiku()