# TODO Найдите количество книг, которое можно разместить на дискете
disketa = 1.44
one_symbol = 4
count_symbol = 25
count_str = 50
count_pages = 100
book = (one_symbol * count_symbol * count_str * count_pages)
book_mb = book/(1024 * 1024)
count_books = int(disketa/book_mb)

print("Количество книг, помещающихся на дискету:", count_books)
