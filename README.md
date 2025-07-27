# qa_python

# Тесты на метод __init__
1. test_init_default_value_books_genre - проверка, что books_genre по умолчанию - пустой словарь
2. test_init_default_value_favorites - проверка, что favorites по умолчанию - пустой список
3. test_init_default_value_genre - проверка, что genre по умолчанию - список с ожидаемыми жанрами
4. test_init_default_value_genre_age_rating - проверка, что genre_age_rating по умолчанию - список с жанрами, имеющими возрастные ограничения

# Тесты на метод add_new_book
5. test_add_new_book_add_two_books - проверка добавления двух книг в словарь books_genre
6. test_add_new_book_add_repeat_book - проверка повторного добавления одной и той же книги в словарь books_genre
7. test_add_new_book_check_length_title - проверка добавления книги в словарь books_genre исходя из длины ее названия (0, 1, 40, 41 символов)
    Параметры теста: длина названия книги - 0, 1, 40, 41 символов

# Тесты на метод set_book_genre
8. test_set_book_genre_valid_book_and_genre - проверка установки жанра для добавленной книге
    Параметры теста: все жанры, которые есть в списке genre
9. test_set_book_genre_change_genre - проверка изменения жанра для книги, которой ранее был установлен жанр
10. test_set_book_genre_invalid_book - проверка, что жанр нельзя установить для книги, которой нет в books_genre
12. test_set_book_genre_invalid_genre - проверка, что книге нельзя установить жанр, который не входит в список genre

# Тесты на метод get_book_genre
13. test_get_book_genre_valid_book - проверка, что для книги получен правильный жанр из books_genre
14. test_get_book_genre_book_with_empty_genre - проверка, что для добавленной книги получен пустой жанр
15. test_get_book_genre_invalid_book - проверка, что для книги не из books_genre вместо жанра возвращается None

# Тесты на метод get_books_with_specific_genre
16. test_get_books_with_specific_genre_when_genre_is_on_the_books_genre - проверка, что получен правильный список книг, относящийся к указанному жанру
17. test_get_books_with_specific_genre_when_genre_is_not_on_the_books_genre - проверка, что приходит пустой список книг, если указанного жанра нет в books_genre
18. test_get_books_with_specific_genre_when_genre_invalid - проверка, что приходит пустой список книг, если указанного жанра нет в списке жанров genre

# Тесты на метод get_books_genre
19. test_get_books_genre - проверка, что получен список тех книг, которые были добавлены в books_genre
    Параметры теста: две книги, одна книга, пустой список

# Тесты на метод get_books_for_children
20. test_get_books_for_children_when_genre_is_not_on_the_genre_age_rating - проверка, что получены только книги, жанры у которых не имеют возрастных ограничений. 
    Параметры теста: в books_genre - книги разных жанров, только жанры с возрастным ограничением, только жанр без возрастного ограничения, пустой список

# Тесты на метод add_book_in_favorites
21. test_add_book_in_favorites_one_book - проверка добавления одной книги в Избранное
22. test_add_book_in_favorites_add_repeat_book_in_favorites - проверка повторного добавления одной книги в Избранное
23. test_add_book_in_favorites_when_book_is_not_on_the_books_genre - проверка добавления книги, которой нет в books_genre

# Тесты на метод delete_book_from_favorites
24. test_delete_book_from_favorites_valid_book - проверка удаления книги из Избранного
25. test_delete_book_from_favorites_invalid_book - проверка удаления книги, которой нет в Избранном

# Тесты на метод get_list_of_favorites_books
26. test_get_list_of_favorites_books - проверка получения списка Избранных книг
    Параметры теста: в favorites - две книги, одна книга, пустой список
