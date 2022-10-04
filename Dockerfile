FROM python:3.7-slim

WORKDIR /app

COPY requirements1.txt requirements1.txt

RUN pip install numpy
RUN pip install -r requirements1.txt

COPY . /app

EXPOSE 3000


ENTRYPOINT [ "python" ]
CMD ["app.py"]
