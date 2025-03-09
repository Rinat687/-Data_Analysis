import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Firefox()

# Открытие страницы
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(3)

# Поиск всех элементов товаров
divans = driver.find_elements(By.CLASS_NAME, "lsooF")

with open('prices.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])

    for divan in divans:
        try:
            price_text = divan.find_element(By.CLASS_NAME, "pY3d2").text.strip()  # Удаляем лишние пробелы
            # Разделяем текст на строки и берем первую цену
            first_price = price_text.split('\n')[0]
            # Удаляем символы "руб." и пробелы, затем преобразуем в число
            price = int(first_price.replace("руб.", "").replace(" ", ""))
            # Запись в CSV
            writer.writerow([price])

        except Exception as e:
            print(f"Ошибка при обработке элемента: {e}")

# Закрытие браузера
driver.quit()
