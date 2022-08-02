import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

titles = soup.findAll(name="h3", class_="title")

title_list =[]
for item in titles:
    title = item.getText()
    title_list.append(title)

with open("./movie_list.txt", "w", encoding="utf-8") as file:
    for title in reversed(title_list):
        file.write(f"{title}\n")