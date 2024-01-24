from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_three_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем три книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Всё о питонах')

        # проверяем, что добавилось именно три
        # словарь books_genre содержит три элемента
        assert len(collector.books_genre) == 3

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_zero_len_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_41_len_name(self):
        collector = BooksCollector()
        collector.add_new_book('one 4567890123456789012345678901234567890')
        assert len(collector.books_genre) == 0

    def test_add_new_book_exactly_that_book_name(self):
        collector = BooksCollector()
        book_name = 'Книга с таким названием. Часть 1'
        collector.add_new_book(book_name)
        assert 'Книга с таким названием. Часть 1' in collector.books_genre

