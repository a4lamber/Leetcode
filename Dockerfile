# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Change to the leetcode_with_adam directory where mkdocs.yml is located
WORKDIR /app/leetcode_with_adam

# Run mkdocs serve when the container launches
ENTRYPOINT ["mkdocs"]
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
