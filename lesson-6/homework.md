# Домашнее задание №6
## Джанго-проект

Необходимо разработать собственный Джанго-проект. Тематика на выбор студента, но не заезженная (типа фильмы, блог и т.д.).
- Создать виртуальное окружение;
- Установить django, djangorestframework (внутри виртуального окружения само собой);
- Создать requirements.txt (при помощи pip freeze);
- Создаём джанго-проект (django-admin startproject <название проекта>);
- Создаём Джанго-приложение (./manage.py startapp <название приложения>);
- А дальше создаём класс-модель на выбор студента;
- Не забываем создать и применить миграции;
- Подключаем [DRF](https://www.django-rest-framework.org/) и создаём для него необходимые вьюшки и обрабатываем методы для работы с REST:
    - GET (получить список сущностей);
    - POST (обновить сущность);
    - PUT (создать новую сущность);
    - DELETE (удалить существующую сущность);
- В случае успеха код вовзрата 200, иначе -- 404;
- Ответ должны отдавать в формате json;
- Не забываем коммитить это (venv, \_\_pycache\_\_ и прочий мусор не нужно коммитить, но миграции нужно коммитить!);

#### Подсказка
Для отправки запросов можно использовать [Postman](https://www.postman.com/downloads/)