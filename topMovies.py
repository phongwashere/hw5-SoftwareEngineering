import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/trending/movie/day"
API_KEY = os.getenv("API_KEY")
params = {
    "api_key": API_KEY,
    "total_results": 1
}

response = requests.get(
    BASE_URL,
    params = params,
)

movies = response.json()

for movie in movies:
    print(movie)