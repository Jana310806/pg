def cislo_text(cislo):
    # převod vstupu na celé číslo
    cislo = int(cislo)

    # slovníky pro základní čísla
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět",
                "šest", "sedm", "osm", "devět"]
    teen = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
            "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát",
               "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    # vlastní převod
    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return teen[cislo - 10]
    elif cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + jednotky[jednotka]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah (0–100)."

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)