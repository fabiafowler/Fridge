FROM python:3.5

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y 

COPY . .
RUN pip3 install -r requirements.txt

ENV DATABASE_URI="mysql+pymysql://root:root@34.89.61.95:3306/fridge_app"
ENV SECRET_KEY=“gsfwhdgfs”

EXPOSE 5000
ENTRYPOINT ["usr/local/bin/python3", "app.py"]


