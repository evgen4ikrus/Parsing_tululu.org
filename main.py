from urllib import response
import requests


for i in range(10):
    url = f'https://tululu.org/txt.php?id=3216{i}'
    response = requests.get(url)
    response.raise_for_status()

    filename = f'book{i}.txt'
    with open(f'books/{filename}', 'w') as file:
        file.write(response.text)
        