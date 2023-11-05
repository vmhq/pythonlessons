from requests_html import HTMLSession
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    

def login(driver, email, password):
    try:
        # Espera hasta que el campo de email sea localizable y luego llena la información
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(email)

        # Espera hasta que el campo de contraseña sea localizable y luego llena la información
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)

        # Espera hasta que el botón 'Continuar' sea clickeable y luego haz clic
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "continue"))
        )
        continue_button.click()

    except Exception as e:
        print("Hubo un problema al intentar iniciar sesión: ", e)


def open_website(url):
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        # Espera hasta que el botón de añadir al carrito sea clickeable y luego haz clic
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()
        # Ahora, espera hasta que el enlace de pasar por caja sea clickeable y luego haz clic
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Pasar por caja')]"))
        )
        checkout_button.click()
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Pasar por caja')]"))
        )
        checkout_button.click()
        # Espera hasta que el enlace de iniciar sesión sea clickeable y luego haz clic
        sign_in_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-link-action='show-login-form']"))
        )
        sign_in_link.click()
        # Función para iniciar sesión
        login(driver, 'vicentem@vmhq.cl', 'pdf3fdf6ztx7bqg@YQN')

    except Exception as e:
        print("Hubo un problema al ejecutar las acciones en el navegador: ", e)
        driver.close()



url = "https://n1g.cl/Home/computacion/2523-msi-ventus-rtx-4060-video-card-rtx-4060-ventus-2x-white-8g-oc-geforce-.html"


def main():
    while True:  # Crea un bucle infinito
        if check_stock(url):  # Si hay stock...
            open_website(url)  # Abre el sitio web
            break  # Sale del bucle después de abrir el sitio web
        else:
            sleep(60)  # Espera 60 segundos antes de volver a comprobar el stock


if __name__ == "__main__":
    main()
