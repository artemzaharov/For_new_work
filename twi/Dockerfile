FROM python:3.8.2 as develop-target
LABEL maintainer="---" description="---"

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY . ./