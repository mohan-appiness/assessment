# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory to /app
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 8000


# Run app.py when the container launches
# CMD ["python", "app.py"]