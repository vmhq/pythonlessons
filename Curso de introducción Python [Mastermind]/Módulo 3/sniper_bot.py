from requests_html import HTMLSession
from time import sleep


def check_stock(url):
    session = HTMLSession()
    r = session.get(url)
    buy_zone = r.html.find(".js-mailalert")
    if len(buy_zone) > 0:
        print("No hay stock 😔")
        return False  # Retorna False cuando no hay stock
    else:
        print("¡Hay stock! 🎉")
        return True  # Retorna True cuando hay stock


url = "https://n1g.cl/Home/computacion/2410-msi-ventus-geforce-rtx-4060-8gb-gddr6-pci-express-40-x8-atx-video-card-rtx-4060-ventus-2x-black-8g-oc.html"


def main():
    while not check_stock(url):  # Continúa mientras no haya stock
        sleep(60)  # Espera 60 segundos antes de volver a comprobar el stock


if __name__ == "__main__":
    main()
