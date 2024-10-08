## test-mirror-app

`test-mirror-app` — это приложение для управления заказами на выгул собак через REST API. Приложение разработано на основе фреймворка FastAPI с использованием SQLAlchemy для работы с базой данных.

## Функционал

Приложение предоставляет два основных эндпоинта:

1. **Получение списка заказов на указанную дату**
   - **Метод:** `GET /orders/`
   - **Параметр:** `date` (дата в формате `YYYY-MM-DD`, на которую нужно получить список заказов)
   - **Возвращает:** Список заказов на указанную дату.

2. **Оформление нового заказа на прогулку**
   - **Метод:** `POST /orders/`
   - **Параметры:** 
     - `apartment_number` (номер квартиры)
     - `pet_name` (кличка питомца)
     - `pet_breed` (порода питомца)
     - `walk_date` (дата прогулки в формате `YYYY-MM-DD`)
     - `walk_time` (время начала прогулки в формате `HH:MM:SS`, допустимы только начала часа и половины)
     - `walker` (имя выгуливающего, либо "Пётр", либо "Антон")
   - **Создает:** Новый заказ на прогулку, если в это время выгуливающий свободен. В противном случае, возвращается ошибка.

## Требования

- Python 3.6-12
- Остальные зависимости указаны в `requirements.txt`

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/lolukuk/test-mirror-app.git
   cd test-mirror-app
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Win: venv\Scripts\activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

### Запуск приложения

1. Запустите приложение:

   ```bash
   uvicorn main:app --reload
   ```

2. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000` для доступа к документации Swagger UI, где вы сможете протестировать API.

### Структура проекта

```plaintext
test-mirror-app/
└── /app
│   │
│   ├── main.py           # Главный файл приложения, содержит эндпоинты API
│   ├── models.py         # Определение моделей базы данных (SQLAlchemy)
│   ├── schemas.py        # Определение Pydantic-схем для валидации данных
│   ├── crud.py           # CRUD-операции для работы с базой данных
│   ├── db.py       # Настройка подключения к базе данных
└── README.md         # Документация проекта
```
