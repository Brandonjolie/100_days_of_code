import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")
titles = [t.text for t in soup.find_all(name="h3", class_="title")]
titles.reverse()
with open("movies.txt", "w") as i:
    for line in titles:
        i.write(line + "\n")
