FROM python:3.11.4

COPY . /tg_bot

WORKDIR /tg_bot

EXPOSE 222

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]