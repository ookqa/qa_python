from main import BooksCollector

import pytest


class TestBooksCollector:

    # проверяем количество добавленных в тесте книг
    def test_add_new_book_add_three_books_got_list_with_3_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Всё о питонах')
        result = collector.get_books_genre()
        assert len(result) == 3

    # проверка добавления книг с допустимым количеством символов в имени
    @pytest.mark.parametrize('name', ['Ы', 'Мы', 'Трое в лодке', 'Книга символов. Часть 39. 1234567890000', 'Книга символов. Часть 40. 12345678900000'])
    def test_add_new_book_no_genre_book_added(self, collector, name):
        collector.add_new_book(name)
        result = collector.get_books_genre()
        assert len(result) == 1

    # проверяем невозможность добавить книгу без имени
    def test_add_new_book_zero_len_name_book_not_added(self, collector):
        collector.add_new_book('')
        result = collector.get_books_genre()
        assert len(result) == 0

    # проверяем невозможность добавить книгу с именем, содержащим более 40 символов
    def test_add_new_book_41_len_name_book_not_added(self, collector):
        collector.add_new_book('Книга символов. Часть 41. 123456789000000')
        result = collector.get_books_genre()
        assert len(result) == 0

    # проверяем невозможность добавить две книги с одинаковым именем
    def test_add_new_book_two_books_with_same_name_added_once(self, collector):
        collector.add_new_book('Уникальное имя')
        collector.add_new_book('Уникальное имя')
        result = collector.get_books_genre()
        assert result == {'Уникальное имя': ''}

    ### проверки для устанавливания жанра книге ###

    # проверка устанавливания жанра если книга есть в словаре и её жанр входит в список
    def test_set_book_genre_actual_book_and_genre_genre_set(self, collector):
        book_name = 'Книга с таким названием. Часть 2'
        book_genre = 'Детективы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        result = collector.get_books_genre()
        assert result == {'Книга с таким названием. Часть 2': 'Детективы'}

    # проверка устанавливания книге несуществующего жанра
    def test_set_book_genre_actual_book_and_nonexistent_genre_genre_not_set(self, collector):
        book_name = 'Книга без жанра'
        book_genre = 'Комиксы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        result = collector.get_books_genre()
        assert result == {'Книга без жанра': ''}

    # проверка устанавливания жанра несуществующей книге
    def test_set_book_genre_nonexistent_book_result_is_none(self, collector):
        book_genre = 'Комедии'
        book_name = 'Nonexistent book'
        collector.set_book_genre(book_name, book_genre)
        result = collector.get_book_genre(book_name)
        assert result is None

    ### проверки для получния жанра по имени книги ###

    # проверка получения жанра если книга есть в словаре и жанр входит в список жанров
    def test_get_book_genre_actual_book_and_genre_got_genre(self, collector):
        book_name = 'Ужасы нашего городка'
        book_genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre('Ужасы нашего городка') == 'Ужасы'

    # проверка получения жанра если книга есть в словаре, но жанр не входит в список жанров
    def test_get_book_genre_actual_book_nonexistent_genre_empty_list(self, collector):
        book_name = 'Как вселить уверенность'
        book_genre = 'Комиксы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre('Как вселить уверенность') == ''

    ### проверки вывода списка книг с определенным жанром ###
    def test_get_books_with_specific_genre_actual_books_and_genres_got_specific_genre_books_list(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_new_book('Юмористическая книга')
        collector_with_books_and_genres.set_book_genre('Юмористическая книга', 'Комедии')
        assert collector_with_books_and_genres.get_books_with_specific_genre('Комедии') == ['Комедийная книга', 'Юмористическая книга']

    ### проверки вывода текущего словаря с добавленными книгами и отображением жанров для каждой из них ###

    # проверка не пустого словаря
    def test_get_books_genre_five_books_with_genres_got_list_with_five_books(self, collector_with_books_and_genres):
        result = collector_with_books_and_genres.get_books_genre()
        assert result == {'Фантастическая книга': 'Фантастика', 'Ужасная книга': 'Ужасы', 'Детективная книга': 'Детективы', 'Мультипликационная книга': 'Мультфильмы', 'Комедийная книга': 'Комедии'}

    # проверка пустого словаря
    def test_get_books_genre_empty_list_is_empty(self, collector):
        assert collector.get_books_genre() == {}

    ### проверки вывода списка книг которые подходят детям ###

    # проверка для списка книг в котором есть и книги для детей, и книги с возрастным рейтингом
    def test_get_books_for_children_books_with_all_genres_got_children_books_list(self, collector_with_books_and_genres):
        assert collector_with_books_and_genres.get_books_for_children() == ['Фантастическая книга', 'Мультипликационная книга',
                                                                 'Комедийная книга']

    # проверка для списка в котором лишь книги с возрастным ограничением
    def test_get_books_for_children_books_with_age_rating_empty_list(self, collector):
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        collector.add_new_book('Детективная книга')
        collector.set_book_genre('Детективная книга', 'Детективы')
        assert collector.get_books_for_children() == []

    ### проверки добавления книги в избранное ###

    # проверка для книги которая есть в словаре
    def test_add_book_in_favorites_actual_book_with_genre_added_in_list(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Детективная книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == ['Детективная книга']

    # проверка кейса, когда книги нет в словаре
    def test_add_book_in_favorites_book_not_in_list_not_added(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Призрачная книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == []

    # проверка попытки повторного добавления книги в избранное
    def test_add_book_in_favorites_same_book_again_added_once(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Комедийная книга')
        collector_with_books_and_genres.add_book_in_favorites('Комедийная книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == ['Комедийная книга']

    ### проверки удаления книги из избранного ###
    def test_delete_book_from_favorites_actual_book_deleted(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Ужасная книга')
        collector_with_books_and_genres.add_book_in_favorites('Комедийная книга')
        collector_with_books_and_genres.delete_book_from_favorites('Ужасная книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == ['Комедийная книга']

    # проверка попытки удаления книги не из избранного
    def test_delete_book_from_favorites_book_not_from_favorites_list_unchanged(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Мультипликационная книга')
        collector_with_books_and_genres.delete_book_from_favorites('Ужасная книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == ['Мультипликационная книга']

    ### проверка получения списка избранных книги ###
    def test_get_list_of_favorites_books_got_list(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Детективная книга')
        collector_with_books_and_genres.add_book_in_favorites('Фантастическая книга')
        result = collector_with_books_and_genres.get_list_of_favorites_books()
        assert result == ['Детективная книга', 'Фантастическая книга']
