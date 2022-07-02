from bs4 import BeautifulSoup
import requests
import pdb

url = "https://news.ycombinator.com/"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
raw_titles = soup.find_all(name="a", class_="titlelink")
titles = [t.text for t in raw_titles]
links = [l.get("href") for l in raw_titles]
scores = [int(s.text.split()[0]) for s in soup.find_all(name="span", class_="score")]
top_score = max(scores)
index = scores.index(top_score)
print(links[index], titles[index], top_score)
