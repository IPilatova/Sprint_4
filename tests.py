import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

# 1. Тесты на метод __init__

    def test_init_default_value_books_genre(self, collector):

        # проверяем, что books_genre по умолчанию - пустой словарь
        assert collector.books_genre == {}

    def test_init_default_value_favorites(self, collector):

        # проверяем, что favorites по умолчанию - пустой список
        assert collector.favorites == []

    def test_init_default_value_genre(self, collector):

        # проверяет, что genre по умолчанию - список
        # ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre == [
            'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'
        ]

    def test_init_default_value_genre_age_rating(self, collector):

        # проверяет, что genre_age_rating по умолчанию - список
        # ['Ужасы', 'Детективы']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

# 2. Тесты на метод add_new_book

    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяет, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_repeat_book(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем одну книгу дважды в books_genre
        collector.add_new_book(title)
        collector.add_new_book(title)

        # проверяет, что добавилась только одна книга и дубля нет
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'title, count_books',
        [
            ['', 0],
            ['!', 1],
            ['Название этой книги равно 40 символов!!!', 1],
            ['Название этой книги больше 40 символов!!!', 0]
        ]
    )
    def test_add_new_book_check_length_title(self, collector, title, count_books):

        # добавляем одну книгу с названием нужной длины
        collector.add_new_book(title)

        # проверяем, добавилась ли книга в словарь
        assert len(collector.get_books_genre()) == count_books

