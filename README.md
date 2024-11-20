# qa_python
test_add_new_book_negative_cases - тест проверяет не добавление книг с пустым именем или с длиной более 40 символов.

test_set_book_genre_return_book_and_genre - тест проверяет установку жанра для книги, использованы все доступные параметры.

test_set_book_genre_not_in_genre_list - тест проверяет не добавление жанра не из спискаю.

test_get_books_with_specific_genre_return_two_books - тест проверяет работу гет метода по всем книгам жанра.

test_get_books_genre_return_genre - тест проверяет раборяет гет запрос по имени книги, возвращает жанр.

test_get_books_for_children_return_two - тест проверяет работа метода по генерации списка с детскими книгами.

test_add_book_in_favorites_book_in_list_and_not_in_fv - проверка добавления книги в избранное.

test_add_book_in_favorites_book_in_list_and_in_fv - проверка повторного добавления книги в избранное.

test_add_book_in_favorites_book_not_in_list_and_not_fv - проверка не добавления книги в избранное, книга не в словаре.

test_delete_book_in_favorites_book_in_fv - проверка удаления книги из избранного.

test_delete_book_in_favorites_book_not_in_fv - проверка удаления книги из избранного, книги нет в избранном.

get_list_of_favorites_books - проверка получения списка избранных книг