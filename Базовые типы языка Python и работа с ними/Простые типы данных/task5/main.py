speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 0.125  # стоимость за один килобайт

speed_in_kb_in_sec = speed / 1024
time_in_sec = 60 * 120

free_traffic = 500  # количество бесплатного трафика
file_size = time_in_sec * speed_in_kb_in_sec
total_coast = (file_size - free_traffic) * 0.125

print('Размер файла в килобайтах =', file_size)
print('За трафик придется заплатить:', total_coast)


