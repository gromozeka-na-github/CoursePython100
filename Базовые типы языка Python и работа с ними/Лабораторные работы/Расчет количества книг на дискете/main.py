
floppy_disk_capacity = 1.44
number_of_pages = 100
number_of_lines = 50
characters_per_line = 25
character_size = 4

line_size = characters_per_line * character_size
page_size = number_of_lines * line_size
book_size = number_of_pages * page_size

book_size_kb = book_size / 1024
book_size_Mb = book_size_kb / 1024


print("Количество книг, помещающихся на дискету:", int(floppy_disk_capacity // book_size_Mb))