# 3. Тесты на метод set_book_genre

    @pytest.mark.parametrize(
        'genre',
        ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    def test_set_book_genre_valid_book_and_genre(self, collector, genre):

        title = 'Гордость и предубеждение и зомби'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # устанавливаем книге жанр
        collector.set_book_genre(title, genre)

        # проверяем, что жанр установился корректно
        assert collector.get_book_genre(title) == genre

    def test_set_book_genre_change_genre(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # устанавливаем книге жанр
        collector.set_book_genre(title, 'Детективы')

        # устанавливаем книге новый жанр
        collector.set_book_genre(title, 'Комедии')

        # проверяем, что жанр изменился
        assert collector.get_book_genre(title) == 'Комедии'

    def test_set_book_genre_invalid_book(self, collector):

        # добавляем книгу в books_genre
        collector.add_new_book('Гордость и предубеждение и зомби')

        # сохраняем список значений словаря в переменную
        previous_list_of_genre = list(collector.get_books_genre().values())

        title = 'Крик'
        genre = 'Ужасы'

        # устанавливаем книге, не входящей в books_genre, жанр
        collector.set_book_genre(title, genre)

        # сохраняем список значений словаря в переменную, чтобы далее ее сравнивать со списком значений до добавления жанра невалидной книги
        list_of_genre = list(collector.get_books_genre().values())

        # проверяем, что жанр не установился и список значений жанров в books_genre не изменился
        assert (
                title not in collector.books_genre
                and previous_list_of_genre == list_of_genre
        )

    def test_set_book_genre_invalid_genre(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # устанавливаем книге жанр, которого нет в списке genre
        collector.set_book_genre(title, 'Мюзикл')

        # проверяем, что жанр не установился
        assert collector.get_book_genre(title) != 'Мюзикл'

# 4. Тесты на метод get_book_genre

    def test_get_book_genre_valid_book(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # добавляем жанр для книги в books_genre
        collector.set_book_genre(title, 'Комедии')

        # проверяем, что жанр соответствует добавленному
        assert collector.get_book_genre(title) == 'Комедии'

    def test_get_book_genre_book_with_empty_genre(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # проверяем, что жанр у добавленной книги равен ''
        assert collector.get_book_genre(title) == ''

    def test_get_book_genre_invalid_book(self, collector):

        title = 'Гордость и предубеждение и зомби'
        title_invalid = 'Крик'

        # добавляем книгу в books_genre
        collector.add_new_book(title)

        # добавляем жанр для книги в books_genre
        collector.set_book_genre(title, 'Комедии')

        # проверяем, что для книги не из books_genre возвращается None
        assert collector.get_book_genre(title_invalid) is None

# 5. Тесты на метод get_books_with_specific_genre

    def test_get_books_with_specific_genre_when_genre_is_on_the_books_genre(self, collector):

        # добавляем книгу в books_genre и устанавливаем книге жанр
        titles_genres = {
            'Гордость и предубеждение и зомби':'Комедии',
            'Что делать, если ваш кот хочет вас убить':'Детектив',
            'Очень страшное кино':'Комедии',
            'Птицы':'Ужасы',
            'Головоломка':'Мультфильмы',
            'Чисто английские убийства':'Детектив'
        }

        for k,v in titles_genres.items():
            collector.add_new_book(k)
            collector.set_book_genre(k, v)

        # проверяем вывод списка с жанром, который есть в books_genre, например 'Комедии'
        assert collector.get_books_with_specific_genre('Комедии') == [
            'Гордость и предубеждение и зомби', 'Очень страшное кино'
        ]

    def test_get_books_with_specific_genre_when_genre_is_not_on_the_books_genre(self, collector):

        # добавляем книгу в books_genre и устанавливаем книге жанр
        titles_genres = {
            'Гордость и предубеждение и зомби':'Комедии',
            'Что делать, если ваш кот хочет вас убить':'Детектив',
            'Очень страшное кино':'Комедии',
            'Птицы':'Ужасы',
            'Головоломка':'Мультфильмы',
            'Чисто английские убийства':'Детектив'
        }

        for k,v in titles_genres.items():
            collector.add_new_book(k)
            collector.set_book_genre(k, v)

        # проверяем вывод списка с жанром, которого нет в books_genre, например 'Фантастика'
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_when_genre_invalid(self, collector):

        # проверяем, что books_with_specific_genre выводит пустой словарь, если жанра нет в списке жанров genre
        assert collector.get_books_with_specific_genre('Мюзикл') == []

# 6. Тесты на метод get_books_genre

    @pytest.mark.parametrize(
        'title',
        [
            ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'],
            ['Гордость и предубеждение и зомби'],
            []
        ]
    )
    def test_get_books_genre(self, collector, title):

        # добавляем книги в books_genre
        for i in title:
            collector.add_new_book(i)

        # проверяем, что названия книг в books_genre соответствуют title
        assert list(collector.get_books_genre().keys()) == title

# 7. Тесты на метод get_books_for_children
    @pytest.mark.parametrize(
        'titles_genres, books_for_children',
        [
            [
                {
                    'Гордость и предубеждение и зомби':'Комедии',
                    'Что делать, если ваш кот хочет вас убить':'Детектив',
                    'Один дома':'Комедии',
                    'Птицы':'Ужасы',
                    'Головоломка':'Мультфильмы',
                    'Матрица':'Фантастика'
                },
                ['Гордость и предубеждение и зомби', 'Один дома', 'Головоломка', 'Матрица']
            ],
            [
                {},
                []
            ],
            [
                {
                    'Что делать, если ваш кот хочет вас убить': 'Детектив',
                    'Птицы': 'Ужасы',
                },
                []
            ],
            [
                {
                    'Головоломка': 'Мультфильмы'
                },
                ['Головоломка']
            ]
        ]
    )
    def test_get_books_for_children_when_genre_is_not_on_the_genre_age_rating(
            self, collector,titles_genres, books_for_children
    ):

        # добавляем книги в books_genre и устанавливаем жанр
        for k,v in titles_genres.items():
            collector.add_new_book(k)
            collector.set_book_genre(k, v)

        # проверяем вывод списка books_for_children
        assert collector.get_books_for_children() == books_for_children

# 8. Тесты на метод add_book_in_favorites
    def test_add_book_in_favorites_one_book(self, collector):

        title1 = 'Гордость и предубеждение и зомби'
        title2 = 'Что делать, если ваш кот хочет вас убить'

        # добавляем две книги в books_genre
        collector.add_new_book(title1)
        collector.add_new_book(title2)

        # добавляем книгу, находящуюся в books_genre, в список favorites
        collector.add_book_in_favorites(title1)

        # проверяем, что книга добавилась в favorites
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_repeat_book_in_favorites(self, collector):

        title1 = 'Гордость и предубеждение и зомби'
        title2 = 'Что делать, если ваш кот хочет вас убить'

        # добавляем две книги в books_genre
        collector.add_new_book(title1)
        collector.add_new_book(title2)

        # добавляем книгу, находящуюся в books_genre, в список favorites
        collector.add_book_in_favorites(title2)

        # повторно добавляем книгу в список favorites
        collector.add_book_in_favorites(title2)

        # проверяем, что в список favorites добавилась только одна книга
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_when_book_is_not_on_the_books_genre(self, collector):

        title1 = 'Гордость и предубеждение и зомби'
        title2 = 'Что делать, если ваш кот хочет вас убить'

        # добавляем одну книгу в books_genre
        collector.add_new_book(title1)

        # добавляем вторую книгу в список favorites
        collector.add_book_in_favorites(title2)

        # проверяем, что в список favorites книга не добавилась
        assert len(collector.get_list_of_favorites_books()) == 0

# 9. Тесты на метод delete_book_from_favorites
    def test_delete_book_from_favorites_valid_book(self, collector):

        title = 'Гордость и предубеждение и зомби'

        # добавляем две книги в books_genre
        collector.add_new_book(title)

        # добавляем книгу, находящуюся в books_genre, в список favorites
        collector.add_book_in_favorites(title)

        # удаляем книгу из списка favorites
        collector.delete_book_from_favorites(title)

        # проверяем, что книга удалилась
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_invalid_book(self, collector):

        title1 = 'Гордость и предубеждение и зомби'
        title2 = 'Что делать, если ваш кот хочет вас убить'

        # добавляем одну книгу в books_genre
        collector.add_new_book(title1)

        # добавляем книгу, находящуюся в books_genre, в список favorites
        collector.add_book_in_favorites(title1)

        # удаляем из favorites книгу, которой нет в списке favorites
        collector.delete_book_from_favorites(title2)

        # проверяем, что книга не удалилась
        assert len(collector.get_list_of_favorites_books()) == 1

# 10. Тесты на метод get_list_of_favorites_books

    @pytest.mark.parametrize(
        'title_favorites',
        [
            ['Гордость и предубеждение и зомби'],
            ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'],
            []
        ]
    )
    def test_get_list_of_favorites_books(self, collector, title_favorites):

        title1 = 'Гордость и предубеждение и зомби'
        title2 = 'Что делать, если ваш кот хочет вас убить'

        # добавляем две книги в books_genre
        collector.add_new_book(title1)
        collector.add_new_book(title2)

        # добавляем книги в favorites
        for i in title_favorites:
            collector.add_book_in_favorites(i)

        # проверяем, что названия книг в favorites соответствуют title
        assert collector.get_list_of_favorites_books() == title_favorites