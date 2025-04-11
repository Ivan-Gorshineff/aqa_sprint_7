# QA Python Sprint 7 
## Структура проекта

`tests/` папка с тестами
- `test_create_courier.py` — тесты для создания курьерa.
- `test_login_courier.py` — тесты для авторизации курьерa.
- `test_create_order.py` — тесты для создания заказов.
- `test_get_orders_list.py` — тесты для получения списка заказов.

`conftest.py` фикстуры для создания тестовых данных и очистки после тестов.

`api_users.py` класс для работы с API.

`helper.py` утилиты для генерации тестовых данных.

`data_users.py` предопределённые данные для тестов.

`urls.py` главная страница с URL эндпоинтов API.

`requirements.txt` _список зависимостей проекта.
