# Use an official Python runtime as a parent image
FROM python:3.11.3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django app with Daphne and Redis
#CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "djangoProjectChatroom.asgi:application"]

CMD ["gunicorn", "djangoProjectChatroom.asgi:application" ,  "--bind" , "0.0.0.0:8000" , "--worker-class=uvicorn.workers.UvicornWorker" ,"--workers=4"]


#CMD ["gunicorn", "djangoProjectChatroom.asgi:application", "--bind","0.0.0.0", "-p", "8000", "-w","4"]