FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./data ./data

CMD ["python", "-m", "src", "--interactive"]