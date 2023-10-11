# Использованные модули
* allure-pytest - генерация репортов
* allure-python-commons
* Faker - Генерация данных
* pydantic - Валидация JSON хем
* pytest
* requests
* pytest-rerunfailures - Перезапуск упавших тестов
* python-dotenv - Переменные окружения


# Установка

* pip install -r requirements.txt

#.env

(Пишу здесь чтобы вам не нужно было получать свой токен, креды - должны быть в secrets ci/cd)

API_KEY = 'e00da76e2fd4804d8fe53ae137fbb0aa'
URL = 'https://api.openweathermap.org'

# Docker

Чтобы упростить проверку енв файл входит в состав имейджа.

# Запуск

pytest -sv --alluredir=allure_report
allure serve allure_report/
