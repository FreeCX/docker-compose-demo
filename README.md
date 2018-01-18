# docker-compose-demo

## Как запускать
Создайте файл `.env` со следующим содержимым:
```bash
SECRET_KEY=<paste-your-secret-key>
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_SERVICE=postgres
DB_PORT=5432
```

Собираем контейнеры
```shell
$ docker-compose build
```

Cоздаём таблицу в БД
```shell
$ docker-compose run web /usr/local/bin/python create_demo.py
```

Запускаем
```shell
$ docker-compose up -d
```

Теперь можно открыть сам веб-сервис в браузере по адресу <http://localhost:5000>.

Для остановки работы контейнеров выполните следующую команду в директории с проектом
```bash
$ docker-compose stop
```
