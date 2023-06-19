FROM python:3.9

WORKDIR /code

COPY . /code

RUN pip install -r /code/requirements.txt

CMD ["python", "/code/uvicorn_serve.py"]