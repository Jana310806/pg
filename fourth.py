def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    start = figurka["pozice"]
    r1, s1 = start
    r2, s2 = cilova_pozice

    # 1️⃣ Kontrola, že cílová pozice je na šachovnici
    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    # 2️⃣ Kontrola, že cílová pozice není obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Pomocné rozdíly
    dr = r2 - r1
    ds = s2 - s1

    # 3️⃣ Pravidla pro jednotlivé figury
    if typ == "pěšec":
        # Pěšec se hýbe jen dopředu (z nižšího na vyšší řádek)
        if s1 != s2:
            return False
        # Jedno pole vpřed
        if dr == 1 and (r1 + 1, s1) not in obsazene_pozice:
            return True
        # Dvě pole vpřed z výchozí pozice (řádek 2)
        if r1 == 2 and dr == 2 and (r1 + 1, s1) not in obsazene_pozice and (r1 + 2, s1) not in obsazene_pozice:
            return True
        return False

    elif typ == "jezdec":
        return (abs(dr), abs(ds)) in [(1, 2), (2, 1)]

    elif typ == "věž":
        if r1 != r2 and s1 != s2:
            return False
        # kontrola, že v cestě není žádná figura
        if r1 == r2:
            step = 1 if s2 > s1 else -1
            for c in range(s1 + step, s2, step):
                if (r1, c) in obsazene_pozice:
                    return False
        else:
            step = 1 if r2 > r1 else -1
            for r in range(r1 + step, r2, step):
                if (r, s1) in obsazene_pozice:
                    return False
        return True

    elif typ == "střelec":
        if abs(dr) != abs(ds):
            return False
        step_r = 1 if dr > 0 else -1
        step_s = 1 if ds > 0 else -1
        for i in range(1, abs(dr)):
            if (r1 + i * step_r, s1 + i * step_s) in obsazene_pozice:
                return False
        return True

    elif typ == "dáma":
        # Dáma = kombinace věže a střelce
        if r1 == r2 or s1 == s2:
            # pohyb jako věž
            if r1 == r2:
                step = 1 if s2 > s1 else -1
                for c in range(s1 + step, s2, step):
                    if (r1, c) in obsazene_pozice:
                        return False
            else:
                step = 1 if r2 > r1 else -1
                for r in range(r1 + step, r2, step):
                    if (r, s1) in obsazene_pozice:
                        return False
            return True
        elif abs(dr) == abs(ds):
            # pohyb jako střelec
            step_r = 1 if dr > 0 else -1
            step_s = 1 if ds > 0 else -1
            for i in range(1, abs(dr)):
                if (r1 + i * step_r, s1 + i * step_s) in obsazene_pozice:
                    return False
            return True
        else:
            return False

    elif typ == "král":
        return abs(dr) <= 1 and abs(ds) <= 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
