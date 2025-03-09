from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Инициализация драйвера Firefox
driver = webdriver.Firefox()


def parse_prices(url):
    driver.get(url)
    time.sleep(5)  # Ожидание загрузки страницы

    prices = []
    page_number = 1

    while True:
        print(f"Парсинг страницы {page_number}...")

        # Ожидание загрузки карточек объявлений
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-name="CardComponent"]'))
            )
        except Exception as e:
            print(f"Ошибка при загрузке карточек: {e}")
            break

        # Поиск элементов с ценами
        items = driver.find_elements(By.CSS_SELECTOR, 'article[data-name="CardComponent"]')
        for item in items:
            try:
                # Ищем элемент с ценой
                price_element = item.find_element(By.CSS_SELECTOR, 'span[data-mark="MainPrice"]')
                price = price_element.text.strip()
                prices.append(price)
            except Exception as e:
                print(f"Ошибка при парсинге цены: {e}")

        # Попытка перейти на следующую страницу
        try:
            # Ищем кнопку перехода на следующую страницу
            next_button = driver.find_element(By.CSS_SELECTOR,
                                              'li._93444fe79c--page--tTWIr > a._93444fe79c--button--KVooB')

            # Прокручиваем страницу к кнопке и кликаем с помощью JavaScript
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            driver.execute_script("arguments[0].click();", next_button)

            # Ожидание загрузки следующей страницы
            time.sleep(5)
            page_number += 1
        except Exception as e:
            print(f"Не удалось перейти на следующую страницу: {e}")
            break

    return prices


def save_to_csv(prices, filename="prices.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Заголовок столбца
        for price in prices:
            writer.writerow([price])  # Запись каждой цены в новую строку


def main():
    url = "https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"
    prices = parse_prices(url)
    print("Найденные цены:")
    for price in prices:
        print(price)

    # Сохранение цен в CSV-файл
    save_to_csv(prices)
    print(f"Цены сохранены в файл prices.csv")

    driver.quit()  # Закрытие браузера


if __name__ == "__main__":
    main()