FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python3", "-m","container2", "run", "--host=0.0.0.0", "--port=8001"]