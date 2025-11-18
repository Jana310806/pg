import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    # 1) stáhneme stránku
    response = requests.get(url)

    # 2) ověříme status 200
    if response.status_code != 200:
        print(f"Chyba: server vratil status {response.status_code}")
        return hrefs

    # 3) načteme obsah stránky jako text
    html = response.text

    # 4) regulární výraz pro hledání <a href="něco">
    hrefs = re.findall(r'<a[^>]+href="([^"]+)"', html)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        # výpis nalezených odkazů
        for h in hrefs:
            print(h)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
