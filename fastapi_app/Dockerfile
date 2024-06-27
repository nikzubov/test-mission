FROM python:3.11.4

COPY . /fastapi_app

WORKDIR /fastapi_app

EXPOSE 8000

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
