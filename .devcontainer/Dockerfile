# Dockerfile
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

ENV PYTHONDONTWRITEBYTECODE 1

ARG TOKEN

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# ENV PYTHONPATH $PYTHONPATH:/app

RUN pip install poetry

# WORKDIR "/workspaces/plateforme-data-demo-python/"

# RUN poetry install --no-root

