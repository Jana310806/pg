def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    # Převeďme vstup na řetězec (aby fungovalo pro int i str)
    s = str(binarni_cislo).strip()
    if s == "":
        return 0
    # Ověření, že řetězec obsahuje pouze '0' a '1'
    if any(ch not in "01" for ch in s):
        raise ValueError("Neplatné binární číslo: musí obsahovat pouze 0 a 1")
    # Použijeme vestavěnou konverzi se základem 2
    return int(s, 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128