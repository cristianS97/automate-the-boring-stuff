import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import time
import random
from win10toast import ToastNotifier # pip install win10toast

# URL de consulta
url = 'https://jkanime.net/'

# User-agent tor
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# Objeto para interactuar con las notificaciones de windows
toaster = ToastNotifier()

# Ciclo que consultara hasta encontar el anime solicitado
while True:
    # Consultamos la url
    response = requests.get(url, headers=headers)
    print(f'Estado respuesta: {response.status_code}')
    # Creamos el árbol html
    soup = BeautifulSoup(response.text)

    # Buscamos donde se encuentran los animes
    programacion = soup.find(id='slider3')
    animes = programacion.find_all('a', class_='odd')

    # Variable para comprobar si se encontro le anime buscado
    encontrado = False
    # Recorremos la lista de animes encontrados
    for anime in animes:
        # Obtenemos sus datos
        titulo = anime.find('h2').text.strip()
        episodio = anime.find('span', class_='episode').text.strip()
        estreno = anime.find('i', class_='clock-icon').text.strip()

        # Consultamos si se encontró el ánime deseado
        if 'hanayome' in titulo.lower():
            encontrado = True
            print(titulo)
            print(episodio)
            print(estreno)
            print('=' * 80)
            print()
            # Terminamos el ciclo
            break

    if encontrado:
        # Mensaje que contiene la hora en que se encontró el anime
        mensaje = f'{time.strftime("%H:%M:%S")} -> Estrenado'
        toaster.show_toast('Go Toubun no Hanayome', mensaje, duration=5)
        break

    time.sleep(random.uniform(6.0, 8.0))

print("Fin del programa")