FROM python:3.11.0a6-alpine3.15

WORKDIR /telebots

RUN python -m pip install --upgrade pip

COPY . .

# install python dependencies
RUN pip install .

