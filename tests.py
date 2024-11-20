from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.fixture
    def books_collector(self):
        collector = BooksCollector()
        books=[['1001 и одна ночь на курсах','Фантастика'],['Граф МонтеКиска', 'Детективы'],['Крипта или иметь здоровый сон', 'Фантастика'],['Оно','Ужасы']]
        for book in books:
            collector.add_new_book(book[0])
            collector.set_book_genre(book[0], book[1])
        return collector

    @pytest.mark.parametrize('name',['','12345678901234567890123456789012345678901'])
    def test_add_new_book_negative_cases(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == None

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_return_book_and_genre(self, genre):
        collector = BooksCollector()
        name='1001 и одна ночь на курсах'
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        assert collector.books_genre == {name: genre}

    def test_set_book_genre_not_in_genre_list(self):
        collector = BooksCollector()
        name='Тони Карк'
        genre = 'Биография'
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        assert collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre_return_two_books(self, books_collector):
        fantasy_books=books_collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2

    def test_get_books_genre_return_genre(self, books_collector):
        assert books_collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_for_children_return_two(self, books_collector):
        assert  len(books_collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_book_in_list_and_not_in_fv(self, books_collector):
        books_collector.add_book_in_favorites('1001 и одна ночь на курсах')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_in_list_and_in_fv(self, books_collector):
        books_collector.add_book_in_favorites('1001 и одна ночь на курсах')
        books_collector.add_book_in_favorites('1001 и одна ночь на курсах')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_not_in_list_and_not_fv(self, books_collector):
        books_collector.add_book_in_favorites('УК РФ')
        assert len(books_collector.get_list_of_favorites_books()) == 0

    def test_delete_book_in_favorites_book_in_fv(self, books_collector):
        books_collector.add_book_in_favorites('1001 и одна ночь на курсах')
        books_collector.delete_book_from_favorites('1001 и одна ночь на курсах')
        assert len(books_collector.get_list_of_favorites_books()) == 0

    def test_delete_book_in_favorites_book_not_in_fv(self, books_collector):
        books_collector.add_book_in_favorites('1001 и одна ночь на курсах')
        books_collector.delete_book_from_favorites('Утиные истории')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_return_list(self, books_collector):
        books_collector.add_book_in_favorites(list(books_collector.books_genre.keys())[0])
        books_collector.add_book_in_favorites(list(books_collector.books_genre.keys())[1])
        assert books_collector.get_list_of_favorites_books() == ['1001 и одна ночь на курсах', 'Приключение МонтеКиски']
