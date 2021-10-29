from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)
yc = response.text

soup = BeautifulSoup(yc, 'html.parser')

article_texts = []
article_links = []
article_scores = []

articles = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_scores = [int(score.getText().split()[0]) for score in scores]

max_score_index = article_scores.index(max(article_scores))
print(f"'{article_texts[max_score_index]}' [{article_links[max_score_index]}]")