# Use an official Python runtime as a parent image
FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

WORKDIR /app/leetcode_with_adam

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]