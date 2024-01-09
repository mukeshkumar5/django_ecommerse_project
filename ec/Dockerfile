# Use the official Python base image with the desired version
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /ec

# Copy the requirements.txt file to the working directory
COPY ./requirements.txt /ec/requirements.txt

# Install dependencies using pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . /ec

# Expose the port the Django app runs on (change to your desired port)
EXPOSE 8080

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
