# Use an official Python runtime as a parent image
FROM python:3.5

# Set the working directory to /app
WORKDIR /proxy_servies

# Copy the current directory contents into the container at /app
ADD . /proxy_servies

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 6002

# Define environment variable
ENV NAME proxy_servies

# Run run.py when the container launches
CMD ["python", "run.py"]