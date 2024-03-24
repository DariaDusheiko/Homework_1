# Указываю базовый образ, чтобы построить новый образ поверх, в моем случае таким образом является последний созданный
FROM ubuntu:latest

# Указываю сведения о том, кто создал образ
LABEL maintainer="dvdusheiko@edu.hse.ru"

# Указываю команды для внесения изменений в образ, а затем контейнеры, запускаемые с этого образа
# по обновлению до нужной версии питона или по установке питона
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3-venv

# Задаю рабочую директорию для следующей инструкции
WORKDIR /app/

# по установке нужной среды
RUN python3 -m venv /app/venv

# Устанавливаю переменных среды в контейнерах, созданных из образа
ENV PATH="/app/venv/bin:$PATH" \
    TEMPLATE_FILE_NAME='./templates/index.html'\
    INDEX_FILE_NAME='./public/index.html'\
    RESUME_FILE_NAME='resume.txt'\
    user_id='351297070'\
    access_token='a3cc68d2a3cc68d2a3cc68d25ba0db00e5aa3cca3cc68d2c61273f5e18643b9b0045357'

# Копирую в контейнер файлы и папки
COPY . /app

# Указываю команды для внесения изменений в образ, а затем контейнеры, запускаемые с этого образа
# по установке нужных библиотек
RUN pip install -r requirements.txt

# устанавливаю приложение по умолчанию, используемое каждый раз, когда контейнер создается из образа
ENTRYPOINT ["python3", "/app/1.py"]