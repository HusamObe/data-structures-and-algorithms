import pytest
from Comparisons.movie_sorter import Movie, MovieSorter


@pytest.fixture
def sample_movies():
    return [
        Movie('Inception', 2010, ['Action', 'Adventure', 'Sci-Fi']),
        Movie('The Shawshank Redemption', 1994, ['Drama']),
        Movie('Pulp Fiction', 1994, ['Crime', 'Drama']),
        Movie('The Godfather', 1972, ['Crime', 'Drama']),
        Movie('The Dark Knight Rises', 2012, ['Action', 'Thriller']),
    ]


def test_sort_by_year(sample_movies):
    sorter = MovieSorter()
    sorted_movies = sorter.sort_by_year(sample_movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2012, 2010, 1994, 1994, 1972]


def test_sort_by_title(sample_movies):
    sorter = MovieSorter()
    sorted_movies = sorter.sort_by_title(sample_movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ['Dark Knight Rises', 'Godfather', 'Inception', 'Pulp Fiction', 'Shawshank Redemption']
