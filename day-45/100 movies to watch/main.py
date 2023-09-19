import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
all_movie_titles = [movie.getText() for movie in all_movies]

with open("movies.txt", "w") as file:
    for movie in all_movie_titles[::-1]:
        file.write(f"{movie}\n")
