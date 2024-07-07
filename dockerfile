
FROM python:3.9-slim


RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8501
WORKDIR /app

COPY . /app

RUN pip install  -r requirements.txt


ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
