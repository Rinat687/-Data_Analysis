import csv

def process_csv(input_file, output_file):
    # Открываем файл для чтения
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)  # Читаем все строки в список

    # Обрабатываем каждую строку, начиная со второй (первая строка — заголовок)
    for row in rows[1:]:  # Пропускаем заголовок
        if row:  # Проверяем, что строка не пустая
            # Убираем "₽/мес." и преобразуем в число
            cleaned_value = row[0].replace('₽/мес.', '').strip()  # Убираем подстроку и лишние пробелы
            cleaned_value = cleaned_value.replace(' ', '')  # Убираем пробелы
            try:
                row[0] = int(cleaned_value)  # Преобразуем в число
            except ValueError:
                print(f"Ошибка: не удалось преобразовать '{cleaned_value}' в число. Пропускаем строку.")
                continue  # Пропускаем строку, если преобразование не удалось

    # Перезаписываем файл с обновлёнными данными
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)  # Записываем все строки обратно в файл

# Пример использования
input_file = 'prices.csv'  # Имя исходного файла
output_file = 'prices_processed.csv'  # Имя файла для сохранения результата
process_csv(input_file, output_file)

print(f"Файл '{input_file}' обработан и сохранён как '{output_file}'.")