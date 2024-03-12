# Dockerfile
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ARG TOKEN

ENV VIRTUAL_ENV=/opt/venv

WORKDIR /app

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONPATH $PYTHONPATH:/app

COPY . /app

RUN pip install poetry
RUN poetry install


ENTRYPOINT ["python3"]

CMD ["/app/src/main.py"]