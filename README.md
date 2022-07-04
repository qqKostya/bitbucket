Учебное прилодение на FASTAPI

1) Развернул docker
2) Развернул docker-compose с db postgresql
3) При локальном развертывании ссылка на проверку http://localhost:8002/ping
4) Проверка ДБ docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
hello_fastapi_dev=# \l

Дальнейшие действия: 
- составление схемы базы данных
- создание моделей для ДБ
- выдача необходимых доступов на github