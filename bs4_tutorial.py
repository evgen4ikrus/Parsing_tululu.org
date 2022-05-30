from bs4 import BeautifulSoup
import requests


url = 'https://www.franksonnenbergonline.com/blog/are-you-grateful/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
title_tag = soup.find('main').find('header').find('h1')
title_text = title_tag.text
pictures_link = soup.find('img', class_='attachment-post-image')['src']
post_text_tag = soup.find('div', class_='entry-content')
post_text = post_text_tag.text
print(title_text, pictures_link, post_text, sep='\n')