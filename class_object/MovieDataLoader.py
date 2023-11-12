import requests
import json
from .MovieSearch import MovieSearch


class MovieDataLoader:
    def __init__(self, url_raw_data):
        self.url_raw_data = url_raw_data
        self.movies = []

    def transform_data(self, line):
        def validate_id(line):
            try:
                data = json.loads(line)
                return data.get('_id', {}).get('$oid')
            except (KeyError, json.JSONDecodeError):
                return None

        def validate_title(data):
            return data.get('title', '')

        def validate_year(data):
            try:
                return int(data.get('year', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        def validate_genres(data):
            return data.get('genres', '')

        def validate_tomatoes(data):
            try:
                return int(data.get('tomatoes', {}).get('viewer', {}).get('meter', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        id = validate_id(line)
        with_id = {}
        no_id = {}

        if id:
            data = json.loads(line)

            no_id = {
                "title": validate_title(data),
                "year": validate_year(data),
                "genres": validate_genres(data),
                "rating": validate_tomatoes(data)
            }
            with_id[id] = no_id

        return with_id, no_id

    def load_data_to_movie_dict(self):
        response = requests.get(self.url_raw_data)
        lines = response.text.split("\n")
        with_ids = []
        no_ids = []

        for line in lines:
            with_id, no_id = self.transform_data(line)

            if with_id and no_id:
                with_ids.append(with_id)
                no_ids.append(no_id)

        self.movies = no_ids
        return with_ids, no_ids


if __name__ == "__main__":
    url_raw_data = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    m_loader = MovieDataLoader(url_raw_data)
    with_ids, no_ids = m_loader.load_data_to_movie_dict()

    m_search = MovieSearch(no_ids)
    keywords, results = m_search.search_query("my way")

    print('Keywords:\n', keywords, '\n')
    print('Search results:')
    for movie in results:
        print(movie)
