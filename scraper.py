import requests, bs4
from printer import Printer


def main():
    url = "https://clustersweb.andrew.cmu.edu/PrinterStats/All/"

    content = requests.get(url).content

    soup = bs4.BeautifulSoup(content, features="html.parser")

    table = soup.findAll("table")[1].findAll("tr")

    col_tag = ["name", "signal", "lcd_message", "status", "tray_status", "as_of"]

    printers = []

    for row in table[2:]:
        columns = row.find_all("td")
        kwargs = {}
        for c, tag in zip(columns, col_tag):
            if tag == "signal":
                data = c.img["alt"]
            else:
                data = c.get_text()
            kwargs[tag] = data

        printers.append(Printer(**kwargs))

    return printers


if __name__ == "__main__":
    main()