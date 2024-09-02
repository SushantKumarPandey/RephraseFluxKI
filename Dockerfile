FROM python:3.11

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.fileWatcherType", "none"]

ADD app.py .
