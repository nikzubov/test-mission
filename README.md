# Docker-compose для телеграмм бота с fastapi и nginx
Все работает, но без сертификата certbot.

`chmod +x install-docker.sh`
`chmod +x certbot/generate-certificate.sh`
`sudo sh install-docker.sh`
`docker compose up --build -d`