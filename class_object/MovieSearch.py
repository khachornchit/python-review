import requests
import json


class MovieSearch:
    def __init__(self, movies):
        self.movies = movies

    def get_keywords(self, query):
        words = query.split()
        keywords = [' '.join(words[i:j + 1]) for i in range(len(words))
                    for j in range(i, len(words))]
        return sorted(keywords, key=len, reverse=True)

    def search_by_keyword(self, keyword):
        return [movie for movie in self.movies if 'title' in movie and keyword.lower() in movie['title'].lower()]

    def search_query(self, query):
        keywords = self.get_keywords(query)
        results = []
        for keyword in keywords:
            results = self.search_by_keyword(keyword)
            if results:
                return keywords, results
        return keywords, results
