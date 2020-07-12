import utils
import sorts

bookshelf = utils.load_books('./A Sorted Tale/books_small.csv')
# for item in bookshelf:
#     print(item['title'])

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    return len(book_a['author']) + len(book_a['title']) > len(book_b['author']) + len(book_b['title'])

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
# for item in sort_1:
#     print(item['title'])

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
# for item in sort_2:
#     print(item['author'])

bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
# for item in bookshelf_v2:
#     print(item['author'])

long_bookshelf = utils.load_books('./A Sorted Tale/books_large.csv')
# sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
long_bookshelf_v1 = long_bookshelf.copy()
sorts.quicksort(long_bookshelf_v1, 0, len(long_bookshelf_v1) - 1, by_total_length)
