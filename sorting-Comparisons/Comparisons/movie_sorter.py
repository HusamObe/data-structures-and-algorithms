class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year}, genres={self.genres})"


class MovieSorter:
    @staticmethod
    def sort_by_year(movies):
        movies.sort(key=lambda x: x.year, reverse=True)
        return movies

    
    def sort_by_title(self, movies):
        def remove_leading_articles(title):
            articles = ["A ", "An ", "The "]
            for article in articles:
                if title.startswith(article):
                    return title[len(article):]
            return title

        movies.sort(key=lambda x: remove_leading_articles(x.title.lower()))
        return movies



movies = [
    Movie('Inception', 2010, ['Action', 'Adventure', 'Sci-Fi']),
    Movie('The Shawshank Redemption', 1994, ['Drama']),
    Movie('Pulp Fiction', 1994, ['Crime', 'Drama']),
    Movie('The Godfather', 1972, ['Crime', 'Drama']),
    Movie('The Dark Knight Rises', 2012, ['Action', 'Thriller']),
]



sorted_by_year = MovieSorter.sort_by_year(movies)
print("Sorted by Year : ")
print(sorted_by_year)

sorted_by_title = MovieSorter.sort_by_title(movies)
print("Sorted by Title: ")
print(sorted_by_title)
