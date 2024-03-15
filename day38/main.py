from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
title_tag = soup.find_all(name="span", class_="titleline")

article_text = []
article_link = []

for title in title_tag:
    text = title.find("a").getText()
    article_text.append(text)
    link = title.find("a").get("href")
    article_link.append(link)

article_points = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

highest_point = max(article_points)
article_text_index = article_points.index(highest_point)
print(highest_point)
print(article_text[article_text_index])

# print(article_text)
# print(article_link)
# print(article_points)
