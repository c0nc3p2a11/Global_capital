FROM python:3.10-alpine

ENV mark=$mark

LABEL "Author"="Oleg Kiselev"

WORKDIR ./usr/weather_autotests

VOLUME /allure_report

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD pytest -m "$mark" -s -v tests/* --alluredir=allure_report
