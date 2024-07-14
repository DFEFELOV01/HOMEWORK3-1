#используй питон такой-то версии
# Собрать контейнер:
# cd homework_03
# docker build -t myapp .

# Запусить:
# docker run -p 8000:8000 myapp

FROM python:3.12.2-bookworm

#задаёт рабочую директорию для следующей инструкции
WORKDIR /

COPY pyproject.toml poetry.lock ./
#установка нужных пакетов
RUN pip install fastapi==0.111.0
RUN pip install uvicorn
RUN pip install --upgrade pip poetry==1.8.3
RUN poetry config virtualenvs.create false --local

COPY . .

EXPOSE 8000
##описывает команду с аргументами,
#которую нужно выполнить когда контейнер будет запущен.
#Аргументы могут быть переопределены при запуске контейнера. В файле может присутствовать лишь одна инструкция CMD.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]