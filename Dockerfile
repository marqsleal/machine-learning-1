FROM python:3.10-slim

WORKDIR /credit

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["python3", "src/app.py"]
