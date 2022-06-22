FROM python:3.8.3-alpine
WORKDIR /app
RUN apk add --no-cache gcc libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "start.sh"]
