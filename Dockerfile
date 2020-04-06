FROM python:3.7
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV DATABASE_URI "mysql+pymysql://root:password@mysql:3306/flaskapp"
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]


