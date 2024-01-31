import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def collector_with_books_and_genres(collector):
    # Добавление книг и установка жанров
    collector.add_new_book('Фантастическая книга')
    collector.set_book_genre('Фантастическая книга', 'Фантастика')
    collector.add_new_book('Ужасная книга')
    collector.set_book_genre('Ужасная книга', 'Ужасы')
    collector.add_new_book('Детективная книга')
    collector.set_book_genre('Детективная книга', 'Детективы')
    collector.add_new_book('Мультипликационная книга')
    collector.set_book_genre('Мультипликационная книга', 'Мультфильмы')
    collector.add_new_book('Комедийная книга')
    collector.set_book_genre('Комедийная книга', 'Комедии')
    return collector
