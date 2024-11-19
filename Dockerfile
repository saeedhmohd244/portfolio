# Use the official Python image from the Docker
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python3", "my_portfolio/manage.py", "runserver", "0.0.0.0:8000"]



