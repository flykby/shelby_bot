# ---- Base python ----
FROM python:3.11 AS base
RUN apt-get update
RUN mkdir /app
WORKDIR /app

# ---- Dependencies ----
FROM base AS dependencies
RUN pip3 install poetry==1.7.1
RUN poetry config virtualenvs.create false
COPY ./poetry.lock .
COPY ./pyproject.toml .
RUN poetry install


# ---- Release ----
FROM dependencies AS build
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY src/ /app/src/
COPY main.py /app/main.py
ENTRYPOINT ["python", "main.py"]
    
    