FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python3", "-m","container1", "run", "--host=0.0.0.0", "--port=6000"]