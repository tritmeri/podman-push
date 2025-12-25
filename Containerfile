# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install the web server library
RUN pip install flask

# Copy the app file into the container
COPY app.py .

# Open the port so we can access the web app
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
