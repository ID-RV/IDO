# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44
one_symbol_size_byte = 4
character_count = 25
line_count = 50
page_count = 100

disk_size_byte = disk_size_mb*(2**20)
book_size_byte = one_symbol_size_byte*character_count*line_count*page_count
book_count = int(disk_size_byte/book_size_byte)

print("Количество книг, помещающихся на дискету:", book_count)
