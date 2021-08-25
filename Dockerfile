FROM python:3.4


WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["gunicorn", "dcc_python_django_example.wsgi"]