# funkce zkontroluje, zda je cislo sude nebo liche
# a vypise:
# - "Cislo X je sude"
# - "Cislo X je liche"
def sudy_nebo_lichy(cislo):
    if cislo %2 == 0:
        print(f"Cislo {cislo} je sude")
    elif cislo == 0:
        print(f"Cislo {cislo} je 0")
    else:
        print(f"Cislo {cislo} je liche")

      

if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)