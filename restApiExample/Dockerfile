FROM python:3.11
ENV PYTHONUNBEFFERED=1
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt
