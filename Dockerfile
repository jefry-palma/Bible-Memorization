FROM python:3.9

WORKDIR /app

RUN pip install pipenv
COPY . .
RUN pipenv lock --requirements > requirements.txt
RUN pip install --user -r requirements.txt
RUN rm Pipfile* requirements.txt