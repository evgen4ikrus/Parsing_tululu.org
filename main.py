import requests
import os


def check_for_redirect(response):
    if response.history != []:
        raise requests.HTTPError('Ответ пришёл с главной, а не с запрошенной страницы')


if not os.path.exists('books'):
    os.makedirs('books')


for i in range(10):
    
    url = f'https://tululu.org/txt.php?id={i}' 
    response = requests.get(url)
    response.raise_for_status()
    
    try:
        check_for_redirect(response)
        filename = f'book {i}.txt'
        with open(f'books/{filename}', 'w', encoding="utf-16") as file:
            file.write(response.text)
    except requests.HTTPError as error:
        print(error)
        