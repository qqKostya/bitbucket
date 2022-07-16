## Учебное приложение на FASTAPI

1) Развернул docker
2) Развернул docker-compose с db postgresql
3) При локальном развертывании ссылка на проверку http://localhost:8002/ping
4) Проверка ДБ docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
hello_fastapi_dev=# \l

Дальнейшие действия: 
- составление схемы базы данных
- создание моделей для ДБ
- создать нову ветку куда пушить новые изменения

Готово:
- схема баззы данных (https://dbdesigner.page.link/sktk5h51rfAMzzqd7)
- новая ветка

Update schema db:
- id int primary key, auto increment
- ФИО VARCHAR
- Должность VARCHAR
- Дата приема на работу DATE (так как у нас по ТЗ должна храниться только дата начала работы, без времени и окончания)
- Размер заработной платы	INT (будем хранить без условных копеек)
- id начальника (для понимания наличия начальника и кто им является, ссылаться будем на id primary key)
