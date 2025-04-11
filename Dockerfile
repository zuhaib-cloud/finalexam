# Pull a public Python base image from Amazon ECR Public to avoid Docker Hub rate limits
FROM public.ecr.aws/docker/library/python:3.9-slim

# Create an application directory
WORKDIR /app

# Copy only the app.py (or your entire source) into the container
COPY app.py /app

# Install Flask (and any other deps)
RUN pip install flask

# Expose port 5000 within the container
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
