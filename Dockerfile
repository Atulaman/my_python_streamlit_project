# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install streamlit and any other dependencies
RUN pip install --no-cache-dir streamlit

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run your Streamlit app
CMD ["python", "-m", "streamlit", "run", "main.py"]
