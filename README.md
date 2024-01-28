# Юнит-тесты для поверки приложения BooksCollector

Тесты реализованы с использованием **pytest** и проверяют все методы класса `BooksCollector`.
Сами тесты хранятся в `tests.py`.

Тесты используют следующие фикстуры из `conftest.py`:
- `collector` - создание объекта класса
- `collector_with_books_and_genres` - добавление книг и устанавливание им жанров


### Как запустить тесты:

```
pytest -v tests.py
```

### Список тестовых методов:

- `test_add_new_book_add_three_books_got_list_with_3_books` - добавляет три книги и проверяет их количество в словаре
- `test_add_new_book_no_genre_book_added` - параметрический тест, проверяет добавление книг с допустимым количеством символов в имени
- `test_add_new_book_zero_len_name_book_not_added` - проверяет невозможность добавления книги без имени
- `test_add_new_book_41_len_name_book_not_added` - проверяет невозможность добавить книгу с именем, содержащим более 40 символов
- `test_add_new_book_two_books_with_same_name_added_once`- проверяет, что книгу с одинаковым именем можно добавить лишь один раз
- `test_set_book_genre_actual_book_and_genre_genre_set` - проверяет устанавливание жанра, если книга есть в словаре и её жанр входит в список
- `test_set_book_genre_actual_book_and_nonexistent_genre_genre_not_set` - проверяет попытку устанавливания книге несуществующего жанра
- `test_set_book_genre_nonexistent_book_result_is_none` - проверяет устанавливание жанра несуществующей книге
- `test_get_book_genre_actual_book_and_genre_got_genre` - проверяет получения жанра если книга есть в словаре и жанр входит в список жанров
- `test_get_book_genre_actual_book_nonexistent_genre_empty_list` - проверяет получение жанра если книга есть в словаре, но жанр не входит в список жанров
- `test_get_books_with_specific_genre_actual_books_and_genres_got_specific_genre_books_list` - проверяет вывод списка книг с определенным жанром
- `test_get_books_genre_five_books_with_genres_got_list_with_five_books` - проверяет вывод текущего словаря с добавленными книгами и отображением жанров для каждой из них
- `test_get_books_genre_empty_list_is_empty` - проверяет вывод пустого словаря
- `test_get_books_for_children_books_with_all_genres_got_children_books_list` - проверяет вывод списка книг в котором есть и книги для детей, и книги с возрастным рейтингом
- `test_get_books_for_children_books_with_age_rating_empty_list` - проверяет вывод пустого списка если в словаре лишь книги с возрастным ограничением
- `test_add_book_in_favorites_actual_book_with_genre_added_in_list` - проверяет добавление в избранное книги из словаря
- `test_add_book_in_favorites_book_not_in_list_not_added` - проверяет невозможность добавления в избранное книги не из словаря
- `test_add_book_in_favorites_same_book_again_added_once` - проверяет невозможность повторного добавления книги в избранное
- `test_delete_book_from_favorites_actual_book_deleted` - проверяет удаление добавленной в избранное книги из избранного
- `test_delete_book_from_favorites_book_not_from_favorites_list_unchanged` - проверяет невозможность удаления из избраннного книги, не добавленной в избранное
- `test_get_list_of_favorites_books_got_list` - проверяет получения списка избранных книги