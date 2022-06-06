FROM python:3.9

WORKDIR /app

COPY . ./app

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

EXPOSE 8000

CMD ["bash", "app/run.sh"]
