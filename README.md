# BookCollectoin - тесты
Тесты написаны с помощью pytest для класса BookCollector
# Запуск
 -Bash
 python -m pytest -v tests.py
# Тесты проверяют 
 1. Работу с книгами 
    test_add_new_book_add_two_books - добляет 2 книги
    test_add_new_book_add_duplicate_book_not_added - дублирующая книга не добавляется
    test_add_new_book_valid_length_added - добавляются книги с корректной длиной названия
    test_add_new_book_invalid_length_not_added - не добавляются книги с пустыми или слишком длинным названием
 2. Жанры
    test_set_book_genre_set_valid_genre - устанавливается жанр из списка
    test_set_book_genre_set_invalid_genre_not_set - не устанавливается жанр не из списка
    test_set_book_genre_all_valid_genres_set - проверяются все жанры из списка
    test_get_book_genre_get_genre_by_name - возвращается жанр книги по названию
    test_get_books_with_specific_genre_return_books_of_genre - возвращаются книги нужного жанра
    test_get_books_genre_return_full_dict - возвращается весь словарь книг
3. Книги для детей
    test_get_books_for_children_exclude_adult_genre - жанры с возврастным рейтингом не попадают
    test_get_books_for_children_returns_empty_when_all_adult - если все книги с взрослым рейтингом, то список пуст
4. Избранное 
    test_add_book_in_favorites_add_boo - книга добавляется в избранное
    test_add_book_in_favorites_book_not_in_genre_not_added - книга не из списка не добавляется в избранное 
    test_add_book_in_favorites_duplicate_not_added - повторно не добавляется книга в избранное
    test_delete_book_from_favorites_remove_book - удаление книги из избранного
    test_delete_book_from_favorites_book_not_in_favorites_not_error - удаление несуществующей книги не вызывает ошибку
    test_get_list_of_favorites_books_return_list - возвращает список избранных книг
5. Параметризация
    в тестах используется параметризация для проверки нескольких значений одной логикой
    - длина названия книги
    - все жангры из списка
    = жанры с возрастным рейтингом