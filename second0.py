def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cislo = int(cislo)

    text_cisel = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["dvacet", "tricet", "ctyricet", "padesat", "sedesat", "sedmdesat", "osmdesat", "devadesat"]

    if cislo <= 19:
        return text_cisel[cislo]
    elif cislo < 100:
        desitky = cislo // 10
        text_cisel = cislo % 10
        if text_cisel == 0:
            return desitky[desitky]
        else:
            return desitky[desitky] + " " + text_cisel[text_cisel]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah (0-100)."
    

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)