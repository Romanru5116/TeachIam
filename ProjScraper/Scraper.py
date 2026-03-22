# считаем вхождения слов на сайтах
#логика
#Основные компоненты скрапинга: 
#Библиотека `requests`: загружает HTML.
#Библиотека `BeautifulSoup`: находит данные по тегам (soup.find, soup.find_all).
#Заголовки (headers): имитация браузера (User-Agent), чтобы избежать блокировки.
#Паузы (time.sleep): задержка между запросами, чтобы не перегружать сервер. 

import requests
from bs4 import BeautifulSoup

# URL сайта, который хотим скрапить
url = 'https://yandex.ru'

# Отправляем запрос на сайт
response = requests.get(url)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Парсим HTML-контент
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим заголовок страницы (тег <h1>)
    title = soup.find('h1').text
    print(f'Заголовок сайта: {title}')
    
    # Можно найти и другие данные, например, все ссылки
    # links = soup.find_all('a')
else:
    print('Не удалось получить доступ к сайту')
