# Use an official Python runtime as a parent image
FROM docker

RUN apk add python3 && apk add py3-pip
# Set the working directory in the container
WORKDIR /usr/src/web

# Copy the current directory contents into the container at /usr/src/app
COPY /web /usr/src/web

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# CMD ["python", "app.py"]
