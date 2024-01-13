FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /cat_shop
COPY ./req.txt /cat_shop/

RUN pip install -r req.txt

RUN pip install --no-cache-dir -r req.txt

COPY ./ /cat_shop

CMD flask --app app run --port=8000 --host=0.0.0.0
