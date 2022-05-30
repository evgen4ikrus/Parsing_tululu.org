from urllib import response
import requests
import os


if not os.path.exists('books'):
    os.makedirs('books')


for i in range(10):
    url = f'https://tululu.org/txt.php?id=3216{i}'
    response = requests.get(url)
    response.raise_for_status()

    filename = f'book{i}.txt'
    with open(f'books/{filename}', 'w', encoding="utf-16") as file:
        file.write(response.text)
        