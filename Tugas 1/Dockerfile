FROM python:3.10-slim-buster

WORKDIR /Tugas1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY Tugas1/ .

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["manage.py","runserver","0.0.0.0:5000"]