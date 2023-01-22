FROM python:3.9-slim-buster
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN pip install -e .
CMD ["python", "/src/app.py"]