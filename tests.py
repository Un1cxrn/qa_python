import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_duplicate_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Путешествие на запад')
        collector.add_new_book('Путешествие на запад')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', [
        'K', 
        'Книга' * 8,
        'Волшебное название'

    ])

    def test_add_new_book_valid_lenght_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
            '',
            'Книга' * 9,
            'Книга' * 10,
    ])
    def test_add_new_book_invalid_lenght_not_added(self, name):
            collector = BooksCollector()
            collector.add_new_book(name)
            assert name not in collector.get_books_genre()

    def test_set_book_genre_set_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_book_genre_set_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('2030')
        collector.set_book_genre('2030','Биография')
        assert collector.get_book_genre('2030') == ''

    @pytest.mark.parametrize('genre',[
        'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы',
    ])

    def test_set_book_genre_all_valid_genres_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_book_genre('Книга') == genre

    def test_get_book_genre_get_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == "Ужасы"

    def test_get_books_with_specific_genre_return_books_of_genre(self):
        collector = BooksCollector() 
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 2']

    def test_get_books_genre_return_full_dict(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.add_new_book('Книга 2')
         assert collector.get_books_genre() == {'Книга 1': '', 'Книга 2': ''}

    @pytest.mark.parametrize('adult_genre', [
         'Ужасы',
         'Детективы'
    ])

    def test_get_books_for_children_exclude_adult_genre(self, adult_genre):
         collector = BooksCollector()
         collector.add_new_book('Детская книга'),
         collector.add_new_book('Взрослая книга'),
         collector.set_book_genre('Детская книга','Мультфильмы')
         collector.set_book_genre('Взрослая книга', adult_genre)
         assert collector.get_books_for_children() == ['Детская книга']

    def test_get_books_for_children_returns_empty_when_all_adult(self):
         collector = BooksCollector()
         collector.add_new_book('Оно')
         collector.add_new_book('Шерлок')
         collector.set_book_genre('Оно', 'Ужасы')
         collector.set_book_genre('Шерлок', 'Детективы')
         assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_book(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.add_book_in_favorites('Книга 1')
         assert collector.get_list_of_favorites_books() == ['Книга 1']

    def test_add_book_in_favorites_book_not_in_genre_not_added(self):
         collector = BooksCollector()
         collector.add_book_in_favorites('Несуществующая книга')
         assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate_not_added(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.add_book_in_favorites('Книга 1')
         collector.add_book_in_favorites('Книга 1')
         assert collector.get_list_of_favorites_books() == ['Книга 1']

    def test_delete_book_from_favorites_book_not_in_favourites_not_error(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.delete_book_from_favorites('Книга 1')
         assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_remove_book(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.add_book_in_favorites('Книга 1')
         collector.delete_book_from_favorites('Книга 1')
         assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_return_list(self):
         collector = BooksCollector()
         collector.add_new_book('Книга 1')
         collector.add_new_book('Книга 2')
         collector.add_book_in_favorites('Книга 1')
         collector.add_book_in_favorites('Книга 2')
         assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']