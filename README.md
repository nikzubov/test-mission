# Docker-compose для телеграмм бота с fastapi и nginx и certbot

Инструкция для запуска проекта. 
В директориях fastapi_app и tgbot_app представлены примеры базовых проектов с минимальными функциями, требующимися для демонстрации работы.

## Подготовка

Для начала требуется создать три файла с переменными окружения - один для телеграмм бота, один для api и один для docker-compose:
* В корневой директории test-mission:
`touch .env`
`vim .env` - после чего вставить
```
POSTGRES_USER=<пользователь для postgres>
POSTGRES_PASSWORD=<пароль для пользователя>
POSTGRES_DB=<имя базы>
R_PASSWORD=<пароль для redis>
```
Далее требуется сохранить изменения - `:wq`
* В директории fastapi_app:
`touch .env`
`vim .env` - после чего вставить
    ```
    POSTGRES_USER=<пользователь для postgres>
    POSTGRES_PASSWORD=<пароль для пользователя>
    POSTGRES_DB=<имя базы>
    ```
Далее требуется сохранить изменения - `:wq`
* В директории tgbot_app:
`touch .env`
`vim .env` - также вставляем переменные
```
R_PASSWORD=<пароль для redis>
T_TOKEN=<токен, который был выдан BotFather>
```
Далее требуется сохранить изменения - `:wq`

## Установка докер
Требуется сделать скрипт установки исполняемым:
`chmod +x install-docker.sh`
После введите команду:
`sudo sh install-docker.sh`
Проверим корректно ли установился докер:
`docker --version`

## Корректировка названия доменов и настройка DNS

Требуется зайти в раздел редактирования DNS вашего домена и указать в A-записи IP-адрес вашего сервера. Смена DNS обычно не занимает много времени, в ближайшие 15-20 минут ваш домен будет отдавать новый IP, для проверки введите команду:
`dig a <ваш домен>`

После чего перейдите `vim nginx/nginx.conf` и укажите его вместо ```anakinnikita.ru``` ваш домен, то же самое сделайте в docker-compose.yml:
```command: certonly --webroot -w /var/www/html --email anakinnikitaa@gmail.com -d anakinnikita.ru --cert-name=certfolder --key-type rsa --agree-tos```
Замените anakinnikitaa@gmail.com на ваш почтовый ящик и anakinnikita.ru на ваш домен.
## Запуск контейнеров
Теперь можно запускать контейнеры:
`docker compose up --build -d`
Приложение запущено.