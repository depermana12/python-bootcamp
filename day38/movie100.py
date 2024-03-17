import requests
from bs4 import BeautifulSoup


target_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=target_url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
title_tag = soup.find_all(name="h3", class_="title")

title_list = [title.getText() for title in title_tag]

# for title in title_tag:
#     tittle_text = title.getText()
#     title_list.append(tittle_text)

title_list.reverse()

with open("top100.txt", "w", encoding="utf8") as file:
    for title in title_list:
        file.write(f"{title}\n")
