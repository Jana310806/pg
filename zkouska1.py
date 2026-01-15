import math

def statistika(rezim, cisla):
    
    if not cisla:
        if rezim == "soucet" or rezim == "pocet":
            return 0
        return None

    if rezim == "soucet":
        vysledek = 0
        for cislo in cisla:      
            vysledek += cislo    
        return vysledek

    elif rezim == "pocet":
        pocitadlo = 0
        for cislo in cisla:      
            pocitadlo += 1       
        return pocitadlo


    elif rezim == "max":
        nejvetsi = cisla[0]      
        for cislo in cisla:
            if cislo > nejvetsi: 
                nejvetsi = cislo 
        return nejvetsi

    
    elif rezim == "min":
        nejmensi = cisla[0]      
        for cislo in cisla:
            if cislo < nejmensi: 
                nejmensi = cislo 
        return nejmensi

    
    elif rezim == "prumer":
        
        soucet_cisel = 0
        pocet_cisel = 0
        for cislo in cisla:
            soucet_cisel += cislo
            pocet_cisel += 1
        
        
        return soucet_cisel / pocet_cisel

    return None


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


if __name__ == "__main__":
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))