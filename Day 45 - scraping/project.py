import requests
from bs4 import BeautifulSoup

# Close enough since the site actually creates the content dynamically now, so can't be easily scraped

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
titles = [title.get("alt") for title in soup.find_all(name="img", class_="loading")]
titles.reverse()

i = 1
with open("movies.txt", "w") as movies_file:
  for title in titles:
    if title != '' and title != '100 Greatest Movies':
      movies_file.write(f"{i}) {title}\n")
      i += 1