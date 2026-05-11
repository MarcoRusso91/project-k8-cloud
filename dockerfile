FROM python:3.9-slim

WORKDIR /app

COPY home.py .

RUN pip install flask 

EXPOSE 5000

CMD ["python", "home.py"]