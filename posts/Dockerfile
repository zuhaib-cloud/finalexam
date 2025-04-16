FROM public.ecr.aws/docker/library/python:3.9-slim
 
ENV PYTHONUNBUFFERED=1
 
# Set a custom work directory
WORKDIR /usr/src/flask-app
 
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
 
# Copy app file
COPY ./app.py .
 
# Install Flask
RUN pip install --no-cache-dir flask
 
# Expose the port Flask runs on
EXPOSE 5000
 
# Run the app
CMD ["python", "app.py"]
